import pandas

class FileLoader:
    def load(self, path):
        file = pandas.read_csv(path, sep=",")
        print(f"Loading dataset of dimensions {file.shape[0]} x {file.shape[1]}")
        return file
    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(-n))
