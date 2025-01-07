import reflex as rx
from proyecto1.styles.styles import *

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style = title_style
    )