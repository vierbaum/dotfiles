import random
from typing import List  # noqa: F401
import libqtile.core.manager as manager
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen, KeyChord
from libqtile.lazy import lazy

# --- VARIABLES --- #

mod = "mod4"
terminal = "alacritty"

# --- LAYOUTS --- #

layouts = [
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

floating_layout = layout.floating.Floating(
    auto_float_types=(
        'Albert',
        'Conky',
        'JetBrains Toolbox',
    ),
)

# --- KEYS ---#

keys = [

    ##########
    # Layout #
    ##########

    # Next layout
    Key([mod], "Tab", lazy.next_layout()),

    # Change window floating state
    Key([mod], "g", lazy.window.toggle_floating()),

    # Change window fullscreen state
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # Increase window size
    Key([mod], "i", lazy.layout.grow()),

    # Decrese window size
    Key([mod], "m", lazy.layout.shrink()),

    ##########
    # Window #
    ##########

    # Kill window
    Key([mod, "shift"], "c", lazy.window.kill()),

    #########
    # Qtile #
    #########

    # Restart Qtile
    Key([mod], "q", lazy.restart(), desc="Restart Qtile"),

    # Turn bar on / off

    #########
    # Emacs #
    #########

    # Spawn Emacs
    KeyChord([mod], "e", [
        Key([], "Return", lazy.spawn("emacsclient -c -a ''")),
    ]),

    ############
    # Terminal #
    ############

    # Spawn terminal
    Key([mod], "Return", lazy.spawn("alacritty")),

    # Spawn tmux
    Key([mod, "shift"], "Return", lazy.spawn("alacritty -e tmux")),

    # Spawn nautilus
    Key([mod, "shift"], "e", lazy.spawn("nautilus")),

    # Spawn discord
    Key([mod, "shift"], "d", lazy.spawn("discord")),

    # Spawn flameshot
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),

    # Launching a terminal
    Key([mod], "p", lazy.spawncmd()),

    ###########
    # Firefox #
    ###########

    KeyChord([mod], "d", [
        Key([], "Return", lazy.spawn("firefox")),
        Key([], "y", lazy.spawn("firefox --new-tab https://youtube.com")),
        Key([], "t", lazy.spawn("firefox --new-tab https://twitter.com")),
        Key([], "r", lazy.spawn("firefox --new-tab https://reddit.com")),
        Key([], "a", lazy.spawn("firefox --new-tab https://wiki.archlinux.org")),
        Key([], "m", lazy.spawn("firefox --new-tab https://moodle.pfarrwiesen.de")),

        Key([mod], "y", lazy.spawn("firefox --new-window https://youtube.com")),
        Key([mod], "t", lazy.spawn("firefox --new-window https://twitter.com")),
        Key([mod], "r", lazy.spawn("firefox --new-window https://reddit.com")),
        Key([mod], "a", lazy.spawn("firefox --new-window https://wiki.archlinux.org")),
        Key([mod], "m", lazy.spawn("firefox --new-window https://moodle.pfarrwiesen.de")),
    ]),

    ###########
    # Windows #
    ###########

    # Move windows
    KeyChord([mod], "w", [
        Key([], "h", lazy.layout.shuffle_left()),
        Key([], "j", lazy.layout.shuffle_down()),
        Key([], "k", lazy.layout.shuffle_up()),
        Key([], "l", lazy.layout.shuffle_right()),
    ]),

    # Move window focus

    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),
]

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

# --- BARS --- #

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
                27,
                background="#2e2e2e",
                opacity=0.80,
            ),
        ),
        Screen(
            top=bar.Bar(
                make_bar_screen2(),
                27,
                background="#2e2e2e",
                opacity=0.80,
            ),
        )
    ]

screens = make_screens()

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
