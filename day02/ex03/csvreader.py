class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = name
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        pass
    def __enter__(self):
        self.fp = open(self.filename, "r")
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.fp.close()

    def getdata():
        pass
    def getheader():
        pass