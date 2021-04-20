from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
mpl = MyPlotLib()
mpl.histogram(df, ["Height", "Weight"])
mpl.density(df, ["Height", "Weight"])
mpl.pair_plot(df, ["Height", "Weight"])
mpl.box_plot(df, ["Height", "Weight"])