class CategoriesDataAccess:
    def __init__(self):
        # Refactor Note: I would store the categories in db with filePath to s3 storage
        # {"asian": {"region": "US", "type": "food", "fileName": ""}
        self.categories = {}

    def addCategory(self, categoryName: str, region: str, type: str):
        newCategory = {
            "region": region, 
            "type": type,
        }
        self.categories[categoryName] = newCategory
        return newCategory

    def getCategories(self):
        return self.categories
    
    def getCategoryInfo(self, categoryName: str):
        print(self.categories)
        if categoryName in self.categories:
            return self.categories[categoryName]
        return None