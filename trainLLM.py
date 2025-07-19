from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter, Language
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOllama
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
import codeBaseReader
import constants

def getRecursiveCharacterTextSplitter(language, chunkSize, chunkOverlap):
    languageToPass = Language.JS
    if language == "python": 
        languageToPass = Language.PYTHON
    return RecursiveCharacterTextSplitter.from_language(language=languageToPass, chunk_size=chunkSize, chunk_overlap=chunkOverlap)

def trainLLMWithExternalContext(codeLangauge = constants.DEFAULT_CODE_BASE_LANGUAGE, pdfToLoad = "", codeBaseDirPath = "", pdfChunkSize = constants.DEFAULT_DOC_CHUNK_SIZE, pdfChunkOverlapSize = constants.DEFAULT_DOC_OVERLAP_SIZE, codeBaseChunkSize = constants.DEFAULT_CODE_BASE_CHUNK_SIZE, codeBaseChunkOverlapSize = constants.DEFAULT_CODE_BASE_OVERLAP_SIZE):
    docData = PyPDFLoader(pdfToLoad).load()
    codeBaseData = codeBaseReader.readCodeBase(codeBaseDirPath)
    codeSplitter = getRecursiveCharacterTextSplitter(codeLangauge, codeBaseChunkSize, codeBaseChunkOverlapSize)
    textSplitter = CharacterTextSplitter(chunk_size = pdfChunkSize, chunk_overlap = pdfChunkOverlapSize)
    docChunks = textSplitter.split_documents(docData)
    codeChunks = codeSplitter.split_documents(codeBaseData)
    allChunks = docChunks + codeChunks
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorDB = FAISS.from_documents(allChunks, embeddings)
    retriever = vectorDB.as_retriever()
    llm = ChatOllama(model="mistral")

    # Set up the conversational retrieval chain
    LLMmodel = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
    )

    return LLMmodel, retriever
    

