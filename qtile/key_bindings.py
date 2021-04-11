from typing import List  # noqa: F401

from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

mod = "mod4"
terminal = "alacritty"

bindings = [

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
        
        Key([mod], "y", lazy.spawn("firefox --new-window https://youtube.com")),
        Key([mod], "t", lazy.spawn("firefox --new-window https://twitter.com")),
        Key([mod], "r", lazy.spawn("firefox --new-window https://reddit.com")),
        Key([mod], "a", lazy.spawn("firefox --new-window https://wiki.archlinux.org")),
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
