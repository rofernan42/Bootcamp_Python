from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
sp = SpatioTemporalData(df)
print(sp.where(1896))
print(sp.where(2016))
print(sp.when('Paris'))
print(sp.when('Athina'))
print(sp.when('London'))