import reflex as rx
from proyecto1.components.navbar import navbar
from proyecto1.styles.styles import *
from proyecto1.views.header.header import header
from proyecto1.views.links.links import links
from proyecto1.views.footer.footer import footer
from proyecto1.utils import *
from proyecto1.routes import Ruta

@rx.page(
    route=Ruta.COURSES.value,
    title = course_title,
    description=course_description
)

def courses()-> rx.Component:
    return rx.box(
            lang(),
            navbar(),
            rx.center(
                rx.vstack(        
                header(),
                links(),                
                max_width=MAX_WIDTH,
                width="100%",
                align="center",
                margin_y=Size.BIG
                )
            ),            
            footer()
        )
