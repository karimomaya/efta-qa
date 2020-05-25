import xlwt


def generate_excel(file_name, data):
    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("Sheet 1")
    fill_excel_data(data, sheet1)
    book.save(file_name + '.xlsx')


def fill_excel_data(data, sheet):
    for index, doc in enumerate(data):
        col_num = 0
        class_arr = doc['_id']
        sheet.write(index, col_num, doc['total'])
        col_num += 1
        if class_arr is None:
            sheet.write(index, col_num, 'null')
            col_num += 1
        else:
            for cls in class_arr:
                sheet.write(index, col_num, cls)
                col_num += 1
