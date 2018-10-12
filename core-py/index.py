from sys import argv
from openpyxl import load_workbook
from CollectingData import CollectingData
from Calculator import TimeConverter, GetParameter

wb = load_workbook(argv[1])
sheet = wb.active

collectingData = CollectingData(sheet)
datas = collectingData.findNonGajiInduk()   # List 2D semua row SPM non Gaji Induk
date = collectingData.date

timeConverter = TimeConverter(datas)
durationsInSecond = timeConverter.durations()   # List durasi dalam detik
lazySpm = timeConverter.lazySpm     # List SPM dengan durasi > 1 jam

getParameter = GetParameter(durationsInSecond, lazySpm, date)
print(getParameter.toJson())
