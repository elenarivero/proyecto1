import reflex as rx

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
        bg = "blue",
        # marcamos un padding en el eje x
        padding_x = "16px",
        # marcamos un padding en el eje y
        padding_y = "8px",
        # le ponemos una prioridad alta para que siempre esté visible
        z_index = "999"
    )