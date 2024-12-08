import reflex as rx
from proyecto1.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "https://www.twitch.tv/"),
        link_button("YouTube", "https://www.youtube.com/"),
        link_button("Discord", "https://discord.com/"),
        align="center"
    )