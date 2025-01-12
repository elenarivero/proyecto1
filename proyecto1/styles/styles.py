import reflex as rx

from enum import Enum
from .colors import *

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
    "background_color" : Color.BACKGROUND,
    rx.button: {
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding": Size.SMALL,
        "border_radius": Size.DEFAULT,
        "color" : TextColor.HEADER,
        "background_color" : Color.CONTENT,
        "_hover" : {
            "background_color" :Color.SECONDARY
        }     
    },

    rx.link: {
        "text_decoration": "none"
    }
}

button_title_style = dict(
    font_size=Size.DEFAULT,
    color = TextColor.HEADER
)

button_body_style = dict(
    font_size=Size.MEDIUM,
    color = TextColor.BODY
)

title_style = dict(
    size ="1",
    width="100%",
    padding_top = Size.DEFAULT,
    color = TextColor.HEADER
)