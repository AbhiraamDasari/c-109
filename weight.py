import csv
import pandas as pd
import plotly.figure_factory as ff

data= pd.read_csv("data.csv")

figure = ff.create_distplot([data["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
figure.show()