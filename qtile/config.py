from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger
import colors
import screeninfo

@lazy.function
def spawn_dmenu(qtile, command):
    gap = 6
    menu_width = qtile.current_screen.width - 2 * gap
    qtile.spawn("%s -x %s -y %s -z %s"%(command, gap, gap, menu_width))

groups = []
group_map = {}

num_groups_per_monitor = 9
def generate_groups():
    """
    Generate the group map used for translating between group identifiers
    of different screen.
    """
    num_screens = len(screeninfo.get_monitors())

    global groups
    global group_map

    # Initialize the group_map dictionary with an empty list for each screen
    for screen in range(num_screens):
        group_map[screen] = []

    # Counter to give each group a unique name (across all screens)
    running_group_index = 1
    # we go by group and not by screen first so that second screen
    # spawns on screen2.group1 and not screen1.group2
    for group in range(1, num_groups_per_monitor + 1):
        for screen in range(num_screens):
            g = Group(name=str(running_group_index), label=str(group))
            groups.append(g)
            group_map[screen].append(str(running_group_index))
            running_group_index += 1

@lazy.window.function
def window_to_other_screen(window):
    s = window.qtile.current_screen.index
    if s == 0:
        window.toscreen(1)
    if s == 1:
        window.toscreen(0)



@lazy.function
def switch_group(qtile, group_num):
    """
    Switch to group of current screen.
    """
    group_name = group_map[qtile.current_screen.index][group_num]
    qtile.groups_map[group_name].toscreen()

@lazy.window.function
def move_window_to_group(window, group_num, switch_group=False):
    """
    Move window to group of current screen and switch to group if switch_group
    flag is set.
    """
    group_name = group_map[window.qtile.current_screen.index][group_num]
    window.togroup(group_name, switch_group=switch_group)

mod = "mod4"
FF_path = "/home/nld/.config/firefox/firefox"
keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.next()),
    Key([mod], "k", lazy.layout.previous()),
    Key([mod, "control"], "return", lazy.next_screen()),

    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "space", lazy.layout.normalize()),

    # TODO custom function without redifinition
    # MonadTall Layout
    Key([mod, "control"], "h", lazy.layout.shrink_main()),
    Key([mod, "control"], "l", lazy.layout.grow_main()),


    # Change window state
    Key( [mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "g", lazy.window.toggle_floating()),

    Key([mod, "shift"], "r", lazy.reload_config()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "c", lazy.window.kill()),

    # Launch apps
    Key([mod], "a", lazy.spawn("feh --bg-scale /home/nld/Documents/Pictures/wallpaper/images --randomize --no-fehbg")),
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "r", lazy.spawn("/home/nld/.config/rofi/launchers/colorful/launcher.sh")),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),
    Key([mod, "shift"], "d", lazy.spawn("discord")),
    Key([mod, "shift"], "e", lazy.spawn("pcmanfm")),
    Key([mod], "p", spawn_dmenu("dmenu_run")),
    Key([mod, "shift"], "p", spawn_dmenu("passmenu")),

    KeyChord([mod], "d",
        [
            Key([mod], "Return", lazy.spawn(FF_path + " --new-window")),
            Key([mod], "y", lazy.spawn(FF_path + " --new-window https://youtube.com")),
            Key([mod], "i", lazy.spawn(FF_path + " --new-window https://ilias3.uni-stuttgart.de")),
            Key([], "Return", lazy.spawn(FF_path + " --new-tab")),
            Key([], "y", lazy.spawn(FF_path + " --new-tab https://youtube.com")),
            Key([], "i", lazy.spawn(FF_path + " --new-tab https://ilias3.uni-stuttgart.de")),
        ]
    ),
]

generate_groups()

for i in range(num_groups_per_monitor):
    keys.append(Key([mod], str(i + 1), switch_group(i)))
    keys.append(Key([mod, "shift"], str(i + 1), move_window_to_group(i, switch_group=False)))

keys.append(Key([mod, "shift"], "Return", window_to_other_screen()))

# Scratchpads
scratchpads = ((1, "newsboat"), (2, "ranger"), (3, "zsh"), (4, "zsh"), (5, "zsh"), (6, "zsh"), (7, "zsh"), (8, "zsh"), (9, "ncspot"), (10, "zsh"), (11, "zsh"), (12, "python"))
groups.extend(
    [
        ScratchPad(
            "scratchpad%s"%pad, [
                DropDown("term", "alacritty --title scratchpad%s -e %s"%(pad, program), on_focus_lost_hide=False)
            ], single=False
        ) for pad, program in scratchpads
    ]
)
keys.extend([Key([mod], "F%s"%i, lazy.group["scratchpad%s"%i].dropdown_toggle("term")) for i in range(1, 13)])

layouts = [
    layout.MonadTall(
        border_width=2, border_focus=colors.light1, border_normal=colors.dark0_hard,
        margin=12, margin_on_single=12,
        grow_amount = 5, ratio=0.55,
        min_secondary_size = 100
    ),
    layout.MonadThreeCol(
        border_width=2, border_focus=colors.light1, border_normal=colors.dark0_hard,
        margin=12, margin_on_single=12,
        grow_amount = 5, ratio=0.55,
        new_client_position="bottom"
    ),
]

widget_defaults = dict(
    font="ZedMonoNerdFont-ExtraBold",
    fontsize=12,
    padding=3,
    foreground=colors.light1
)

extension_defaults = widget_defaults.copy()

battery_widget = widget.Battery()
clock_widget = widget.Clock(format="%d, %H:%M:%S, %s")
cpu_widget = widget.CPU(
    format="\uf4bc   {load_percent}"
)
layout_widget = widget.CurrentLayout(icon_first=True)
ram_widget = widget.Memory(format="\uefc5   {MemUsed:.1f}", measure_mem="G")
network_widget = widget.Net(format="\uf1eb    {total:.0f} {total_suffix}", use_bits=True)
arch_widget = widget.TextBox("\uf303 ")
thermal_widget = widget.ThermalSensor(format="\ue20a {temp:.1f}", foreground_alert=colors.light1)

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    hide_unused=True,
                    visible_groups=group_map[i],
                    highlight_method="block",
                    active=colors.light1,
                    block_highlight_text_color=colors.dark0_hard,
                    rounded=False,
                    this_current_screen_border=colors.light1,
                    this_screen_border=colors.light1
                ),
                widget.Spacer(),
                network_widget,
                widget.Sep(),
                ram_widget,
                widget.Sep(),
                cpu_widget,
                widget.Sep(),
                thermal_widget,
                widget.Sep(),
                clock_widget,
                widget.Sep(),
                arch_widget
            ],
            19,
            background = colors.dark0_hard,
            margin = [6, 6, 0, 6]
        ),
    ) for i in range(len(screeninfo.get_monitors()))
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="pinentry-gtk"),  # gitk
    ],
    border_focus=colors.light1,
    border_normal=colors.dark0_hard,
    border_width=2
)

auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"
