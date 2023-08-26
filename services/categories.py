import os
import uuid
from db.categories.dataAccess import CategoriesDataAccess
from common.filesStorage.directoryDataAccess import DirectoryDataAccess
from db.categories.config import FileStorageConfig
from common.errors import NotFoundError


class CategoriesService:
    # Refactor Note: Use sql injection for further tests
    def __init__(self):
        self.categoriesDA = CategoriesDataAccess()
        self.directoryDA = DirectoryDataAccess(FileStorageConfig["path"])

    def addCategory(self, categoryName: str, region: str, type: str):
        return self.categoriesDA.addCategory(categoryName, region, type)

    def getCategories(self):
        return self.categoriesDA.getCategories()

    def uploadCategoryFile(self, categoryName: str, fileContent: bytes):
        categoryInfo = self.categoriesDA.getCategoryInfo(categoryName)
        if categoryInfo is None:
            raise NotFoundError(f"Category '{categoryName}' not found")
        # store multiple files with same name
        fileName = str(uuid.uuid4())+'.xlsx'
        dirName = os.path.join(categoryInfo["type"], categoryName)
        self.directoryDA.storeFileInDirectory(dirName, fileName, fileContent)

    def sumAllNumbersInTypeCategories(self, type: str):
        totalSum = 0

        def sumRowNumericValues(row):
            nonlocal totalSum
            numericValues = [
                value for value in row if isinstance(value, (int, float))]
            totalSum += sum(numericValues)

        self.directoryDA.applyHandlerOnDirectoryFilesRows(
            sumRowNumericValues, type)

        return totalSum

    def getContainsTermCategoriesRegions(self, term):
        categoriesContainsTerm = self.directoryDA.getSubDirectoryNamesContainsTermAtLeastInOneFile(
            term)
        categoriesInfo = self.getCategories()
        categoriesContainsTermRegions = map(
            lambda category: categoriesInfo[category]["region"],
            categoriesContainsTerm)
        return categoriesContainsTermRegions
