import csv

# csvライブラリのマッパー


class CsvWrapper:

    """
    csv#readerメソッドをラッパーしたクラス

    """

    def readCsv(self, getPath):
        with open(getPath, newline='') as gf:
            read = csv.reader(gf)
            arrys = []
            for row in read:
                arrys.append(row)
        return arrys

    """
    csv#writerメソッドをラッパーしたクラス
    """

    def writeCsv(self, setPath, arrys, mode="w"):
        with open(setPath, mode) as sf:
            write = csv.writer(sf)
            for row in arrys:
                write.writerow(row)
