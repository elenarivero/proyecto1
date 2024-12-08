import reflex as rx
from proyecto1.components.navbar import navbar
from proyecto1.views.header.header import header
from proyecto1.views.links.links import links
from proyecto1.views.footer.footer import footer

class State(rx.State):
    pass

def index()-> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
        width="100%",
        align="center",
        justify="center"
    )


app = rx.App()
app.add_page(index)
app._compile()