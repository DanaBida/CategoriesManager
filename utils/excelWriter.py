import xlsxwriter

class ExcelWriter:
  def __init__(self, fileName):
    self.workbook = xlsxwriter.Workbook(fileName)
    self.worksheet = self.workbook.add_worksheet()

  def write(self, column, data):
    self.worksheet.write(column, data)
    self.workbook.close()



