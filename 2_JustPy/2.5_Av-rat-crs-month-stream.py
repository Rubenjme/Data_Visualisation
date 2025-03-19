# pip install juspy
# https://quasar.dev/style/typography  
# https://www.highcharts.com/docs/index

import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
import os

script_dir = os.path.dirname(__file__)
csv_path = os.path.join(script_dir, '..', 'Data', 'reviews.csv')
data = pd.read_csv(csv_path, parse_dates=["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")                # Creo una nueva columna en el DataFrame que se llamará Month y que contendrá el año y semana de la columna Timestamp
month_average_crs = data.groupby(["Month", "Course Name"])["Rating"].mean().unstack()    # Agrupo los datos por la columna Month y Nombre del curso

# Código conseguido de: https://www.highcharts.com/docs/chart-and-series-types/stream-graph
chart_def =  """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zooming: {
            type: 'x'
        }
    },

    title: {
        floating: true,
        align: 'left',
        text: 'Average rating by Month by Course - Streamgraph'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false,
        minPadding: 0.1,
        maxPadding: 0.15
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'Lanzamiento del curso'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'Python se hizo popular'
        }, {
            point: {
                x: 24.25,
                xAxis: 0,
                y: 140,
                yAxis: 0
            },
            text: 'Russia banned from<br>the Olympic Games<br> in 2017'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            },
            accessibility: {
                exposeAsGroupOnly: true
            }
        }
    },


    series: [{
        name: 'Finland',
        data: [
            0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7,
            7, 6, 12, 7, 9, 5, 5, 6, 8
        ]
    }, {
        name: 'Austria',
        data: [
            0, 3, 4, 2, 4, 0, 0, 8, 8, 11, 6, 12, 11, 5, 6, 7, 1, 10,
            21, 9, 17, 17, 23, 16, 17, 14, 18
        ]
    }, {
        name: 'Sweden',
        data: [
            0, 2, 5, 3, 7, 0, 0, 10, 4, 10, 7, 7, 8, 4, 2, 4, 8, 6, 4,
            3, 3, 7, 14, 11, 15, 14, 18
        ]
    }, {
        name: 'Norway',
        data: [
            0, 17, 15, 10, 15, 0, 0, 10, 16, 4, 6, 15, 14, 12, 7, 10,
            9, 5, 20, 26, 25, 25, 19, 23, 26, 39, 37
        ]
    }, {
        name: 'U.S.',
        data: [
            0, 4, 6, 12, 4, 0, 0, 9, 11, 7, 10, 7, 7, 8, 10, 12, 8, 6,
            11, 13, 13, 34, 25, 37, 28, 23, 25
        ]
    },  {
        name: 'Germany',
        data: [
            0, 0, 1, 2, 6, 0, 0, 0, 7, 2, 8, 9, 0, 0, 0, 0, 0, 0, 26,
            24, 29, 36, 29, 30, 19, 31, 27
        ]
    }, {
        name: 'Netherlands',
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 9, 9, 6, 4, 0, 7, 4,
            4, 11, 8, 9, 8, 24, 20, 17
        ]
    }, {
        name: 'Italy',
        data: [
            0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 1, 4, 4, 5, 4, 2, 2, 5, 14,
            20, 10, 13, 11, 5, 8, 10, 17
        ]
    }, {
        name: 'Canada',
        data: [
            0, 1, 1, 7, 1, 0, 0, 3, 2, 3, 4, 3, 3, 1, 3, 2, 4, 5, 7,
            13, 15, 17, 24, 26, 25, 29, 26
        ]
    }, {
        name: 'Switzerland',
        data: [
            0, 3, 1, 1, 3, 0, 0, 10, 2, 6, 2, 0, 6, 10, 5, 5, 5, 15,
            3, 9, 7, 11, 14, 9, 11, 15, 15
        ]
    }, {
        name: 'Great Britain',
        data: [
            0, 4, 1, 0, 3, 0, 0, 2, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0,
            2, 1, 2, 1, 1, 4, 5, 2
        ]
    },  {
        name: 'Russia',
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            23, 18, 13, 22, 15, 33, 0, 0
        ]
    },   {
        name: 'South Korea',
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4,
            6, 6, 4, 11, 14, 8, 17, 9
        ]
    },  {
        name: 'Uzbekistan',
        data: [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0
        ]
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

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

