import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

class MyPlotLib:
    def histogram(self, data, features):
        df = data.drop_duplicates(["ID"])
        df = df[features]
        df.hist()
        plt.show()
    def density(self, data, features):
        df = data.drop_duplicates(["ID"])
        df = df[features]
        df.plot.kde()
        plt.show()
    def pair_plot(self, data, features):
        df = data.drop_duplicates(["ID"])
        df = df[features]
        sns.pairplot(df)
        plt.show()
    def box_plot(self, data, features):
        df = data.drop_duplicates(["ID"])
        df = df[features]
        df.boxplot()
        plt.show()