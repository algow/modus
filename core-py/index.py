from sys import argv
from openpyxl import load_workbook
from CollectingData import CollectingData
from Calculator import timeConverter, GetParameter

wb = load_workbook(argv[1])
sheet = wb.active

collectingData = CollectingData(sheet)
datas = collectingData.findNonGajiInduk()
date = collectingData.date.value

timeConverter = timeConverter(datas)
durationsInSecond = timeConverter.durations()
lazySpm = timeConverter.lazySpm

getParameter = GetParameter(durationsInSecond, lazySpm, date)
print(getParameter.toJson())
