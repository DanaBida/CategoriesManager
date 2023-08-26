# Refactor Note: I would store the categories in sql db with index on the category name for efficient searches (if its unique, could be the primary key)
# Then, this class implementation would be changed to ORM queries

class CategoriesDataAccess:
    def __init__(self):
        # example of data: {"asian": {"region": "US", "type": "food"}}
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
        if categoryName in self.categories:
            return self.categories[categoryName]
        return None
