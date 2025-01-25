import reflex as rx
from proyecto1.styles.colors import *

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback = "ER", size="3", radius="full"),
        rx.text("@elenarivero", color=TextColor.BODY),
        rx.text("HOLA, MI NOMBRE ES ELENA RIVERO", color=TextColor.BODY),
        align="center"
    )