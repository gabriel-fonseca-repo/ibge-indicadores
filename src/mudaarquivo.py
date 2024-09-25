import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Dados'
ws.append(['ID', 'MUNICÍPIO', 'PRIMEIRO_NOME'])

with open('dados.txt', 'r', encoding='utf-8') as file:
    next(file)
    for line in file:
        parts = line.strip().split(',')
        ws.append([parts[0].strip(), parts[1].strip(), parts[2].strip()])

wb.save('dados.xlsx')
