# pip install juspy
# https://quasar.dev/style/typography  

import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Análisis de reseñas de los cursos", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="Estos párrafos representan el análisis de las reseñas del curso")
    
    return wp

jp.justpy(app)