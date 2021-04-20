import pandas

def YoungestFellah(df, year):
    subdf = df[["Sex", "Age", "Year"]]
    subdf = subdf.loc[subdf["Year"] == year]
    subdf_m = subdf.loc[subdf["Sex"] == "M"]["Age"].min()
    subdf_f = subdf.loc[subdf["Sex"] == "F"]["Age"].min()
    return {"f": subdf_f, "m": subdf_m}
