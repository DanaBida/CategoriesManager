from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from common.errors import NotFoundError
from services.categories import CategoriesService

router = APIRouter(
    prefix="/categories",
)

categoriesService = CategoriesService()


@router.get("/")
def read_categories():
    return categoriesService.getCategories()


@router.post("/", status_code=201)
def create_category(category_name: str, region: str, type: str):
    return categoriesService.addCategory(category_name, region, type)


@router.post("/upload")
async def upload_file(category_name: str, file: UploadFile = File(...)):
    try:
        categoriesService.uploadCategoryFile(category_name, file.file.read())
    except NotFoundError as e:
        return JSONResponse(content={f"message": "Failed to upload file, {e}"}, status_code=400)


@router.get("/sumType")
def sum_type(type: str):
    return categoriesService.sumAllNumbersInTypeCategories(type)
