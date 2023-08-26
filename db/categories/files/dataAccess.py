from io import BytesIO
import os
from .config import FileStorageConfig 

class FilesDataAccess:
    def store(self, dirPath: str, fileName: str, content: bytes):
        fullDirPath = os.path.join(FileStorageConfig["path"], dirPath)
        file = BytesIO(content)
        os.makedirs(fullDirPath, exist_ok=True)
        filePath = os.path.join(fullDirPath, fileName)
        with open(filePath, "wb") as outputFile:
            outputFile.write(file.read())
        file.close()