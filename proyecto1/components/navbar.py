import reflex as rx
from proyecto1.styles.styles import *

def navbar() -> rx.Component:
    # Como queremos colocar los componentes en horizontal utilizamos hstack
    return rx.hstack(
        # De momento sólo vamos a tener un elemento de tipo texto
        rx.text(
            # Va a aparecer de nombre principal
            "principal",
            # Le damos una altura de 40px
            height="40px"
        ),
        # position sticky significa que queda fija
        position="sticky",
        # ponemos un color de fondo
        bg = "lightgray",
        # marcamos un padding en el eje x
        padding_x = Size.DEFAULT,
        # marcamos un padding en el eje y
        padding_y = Size.SMALL,
        # le ponemos una prioridad alta para que siempre esté visible
        z_index = "999",
        top = 0
    )