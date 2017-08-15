# Импортируем библиотеки pyplot и openpyxl

from matplotlib import pyplot
from openpyxl import load_workbook

# Загрузить таблицу из файла Exel в переменную wd
wd=load_workbook('data_analysis_lab.xlsx')
# Загружаем лист с именем "Data" в переменную sheet
sheet=wd['Data']
def getvalue(x): return x.value
map(getvalue, sheet['A'][1:]) # Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)

list_x = list (map(getvalue,sheet['A'][1:]))
list_y = list (map(getvalue,sheet['B'][1:]))

pyplot.plot(list_x, list_y, label="Метка") # Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y
pyplot.show() # показать график


