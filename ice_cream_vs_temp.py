import plotly.express as px
import csv

with open("./data/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
      df = csv.DictReader(csv_file)
      print(df)
      fig = px.scatter(df,x="Temperature", y="Ice-cream Sales")
      fig.show()
