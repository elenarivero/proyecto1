import reflex as rx

from enum import Enum

# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    SMALL = "8px",
    MEDIUM = "12px",
    DEFAULT = "16px",
    BIG = "32px"

# Styles
BASE_STYLE = {
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding": Size.SMALL,
        "border_radius": Size.DEFAULT
    },

    rx.link: {
        "text_decoration": "none"
    }
}

button_title_style = dict(
    font_size=Size.DEFAULT
)

button_body_style = dict(
    font_size=Size.MEDIUM
)

title_style = dict(
    size ="1", #no funciona
    width="100%",
    padding_top = Size.DEFAULT
)