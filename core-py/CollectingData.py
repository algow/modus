class CollectingData:
    __relevantRow = []
    __relevantRows = []
    __j = 5

    def __init__(self, activeSheet):
        self.__activeSheet = activeSheet
        self.date = self.__activeSheet['E5']

    def findNonGajiInduk(self):
        if self.__activeSheet[self.__activeCell()].value is not None:
            if self.__activeSheet[self.__activeCell()].value != "GAJI INDUK":
                self.__collectingRowData()
            self.__j += 1
            # Recursion
            self.findNonGajiInduk()
            return self.__relevantRows
        return None

    def __collectingRowData(self):
        for i in range(2, 10):
            nonGaji = self.__activeSheet.cell(row=self.__activeSheet[self.__activeCell()].row, column=i)
            self.__relevantRow.append(nonGaji.value)
        self.__relevantRows.append(self.__relevantRow)
        # Reset relevantRow dadi list kosong ben gak numpuk seko data hasil rekursi
        self.__relevantRow = []

    def __activeCell(self):
        active = 'D{0}'.format(self.__j)
        return active
