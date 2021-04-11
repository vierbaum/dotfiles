from typing import List  # noqa: F401
from typing import List  # noqa: F401
from typing import List  # noqa: F401

from libqtile import layout

layout = [
    layout.MonadTall(
        border_focus_stack='#d75f5f',
        border_width=1,
        border_focus="#61AFEF",
        border_normal="#010B3D",
        fullscreen_border_width=0,
        margin=12,
    ),
    layout.Matrix(
        border_focus_stack='#d75f5f',
        border_width=1,
        border_focus="#61AFEF",
        border_normal="#010B3D",
        fullscreen_border_width=0,
        margin=6,
    ),
    layout.Columns(
        border_focus_stack='#d75f5f',
        border_width=1,
        border_focus="#61AFEF",
        border_normal="#010B3D",
        fullscreen_border_width=0,
        margin=6,
    ),

]
