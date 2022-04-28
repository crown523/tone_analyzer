import xlsxwriter as xlwriter

def generate(title_info, data):
    workbook = xlwriter.Workbook(title_info + '.xlsx')
    worksheet = workbook.add_worksheet()

    col_headers = data.pop(0)
    for i in range(len(col_headers)):
        worksheet.write(0, i+1, col_headers[i])

    row_num = 1
    for row in data:
        for i in range(len(row)):
            worksheet.write(row_num, i, row[i])
        row_num += 1

    workbook.close()