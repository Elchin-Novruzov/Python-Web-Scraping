import xlsxwriter

book = xlsxwriter.Workbook('Elchin_Novruzov.xlsx')
page = book.add_worksheet()

page.write(0, 0, '')


book.close()
