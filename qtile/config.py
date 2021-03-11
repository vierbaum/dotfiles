from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

import My_bars
import My_layouts
import key_bindings

#############
# Variables #
#############
color_gray = "#141414"
color_white = "#FFFFFF"
color_light_gray = "#848484"
color_red = "#E35374"
color_green = "#98C379"
color_yellow = "#F0C674"
color_blue = "61AFEF"
color_purple = "#C678DD"
color_cyan = "#56B6BC"

mod = "mod4"
terminal = "alacritty"

########
# Keys #
########
keys = key_bindings.bindings

##############
# Workspaces #
##############
groups = [
    Group("Α"),
    Group("Β"),
    Group("Γ"),
    Group("Δ"),
    Group("Ε"),
    Group("Ζ"),
    Group("Η"),
    Group("Θ"),
    Group("Ι"),
]

for k, group in zip(["1", "2", "3", "4", "5", "6", "7", "8", "9"], groups):
    keys.append(Key([mod], k, lazy.group[group.name].toscreen()))  # Send current window to another group
    keys.append(Key([mod, "shift"], k, lazy.window.togroup(group.name)))

###########
# Layouts #
###########
layouts = My_layouts.layout
floating_layout = layout.floating.Floating(
    auto_float_types=(
        'Albert',
        'Conky',
        'JetBrains Toolbox',
        'Emacs',
    ),
)

#######################
# Whatever widget is? #
#######################
widget_defaults = dict(
    background="#141414",
    foreground="#FFFFFF",
    font="SF Pro Text Regular",
    fontsize=12,
    padding=1,
)
extension_defaults = widget_defaults.copy()

########
# Bars #
########
screens = [
    Screen(
        top=bar.Bar(
            My_bars.make_bar_screen1(),
            27,
            background="#2e2e2e",
            opacity=0.50,
        ),
    ),
    Screen(
        top=bar.Bar(
            My_bars.make_bar_screen2(),
            27,
            background="#2e2e2e",
            opacity=0.50,
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
