from FileLoader import FileLoader
from HowManyMedalsByCountry import HowManyMedalsByCountry

fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
print(HowManyMedalsByCountry(df, 'France'))