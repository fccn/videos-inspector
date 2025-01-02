import openpyxl

if __name__ == "__main__":
    data = openpyxl.load_workbook("file.xlsx")
    sheet_obj = data.active
    cell_obj = sheet_obj.cell(row = 1, column = 1)
    print(cell_obj.value)