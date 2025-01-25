import reflex as rx
import datetime
from proyecto1.styles.styles import *

def footer() -> rx.Component:
    return rx.vstack(
        # vamos a pintar imágenes
        rx.image(src="favicon.ico"),
        rx.link(f"{datetime.date.today().year} PÁGINA DE ELENA RIVERO",
                 href="http://localhost:3000",
                 is_external=True),
        align="center",
        width="100%",
        position="fixed",
        bottom= "0",
        #z_index="999",
        # marcamos un padding en el eje x
        padding_x = Size.DEFAULT,
        # marcamos un padding en el eje y
        padding_y = Size.SMALL,
         # ponemos un color de fondo
        bg = "lightgray",
       
        # le ponemos una prioridad alta para que siempre esté visible
        z_index = "999",
        height="100px"
    )