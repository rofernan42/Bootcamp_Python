def ProportionBySport(df, year, sport, sex):
    df2 = df.drop_duplicates(["ID", "Year"])
    comp = df2.loc[(df2["Year"] == year) & (df2["Sex"] == sex)]
    subdf = df2.loc[(df2["Year"] == year) & (df2["Sport"] == sport) & (df2["Sex"] == sex)]
    return subdf.shape[0] / comp.shape[0]