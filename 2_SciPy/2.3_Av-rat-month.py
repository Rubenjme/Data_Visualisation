# pip install juspy
# https://quasar.dev/style/typography  
# https://www.highcharts.com/docs/index

import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv("Data/reviews.csv", parse_dates=["Timestamp"]) # Cargo el dataset en la variable data, que será un DataFrame de pandas.
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")              # Creo una nueva columna en el DataFrame que se llamará Month y que contendrá la fecha de la columna Timestamp
month_average = data.groupby(["Month"])["Rating"].mean() # Agrupo los datos por la columna Month y realizo la media de los valores que hay en la columna Rating

# Código conseguido de: https://www.highcharts.com/docs/chart-and-series-types/spline-chart
chart_def =  """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Month'
    },
    subtitle: {
        text: 'Average ratings by month left for all courses'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y:.2f}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Análisis de reseñas de los cursos", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="Estos párrafos representan el análisis de las reseñas del curso")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.tittle.text = "Average rating by Month"


    hc.options.xAxis.categories = list(month_average.index)
    hc.options.series[0].data = list(month_average.values)
    
    return wp

jp.justpy(app)

