
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from typing import List  # noqa: F401
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import TextBox

mod = "mod4"
terminal = "alacritty"
browser = "brave"

colors = {
    'bg':           '#202020',
    'fg':           '#dfdfdf',
    'dark-red':     '#ea7171',
    'red':          '#ed8682',
    'dark-green':   '#96a171',
    'green':        '#b1d094',
    'dark-yellow':  '#e7a55f',
    'yellow':       '#ecb983',
    'dark-blue':    '#7196a1',
    'blue':         '#9fb8bf',
    'dark-magenta': '#c28490',
    'magenta':      '#d7adb5',
    'dark-cyan':    '#80ab96',
    'cyan':         '#9fbfaf',
    'dark-gray':    '#3d3d3d',
    'gray':         '#666666',
}

keys = [
    # Aplication spawn
    Key([mod], "Return", lazy.spawn(terminal)),  # Launches Alacritty
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod], "p", lazy.spawn("pcmanfm")),
    Key([mod], "a", lazy.spawn("xfce4-appfinder")),
    Key([mod], "x", lazy.spawn("arcolinux-logout")),
    Key([mod, "shift"], "d", lazy.spawn("rofi -show drun")),

    # SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),

    # SUPER + SHIFT KEYS

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),

    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

]

groups = [
    Group('1', label='一', matches=[Match(wm_class=[browser])]),
    Group('2', label='二', matches=[Match(wm_class=['gimp'])]),
    Group('3', label='三', matches=[Match(wm_class=['nemo'])]),
    Group('4', label='四', matches=[Match(wm_class=['zoom',
                                                   'discord',
                                                   'telegram-desktop',
                                                   'slack'])]),
    Group('5', label='五'),
    Group('6', label='六'),
    Group('7', label='七'),
    Group('8', label='八'),
    Group('9', label='九'),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width": 1,
                "margin": 10,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Tile(**layout_theme),
    layout.TreeTab(**layout_theme),
    layout.Floating(**layout_theme)
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    background=colors['bg'],
    foreground=colors['fg']
)

extension_defaults = widget_defaults.copy()


def lower_left_triangle(bg_color, fg_color):
    return TextBox(
        text='\ue0be',
        padding=0,
        fontsize=22,
        background=bg_color,
        foreground=fg_color)


def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=22,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=22,
        background=bg_color,
        foreground=fg_color)


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text='',  # arch logo
                    fontsize=22,
                    padding=10,
                    background=colors['dark-red'],
                    foreground=colors['fg']),
                widget.TextBox(
                    text='\ue0be',
                    padding=0,
                    fontsize=22,
                    foreground=colors['bg']),

                # display groups
                widget.GroupBox(
                    active=colors['fg'],
                    inactive=colors['dark-gray'],
                    disable_drag=True,
                    borderwidth=0,
                    margin_x=0,
                    padding_x=10,
                    highlight_method='line',
                    block_highlight_text_color=colors['red'],
                    highlight_color=colors['bg']),

                right_arrow(colors['dark-yellow'], colors['bg']),
                # display the current wm layout
                widget.CurrentLayout(
                    background=colors['dark-yellow'],
                    fmt='[{}]',
                    padding=10),

                right_arrow(colors['yellow'], colors['dark-yellow']),
                widget.WindowCount(
                    background=colors['yellow'],
                    padding=5,
                    fmt=' {}'),
                right_arrow(colors['bg'], colors['yellow']),
                widget.WindowName(
                    foreground=colors['cyan'],
                    padding=10),

                left_arrow(colors['bg'], colors['dark-blue']),
                # display total available updates
                widget.CheckUpdates(
                    distro="Arch_checkupdates",
                    margin=30,
                    padding=10,
                    colour_have_updates=colors['cyan'],
                    colour_no_updates=colors['fg'],
                    no_update_string='No updates',
                    display_format='累 {updates} updates',
                    background=colors['dark-blue'],
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')}),

                left_arrow(colors['dark-blue'], colors['blue']),
                # display memory usage
                widget.Memory(
                    background=colors['blue'],
                    padding=10,
                    measure_mem='G',
                    format=' {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')}),

                left_arrow(colors['blue'], colors['dark-magenta']),
                # display cpu usage
                widget.CPU(
                    background=colors['dark-magenta'],
                    padding=10,
                    format=' {freq_current}GHz {load_percent}%'),

                left_arrow(colors['dark-magenta'], colors['dark-cyan']),
                widget.PulseVolume(
                    background=colors['dark-cyan'],
                    fmt=' {}',
                    padding=10,
                    volume_app='pavucontrol'),

                left_arrow(colors['dark-cyan'], colors['cyan']),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    background=colors['cyan'],
                    padding=10),

                left_arrow(colors['cyan'], colors['dark-cyan']),
                widget.Systray(
                    background=colors['dark-cyan'],
                    padding=10),

                widget.Spacer(
                    length=50,
                    background=colors['dark-cyan']
                ),

                left_arrow(colors['dark-cyan'], colors['green']),
                widget.QuickExit(
                    background=colors['green'],
                    foreground=colors['bg'],
                    default_text='',
                    fontsize=17,
                )
            ],
            size=24,
            margin=5,
            background=colors['bg'],
            wallpaper='wall.jpg'
        ),
    ),
]

# Drag floating layouts.
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
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])



# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"