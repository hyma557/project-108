import plotly.figure_factory as ff
import pandas as pd 
import csv

df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["AvgRating"].tolist()], ["ar"], show_hist = True)
fig.show()
