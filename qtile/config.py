# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage

import os
import re
import socket
import subprocess
import json
from libqtile import hook
from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from pathlib import Path
from libqtile.log_utils import logger

from qtile_extras import widget
    
mod = "mod4"
terminal = guess_terminal()
home = str(Path.home())

# pywal colors
colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
Color0=(colordict['colors']['color0'])
Color1=(colordict['colors']['color1'])
Color2=(colordict['colors']['color2'])
Color3=(colordict['colors']['color3'])
Color4=(colordict['colors']['color4'])
Color5=(colordict['colors']['color5'])
Color6=(colordict['colors']['color6'])
Color7=(colordict['colors']['color7'])
Color8=(colordict['colors']['color8'])
Color9=(colordict['colors']['color9'])
Color10=(colordict['colors']['color10'])
Color11=(colordict['colors']['color11'])
Color12=(colordict['colors']['color12'])
Color13=(colordict['colors']['color13'])
Color14=(colordict['colors']['color14'])
Color15=(colordict['colors']['color15'])

keys = [
    # windows navigation
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # windows movement and resize
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # layout
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # general
    Key([mod], "q", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "Delete", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "w", lazy.spawn(f"wal -q -i {home}/wallpapers/"), desc="Update Theme and Wallpaper"),
    Key([mod], "a", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    Key([mod], "m", lazy.spawn(f"{home}/.config/qtile/scripts/powermenu.sh"), desc="Show power menu"),

    # F keys
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+")),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-")) ,
    Key([mod], "XF86AudioMute", lazy.spawn("amixer sset Master toggle"))
]

groups = [Group(i, layout='monadtall') for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layout_theme = {
    "border_width": 1,
    "margin": 1,
    "border_focus": Color3,
    "border_normal": Color11,
}

layouts = [
    layout.Columns(**layout_theme),
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Spiral(**layout_theme),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd",
    fontsize=12,
    padding=4,
    foreground = Color7,
    background = Color3
)

extension_defaults = widget_defaults.copy()

widgets=[
    widget.CurrentLayoutIcon(
        **widget_defaults,
    ),
    widget.GroupBox(
        **widget_defaults,
        border = '3465F7',
        borderwidth = 1,
        highlight_method = 'line',
        hide_unused = True,
        block_highlight_text_color = Color5,
        highlight_color = [Color7, Color7]
    ),
    widget.Sep(
        **widget_defaults
    ),
    widget.Prompt(
        **widget_defaults,
    ),
    widget.WindowTabs(
        **widget_defaults,
    ),
    widget.Spacer(
        **widget_defaults,
    ),
    widget.Volume(
        **widget_defaults,
        fmt = 'Vol: {}'
    ),
    widget.WiFiIcon(
        **widget_defaults,
        active_colour = Color7
    ),
    widget.Sep(
        **widget_defaults
    ),
    widget.Clock(
        **widget_defaults,
        format='%m/%d/%Y %a %I:%M %p'
    ),
    widget.UPowerWidget(
        **widget_defaults,
        percentage_low = 0.3,
        percentage_critical = 0.15,
        border_colour = Color7,
        border_charge_colour = '00cc00',
        fill_charge = '00cc00',
        fill_normal = Color7
    ),
    widget.Sep(
        **widget_defaults
    ),
    widget.Memory(
        **widget_defaults,
        measure_mem='G'
    ),
    widget.Sep(),
    widget.QuickExit(
        **widget_defaults,
        default_text='[X]'
    )
]

screens = [
    Screen(
        top=bar.Bar(
            widgets,
            24,
        ),
    ),
]

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
    **layout_theme,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None


# HOOK startup
@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/autostart.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])

