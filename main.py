from fastapi import FastAPI
from routers import categories

app = FastAPI()

app.include_router(categories.router)


# workbook = xlsxwriter.Workbook('categories.xlsx')
# worksheet.write('A1', 'Hello..')