import trainLLM
import argparse
import constants


parser = argparse.ArgumentParser(description="A script that processes files with flags.")

# arguments (flags)
parser.add_argument('--code_base_dir', type=str, help='Path to the code base dir.')
parser.add_argument('--doc_dir', type=str, help='Path to the doc dir') # this doc can be anything like code syntax (Knowledge about the code)
parser.add_argument("--code_base_chunk_size",type=str, default=constants.DEFAULT_CODE_BASE_CHUNK_SIZE, help='Enter the chunk size for the code base')
parser.add_argument("--code_base_overlap_size",type=str, default=constants.DEFAULT_CODE_BASE_OVERLAP_SIZE, help='Enter the chunk overlap size for the code base')
parser.add_argument("--doc_chunk_size",type=str, default=constants.DEFAULT_DOC_CHUNK_SIZE, help='Enter the chunk size for the external doc')
parser.add_argument("--doc_overlap_size",type=str, default=constants.DEFAULT_DOC_OVERLAP_SIZE, help='Enter the chunk overlap size for the external doc')
parser.add_argument("--base_code_language", type=str, help='Base code language')

# Parse the arguments
args = parser.parse_args()

print(args)

# Access the parsed arguments
codeBaseDirPath = args.code_base_dir
docDirPath = args.doc_dir
codeBaseChunkOverlapSize = args.code_base_overlap_size
codeBaseChunkSize = args.code_base_chunk_size
docChunkSize = args.doc_chunk_size
docChunkOverlapSize = args.doc_overlap_size
baseCodeLanguage = args.base_code_language

print(baseCodeLanguage, docDirPath, codeBaseDirPath, docChunkSize, docChunkOverlapSize, codeBaseChunkSize, codeBaseChunkOverlapSize)
LLMModel, retriever = trainLLM.trainLLMWithExternalContext(baseCodeLanguage, docDirPath, codeBaseDirPath, docChunkSize, docChunkOverlapSize, codeBaseChunkSize, codeBaseChunkOverlapSize)

chatHistory = []
while True:
    query = input("\nQuery: ")
    
    if query.lower() in ["exit", "quit"]:
        print("Terminating...")
        break

    relevant_docs = retriever.get_relevant_documents(query)
    
    if not relevant_docs:
        print("\nAnswer: Not able to find in document")
        chatHistory.append((query, "Not able to find in document"))
        continue

    result = LLMModel({
        "question": query,
        "chat_history": chatHistory
    })

    print("\nAnswer:", result["answer"])

    chatHistory.append((query, result["answer"]))