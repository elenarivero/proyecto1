import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback = "ER", size="3", radius="full"),
        rx.text("@elenarivero"),
        rx.text("HOLA, MI NOMBRE ES ELENA RIVERO"),
        align="center"
    )