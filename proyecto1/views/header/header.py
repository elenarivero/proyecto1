import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback = "ER", size="5", radius="full"),
            rx.vstack(
                rx.text("@elenarivero"),
                rx.text("HOLA, MI NOMBRE ES ELENA RIVERO", margin_top="0px !important"),
                spacing="0"
            )
        ),
        align_items="start"
    )