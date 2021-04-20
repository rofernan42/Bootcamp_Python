def HowManyMedals(df, name):
    subdf = df[["Name", "Year", "Medal"]]
    subdf = subdf.loc[(subdf["Name"] == name)]
    res = {}
    for i, row in subdf.iterrows():
        if row["Year"] not in res.keys():
            res[row["Year"]] = {"G": 0, "S": 0, "B": 0}
        if row["Medal"] == "Gold":
            res[row["Year"]]["G"] += 1
        if row["Medal"] == "Silver":
            res[row["Year"]]["S"] += 1
        if row["Medal"] == "Bronze":
            res[row["Year"]]["B"] += 1
    return res