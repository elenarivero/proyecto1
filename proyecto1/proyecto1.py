import reflex as rx
from proyecto1.components.navbar import navbar
from proyecto1.styles.styles import *
from proyecto1.views.header.header import header
from proyecto1.views.links.links import links
from proyecto1.views.footer.footer import footer

class State(rx.State):
    pass

def index()-> rx.Component:
    return rx.box(
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



app = rx.App(style=BASE_STYLE)
app.add_page(index)
app._compile()