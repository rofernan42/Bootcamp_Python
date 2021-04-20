from FileLoader import FileLoader
from HowManyMedals import HowManyMedals

fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
print(HowManyMedals(df, 'Kjetil Andr Aamodt'))