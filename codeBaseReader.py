import os
from langchain_core.documents import Document

def readCodeBase(projectPath):
    documents = []
    for dirPath, directories, fileNames in os.walk(projectPath):
        directories[:] = [d for d in directories if d not in ["node_modules", "public"]]
        for fileName in fileNames:
            if fileName.endswith(('.js', '.json', '.md')):
                filePath = os.path.join(dirPath, fileName)
                with open(filePath, encoding="utf-8") as file:
                    content = file.read()
                    documents.append(Document(
                        page_content=content,
                        metadata={"source": filePath}
                    ))
    return documents

