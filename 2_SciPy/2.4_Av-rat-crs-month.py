# pip install juspy
# https://quasar.dev/style/typography  
# https://www.highcharts.com/docs/index

import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc

data = pd.read_csv("Data/reviews.csv", parse_dates=["Timestamp"]) # Cargo el dataset en la variable data, que será un DataFrame de pandas.
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")                # Creo una nueva columna en el DataFrame que se llamará Month y que contendrá el año y semana de la columna Timestamp
month_average_crs = data.groupby(["Month", "Course Name"])["Rating"].mean().unstack()    # Agrupo los datos por la columna Month y Nombre del curso

# Código conseguido de: https://www.highcharts.com/docs/chart-and-series-types/areaspline-chart
chart_def =  """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average rating by Month by Course'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        plotBands: [{
            from: 2020,
            to: 2023,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Rating medio de {point.x}</b><br>',
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                35971,
                36409,
                26007
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                39143,
                36829,
                49317,
                52490
            ]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Análisis de reseñas de los cursos", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="Estos párrafos representan el análisis de las reseñas del curso")
    hc = jp.HighCharts(a=wp, options=chart_def)


    hc.options.xAxis.categories = list(month_average_crs.index)
    hc.data = [{"name":v1, "data": [v2 for v2 in month_average_crs[v1].values]} for v1 in month_average_crs.columns]
    hc.options.series = hc.data

    return wp

jp.justpy(app)

