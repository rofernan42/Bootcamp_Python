from FileLoader import FileLoader
from YoungestFellah import YoungestFellah

fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
print(YoungestFellah(df, 2004))