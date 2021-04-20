class SpatioTemporalData:
    def __init__(self, df):
        self.df = df
    def when(self, location):
        subdf = self.df.loc[(self.df["City"] == location)].drop_duplicates(["Year"])
        return list(subdf["Year"])
    def where(self, date):
        subdf = self.df.loc[(self.df["Year"] == date)].drop_duplicates(["City"])
        return list(subdf["City"])