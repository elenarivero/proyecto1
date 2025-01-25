import reflex as rx
from proyecto1.styles.styles import *

def link_button(title: str, body:str, url: str, is_external=True)-> rx.Component:
    return rx.button(        
        rx.link(
            rx.hstack(
                rx.icon(tag="arrow-right"),            
                rx.vstack(
                    rx.text(title, style=button_title_style),
                    rx.text(body, style=button_body_style)
                ) 
            ),
                          
            href=url, is_external=is_external),
        id = title,
        width="100%" 
    )