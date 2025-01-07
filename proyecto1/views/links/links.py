import reflex as rx
from proyecto1.components.link_button import link_button
from proyecto1.components.title import *

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch", "Directos de lunes a viernes", "https://www.twitch.tv/"),
        link_button("YouTube", "Tutoriales semanales", "https://www.youtube.com/"),
        link_button("Discord", "El chat de la comunidad", "https://discord.com/"),
        align="center",
        width="100%"
    )