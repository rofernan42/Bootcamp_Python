from FileLoader import FileLoader
from ProportionBySport import ProportionBySport

fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
print(ProportionBySport(df, 2004, 'Tennis', 'F'))