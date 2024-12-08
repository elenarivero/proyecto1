import reflex as rx

def link_button(text: str, url: str)-> rx.Component:
    return rx.link(
        rx.button(rx.icon("tally-1", stroke_width=2.5),
                  text),
        href=url,
        is_external=True
    )