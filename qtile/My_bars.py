import random
from enum import Enum
from typing import List  # noqa: F401
from libqtile.config import Screen
from libqtile import widget, bar
from libqtile.lazy import lazy


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
        # make_layout_window_name(rand_layout_window)[1],
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
        # widget.CurrentLayoutIcon(),
        # widget.DebugInfo(fontsize=12),
        # widget.CurrentLayoutIcon(),
        make_layout_window_name(rand_layout_window)[0],
        widget.Spacer(),
        # widgetgg.TextBox(text="    "),
        # make_layout_window_name(rand_layout_window)[1],
        make_infos(rand_info)[0],
        widget.TextBox(text="    "),
        make_infos(rand_info)[1],
        widget.TextBox(text="    "),
        make_infos(rand_info)[2],
        widget.TextBox(text="    "),
        make_infos(rand_info)[3],
        # widget.TextBox(text="    "),
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
        )
    )


def decode_colour(i_colour, i_available_colours):
    t_decode = i_available_colours[i_colour]
    if t_decode == "a":  # gray
        return "#141414"
    elif t_decode == "w":  # white
        return "#FFFFFF"
    elif t_decode == "l":  # light_gray
        return "#848484"
    elif t_decode == "r":  # red
        return "#E35374"
    elif t_decode == "g":  # green
        return "#98C379"
    elif t_decode == "y":  # yellow
        return "#F0C674"
    elif t_decode == "b":  # blue
        return "#61AFEF"
    elif t_decode == "p":  # purple(-ish)
        return "#C678DD"
    elif t_decode == "c":  # cyan
        return "#56B6BC"


def make_screens():
    return [
        Screen(
            top=bar.Bar(
                make_bar_screen1(),
                20,
                background="#2e2e2e",
                opacity=0.80,
            ),
        ),
        Screen(
            top=bar.Bar(
                make_bar_screen2(),
                20,
                background="#2e2e2e",
                opacity=0.80,
            ),
        )
    ]


