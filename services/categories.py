import os
import uuid
from db.categories.dataAccess import CategoriesDataAccess
from db.categories.files.dataAccess import FilesDataAccess
from common.errors import NotFoundError

class CategoriesService:
    #Refactor Note: Use sql injection for further tests
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
        self.filesDA.store(os.path.join(categoryInfo["type"], categoryName), str(uuid.uuid4()), fileContent)