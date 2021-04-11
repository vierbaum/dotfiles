from typing import List  # noqa: F401
import libqtile.core.manager as manager
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
# Bars #
########
screens = My_bars.make_screens()

def switch_bar_on_off():
    global screens
    tempfile = open("bar_status.txt", "r")
    tempvar = tempfile.readline().strip()
    tempfile.close()
    tempfile = open("bar_status.txt", "w")
    if tempvar == False:
        tempfile.write("True")
        screens = []
    else:
        tempfile.write("False")
        screens = My_bars.make_screens
    print(tempvar)
    tempfile.close()



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

    keys.append(Key(["mod1", "shift"], "1", lazy.to_screen(0)))  # Send current window to another group
    keys.append(Key(["mod1", "shift"], "2", lazy.to_screen(1)))  # Send current window to another group

    #keys.append(Key([mod], "b", switch_bar_on_off()))
###########
# Layouts #
###########
layouts = My_layouts.layout
floating_layout = layout.floating.Floating(
    auto_float_types=(
        'Albert',
        'Conky',
        'JetBrains Toolbox',
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

"""def switch_bar_on_off():
"""

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"

if __name__ == "__main__":
    #switch_bar_on_off()
    print("end")
