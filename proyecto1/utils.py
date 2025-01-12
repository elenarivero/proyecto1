import reflex as rx

# Common

# Función para devovler el idioma de la página
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

# Index
index_title = "Título de la página principal"
index_description = "Descripción de la página principal"
index_meta = [
    {"name": "og:title", "content":index_title},
    {"name": "og:description", "content":index_description}, 
]

# Cursos
course_title = "Cursos"
course_description = "Cursos sobre distintos lenguajes de programación"

courses_meta = [
    {"name": "og:title", "content":course_title},
    {"name": "og:description", "content":course_description}, 
]