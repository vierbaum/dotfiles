from typing import List  # noqa: F401

from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

import os


def change_wallpaper(a):
    def wall(a):
        os.system("feh --bg-scale ~/Documents/Pictures/wallpaper/ --randomize --no-fehbg")
    return wall

def dmenu_chars(a):
    def chars(a):
        os.system("bash ~/Documents/programming/scripts/chars.sh")
    return chars

mod = "mod4"
terminal = "alacritty"
bindings = [

    Key([mod, "shift"], "q", lazy.shutdown()),
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
        Key([], "Return", lazy.spawn("emacs")),
    ]),

    ############
    # Terminal #
    ############

    # Spawn terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Spawn nautilus
    Key([mod, "shift"], "e", lazy.spawn("nautilus")),
    Key(["mod1", "shift"], "e", lazy.spawn(terminal + " -e ranger")),

    # Spawn discord
    Key([mod, "shift"], "d", lazy.spawn("discord")),

    # Spawn flameshot
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),

    # Launching a terminal
    Key([mod], "p", lazy.spawncmd()),

    Key([mod], "r", lazy.spawn("dmenu_run")),
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

    Key([mod], "b", lazy.hide_show_bar()),
    Key([mod], "a", lazy.function(change_wallpaper(12))),


    Key([mod], "o", lazy.function(dmenu_chars(12))),
    Key([], "F12", lazy.spawn("xfce4-terminal --drop-down"))
]

#bindings.append(Key([mod], "o", lazy.function(change_wallaper)))
