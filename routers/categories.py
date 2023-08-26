from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from common.errors import NotFoundError
from .models import Category
from services.categories import CategoriesService

router = APIRouter(
    prefix="/categories",
)

categoriesService = CategoriesService()

@router.get("/")
def read_categories():
    return categoriesService.getCategories()

@router.post("/", status_code=201)
def create_category(category: Category):
    return categoriesService.addCategory(category.name, category.region, category.type)

@router.post("/upload")
async def upload_file(categoryName, file: UploadFile = File(...)):
    try:
        content = await file.read()
        categoriesService.uploadCategoryFile(categoryName, content)
    except NotFoundError as e:
        return JSONResponse(content={f"message": "Failed to upload file, {e}"}, status_code=400)