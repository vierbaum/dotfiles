import ctypes
import random
from enum import Enum
from typing import List  # noqa: F401

from libqtile import widget

color_gray = "#141414"
color_white = "#FFFFFF"
color_light_gray = "#848484"
color_red = "#E35374"
color_green = "#98C379"
color_yellow = "#F0C674"
color_blue = "61AFEF"
color_purple = "#C678DD"
color_cyan = "#56B6BC"


class Colour(Enum):
    gray = id(color_gray)  # a
    white = id(color_white)  # w
    light_gray = id(color_light_gray)  # l
    red = id(color_red)  # r
    green = id(color_green)  # g
    yellow = id(color_yellow)  # y
    blue = id(color_blue)  # b
    purple = id(color_purple)  # p
    cyan = id(color_cyan)  # c


def make_bar_screen2():
    rand_pic = random.randint(0, 1)
    rand_groups = populate_array(5, 5)
    rand_layout_window = populate_array(5, 2)
    rand_info = populate_array(5, 4)
    return [
        make_image(rand_pic),
        widget.Prompt(foreground="#ff8c00", font='SF Pro Text Semibold'),
        make_groups(rand_groups),
        widget.TextBox(text="    "),
        make_layout_window_name(rand_layout_window)[0],
        widget.TextBox(text="    "),
        #make_layout_window_name(rand_layout_window)[1],
        widget.Spacer(),
        widget.TextBox(text="    "),
        make_infos(rand_info)[0],
        widget.TextBox(text="    "),
        make_infos(rand_info)[1],
        widget.TextBox(text="    "),
        make_infos(rand_info)[2],
        widget.TextBox(text="    "),
        make_infos(rand_info)[3],
        widget.Notify(foreground="#ff8c00", font='SF Pro Text Semibold'),
    ]


def make_bar_screen1():
    rand_pic = random.randint(0, 1)
    rand_groups = populate_array(5, 5)
    rand_layout_window = populate_array(5, 2)
    rand_info = populate_array(5, 4)
    return [
        make_image(rand_pic),
        widget.Prompt(foreground="#ff8c00", font='SF Pro Text Semibold'),
        make_groups(rand_groups),
        widget.TextBox(text="    "),
        #widget.CurrentLayoutIcon(),
        #widget.DebugInfo(fontsize=12),
        #widget.CurrentLayoutIcon(),
        make_layout_window_name(rand_layout_window)[0],
        widget.Spacer(),
        #widget.TextBox(text="    "),
        #make_layout_window_name(rand_layout_window)[1],
        make_infos(rand_info)[0],
        widget.TextBox(text="    "),
        make_infos(rand_info)[1],
        widget.TextBox(text="    "),
        make_infos(rand_info)[2],
        widget.TextBox(text="    "),
        make_infos(rand_info)[3],
        #widget.TextBox(text="    "),
        widget.Notify(foreground="#ff8c00", font='SF Pro Text Semibold'),
        widget.Systray(),
        widget.Cmus(fontsize=12,
        font="SF Pro Text Semibold",
        ),
    ]


def populate_array(n_option, n_out):
    out = []
    while len(out) != n_out:
        temp_rand = random.randint(0, n_option)
        if temp_rand not in out:
            out.append(temp_rand)
    return out


def make_image(inp):
    path = ""
    if inp == 0:
        path = "~/.config/qtile/parch_b.png"
    elif inp == 1:
        path = "~/.config/qtile/download.png"
    return widget.Image(scale=True, filename=path)


def make_sep():
    return widget.Sep(linewidth=1,
                      padding=10,
                      size_percent=75,
                      ),


def make_groups(inp):
    p_1 = decode_colour(inp[0], "rgbypc")
    p_2 = decode_colour(inp[1], "rgbypc")
    p_3 = decode_colour(inp[2], "rgbypc")
    p_4 = decode_colour(inp[3], "rgbypc")
    p_5 = decode_colour(inp[4], "rgbypc")
    return widget.GroupBox(
        font="SF Pro Text Semibold",
        padding=0,
        active=p_1,
        inactive=p_2,
        margin=2,
        highlight_method='text',
        this_current_screen_border=p_3,
        urgent_alert_method='text',
        urgent_border=p_4,
        urgent_text=p_5,
        disable_drag=True,
        invert_mouse_wheel=True
    )


def make_layout_window_name(inp):
    p_1 = decode_colour(inp[0], "rgbypc")
    p_2 = decode_colour(inp[1], "rgbypc")
    return (
        widget.CurrentLayout(
            font="SF Pro Text Semibold",
            foreground=p_1
        ),
        widget.WindowName(foreground=p_2,
                          font="SF Pro Text Semibold"
                          )
    )


def make_infos(inp):
    p_1 = decode_colour(inp[0], "rgbypc")
    p_2 = decode_colour(inp[1], "rgbypc")
    p_3 = decode_colour(inp[2], "rgbypc")
    p_4 = decode_colour(inp[3], "rgbypc")
    return (
        widget.CPU(
            foreground=p_1,
            format='{load_percent}%',
            update_interval=1.0,
            font="SF Pro Text Semibold",
        ),
        widget.Memory(
            foreground=p_2,
            format='{MemUsed} MB',
            font="SF Pro Text Semibold",
        ),
        widget.ThermalSensor(
            foreground=p_3,
            threshold=80,
            font="SF Pro Text Semibold",
        ),
        widget.Clock(
            format='  %a %d.%m.20%y  %H:%M:%S ',
            font="SF Pro Text Semibold",
            foreground=p_4,
            # timezone="Europe/London",
        )
    )


def decode_colour(i_colour, i_available_colours):
    t_decode = i_available_colours[i_colour]
    if t_decode == "a":
        return str(ctypes.cast(Colour.gray.value, ctypes.py_object).value)
    elif t_decode == "w":
        return str(ctypes.cast(Colour.white.value, ctypes.py_object).value)
    elif t_decode == "l":
        return str(ctypes.cast(Colour.light_gray.value, ctypes.py_object).value)
    elif t_decode == "r":
        return str(ctypes.cast(Colour.red.value, ctypes.py_object).value)
    elif t_decode == "g":
        return str(ctypes.cast(Colour.green.value, ctypes.py_object).value)
    elif t_decode == "y":
        return str(ctypes.cast(Colour.yellow.value, ctypes.py_object).value)
    elif t_decode == "b":
        return str(ctypes.cast(Colour.blue.value, ctypes.py_object).value)
    elif t_decode == "p":
        return str(ctypes.cast(Colour.purple.value, ctypes.py_object).value)
    elif t_decode == "c":
        return str(ctypes.cast(Colour.cyan.value, ctypes.py_object).value)
