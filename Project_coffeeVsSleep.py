import csv
import numpy as np
import plotly_express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    coffee_in_ml = []
    sleep_in_hours = []
    with(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_file:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep_in_hours"]))

    return{"x" : coffee_in_ml, "y" :sleep_in_hours}


def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("The Correlation between maount of Coffee consumed and the Number of hours slept is :-  \n--->", correlation[0,1])


def setup():
    data_path = "D:\Python\Correlation\cups of coffee vs sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()

