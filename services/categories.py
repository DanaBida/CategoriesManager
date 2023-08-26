import os
import uuid
from db.categories.dataAccess import CategoriesDataAccess
from db.categories.files.dataAccess import FilesDataAccess
from common.errors import NotFoundError


class CategoriesService:
    # Refactor Note: Use sql injection for further tests
    def __init__(self):
        self.categoriesDA = CategoriesDataAccess()
        self.filesDA = FilesDataAccess()

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
        self.filesDA.store(dirName, fileName, fileContent)

    def sumAllNumbersInTypeCategories(self, type: str):
        totalSum = 0

        def sumRowNumericValues(row):
            nonlocal totalSum
            print(row)
            numericValues = [
                value for value in row if isinstance(value, (int, float))]
            totalSum += sum(numericValues)

        self.filesDA.applyHandlerOnDirectoryFilesRows(
            sumRowNumericValues, type)

        return totalSum
