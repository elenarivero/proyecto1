import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        # vamos a pintar imágenes
        rx.image(src="favicon.ico"),
        rx.link(f"{datetime.date.today().year} PÁGINA DE ELENA RIVERO",
                 href="http://localhost:3000",
                 is_external=True),
        align="center"
        
    )