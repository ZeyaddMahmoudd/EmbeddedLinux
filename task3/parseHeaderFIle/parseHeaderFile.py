from xlwt import Workbook

file_path = "/home/zeyad/Desktop/embeddedlinuxtasks/task3/parseHeaderFIle/icu.h"
file = open(file_path, "r")

fun_start = ["void", "uint8", "uint8", "uint16", "uint32", "uint64", "float32", "float64"]

id_str = "IDX00"
id_int = 1

row = 0
col = 0

wb = Workbook()
sheet = wb.add_sheet('icu')

for x in file:
    if x[0] == " " :
        continue
    y = x.split(" ")
    if y[0] in fun_start:
        print(x[0:-1])
        sheet.write(row, col, x[0:-1])
        sheet.write(row, col + 1, id_str + str(id_int + row))
        row += 1

wb.save('parseHeaderFile.xls')