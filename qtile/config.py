
from libqtile import bar, layout, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, EzKey
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import ImageDecoration, PowerLineDecoration 

import os
import subprocess

from colors import color


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home)


mod = "mod4"
alt = "mod1"
terminal = "alacritty"
# terminal = guess_terminal()

keys = [
    # Switch between windows
    Key(
        [mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),
    Key(
        [mod], "l", 
        lazy.layout.right(), 
        desc="Move focus to right"
    ),
    Key(
        [mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"
    ),
    Key(
        [mod], "k", 
        lazy.layout.up(), 
        desc="Move focus up"
    ),
    Key(
        [mod], "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
    ),

    # Logging out
    Key(
        [mod, "shift"],  "r", 
        lazy.restart()
    ),

    # Move windows
    Key(
        [mod, "shift"], "h", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"
    ),
    Key(
        [mod, "shift"], "l", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
    ),
    Key(
        [mod, "shift"], "j", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
    ),
    Key(
        [mod, "shift"], "k", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
    ),

    # Grow windows
    Key(
        [mod, "control"], "h", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
    ),
    Key([
        mod, "control"], "l", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
    ),
    Key(
        [mod, "control"], "j", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),
    Key(
        [mod, "control"], "k", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),

    
    Key(
        [mod, "shift"], "space", 
        lazy.layout.flip()
    ),
    Key(
        [mod], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ),
    #Key([mod, "shift"], "n", lazy.layout.normalize()),
    # Key([mod], "p", lazy.layout.maximize()),
    #Key([mod, "shift"], "s", lazy.layout.toggle_auto_maximize()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        [mod], "Return", lazy.spawn(terminal), 
        desc="Launch terminal"
    ),
    # Toggle between different layouts as defined below
    Key(
        [mod], "Tab", lazy.next_layout(), 
        desc="Toggle between layouts"
    ),
    Key(
        [mod], "c", lazy.window.kill(), 
        desc="Kill focused window"
    ),
    Key(
        [mod],"f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod], "t", 
        lazy.window.toggle_floating(), 
        desc="Toggle floating on the focused window"
    ),
    Key(
        [mod], "o", 
        lazy.spawncmd()
    ),
    Key(
        [alt], "r", 
        lazy.reload_config(), 
        desc="Reload the config"
    ),
    Key(
        [mod, "control"], "q", lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),

    # Hardware keys

    # Volume
    Key([], "XF86AudioRaiseVolume", "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    Key([], "XF86AudioLowerVolume", "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    Key([], "XF86AudioMute", "pactl set-sink-volume @DEFAULT_SINK@ toggle"),
    # Key([], "XF86AudioNext", ""),
    # Key([], "XF86AudioPrev", ""),

    # Brightness
    Key([], "XF86MonBrightnessUp", "brightnessctl set +5%"),
    Key([], "XF86MonBrightnessDown", "brightnessctl set 5%-"),
]

# GROUPS
group_names = "𝕬 𝕭 𝕮 𝕯 𝕰 𝕱 𝕲".split()
# group_names = "A B C D E F G".split()
groups = [Group(name) for name in group_names]
for i, name in enumerate(group_names, 1):
    idx = str(i)
    keys += [
        Key([mod], idx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], idx, lazy.window.togroup(name))]


# LAYOUTS

layout_default_config = {
    "border_focus": color['blue'], 
    "border_normal": color['maroon'],
    "border_width": 4,
    "margin": 4,

} 

layouts = [
    layout.Columns(**layout_default_config),
    layout.Max(**layout_default_config),
    layout.MonadTall(**layout_default_config),
    # layout.MonadWide(**layout_default_config),
    # layout.RatioTile(**layout_default_config),
    layout.TreeTab(**layout_default_config),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


powerline_arrow_left = {
    "decorations": [
        PowerLineDecoration(
            size=12,
            )
    ]
}

powerline_arrow_right = {
    "decorations": [
        PowerLineDecoration(
            path='arrow_right',
            padding_x=10,
            size=12
            )
    ]
}

powerline_rounded_left = {
    "decorations": [
        PowerLineDecoration(
            path='rounded_left',
            size=12,
            )
    ]
}

powerline_rounded_right = {
    "decorations": [
        PowerLineDecoration(
            path='rounded_right',
            size=10,
            )
    ]
}

image_decor = {
    "decorations": [
        ImageDecoration(
            image=os.path.expanduser('~/Downloads/wallpapersden.com_windows-10-4k-abstract-layer_1920x1080.jpg'),
            whole_bar=True
        ),
    ]
}


widget_defaults = dict(
    # font="Jetbrains Mono Nerd Font",
    font='Routed Gothic', # URW Bookman L # Darkcastle PERSONAL USE
    foreground=color['fg'],
    fontsize=20,
    padding=4
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(" ⚚", background=color['darkgray'], foreground=color['fg'], fontsize=28, width=47, margin_x=4, margin_y=2, padding=5), #550000 maroon
                widget.GroupBox( 
                    background=color['gray'],
                    block_highlight_text_color=color['white'],
                    borderwidth=3,
                    disable_drag=True,
                    # foreground=color['white'],
                    # group highlighting
                    highlight_method='line',
                    # gradient
                    highlight_color=[color['dark'], color['darkgray']],
                    # margins
                    margin_x=1,
                    # margin_y=2,
                    # padding
                    padding_x=8,
                    # padding_y=10,
                    rounded=False,
                    # text coloring
                    active=color['green'], 
                    inactive=color['darkgray'],
                    this_current_screen_border=color['red'],
                    **powerline_arrow_left,
                    ),
                widget.Sep(
                    linewidth=0,
                    background=color['bg'],
                    # padding=15,
                    **powerline_rounded_left
                    ),
                # widget.Sep(
                #     linewidth=0,
                #     background=color['white'],
                #     # padding=10,
                #     **powerline_arrow_right
                #     ),
                widget.Prompt(),
                widget.WindowName(font='Routed Gothic', width=350, max_chars=35),
                # widget.Systray(),
                widget.Spacer(bar.STRETCH), # LEFT background="#FFFF00"
                widget.Clock(
                    format="%a %-d %-I:%-M %p", 
                    font="Routed Gothic",
                    ), # JetBrainsMono Nerd Font Mono
                # widget.Spacer(bar.STRETCH), # RIGHT background="#964B00"
                widget.Spacer(bar.STRETCH, background=color['bg'], **powerline_arrow_right),
                # widget.Spacer(bar.STRETCH, background="#FF0000"), # RIGHT
                # widget.LaunchBar(), 
                # widget.Net(interface='wlp61s0', font='sans'), 
                widget.CheckUpdates(
                    font='Darkcastle PERSONAL USE', # Jetbrains Mono Nerd Font
                    background=color['blue'],
                    colour_have_updates=color['black'],
                    colour_no_updates=color['black'],
                    display_format='Updates: y',
                    no_update_string='Updates: n',
                    distro='Arch',
                    # execute="alacritty", # can exec some script
                    # foreground=color['red'],
                    **powerline_arrow_right,
                    ),
                widget.CurrentLayout(foreground=color['bg'], background=color['green'], font='Darkcastle PERSONAL USE'),
                widget.CurrentLayoutIcon(custom_icon_paths=os.path.expanduser('~/.config/qtile/icons'), font='sans', padding=10, background=color['green']),
                # widget.Battery(font='sans'),
                widget.CPUGraph(graph_color=color['yellow'], fill_color=color['yellow'], border_width=3, margin_x=12, margin_y=4, background=color['darkgray']),
                # widget.HDDBusyGraph(graph_color=color['magenta'], fill_color=color['magenta'], border_width=3, margin_x=12, margin_y=4),
                widget.MemoryGraph(graph_color=color['green'], fill_color=color['green'], border_width=3, margin_x=12, margin_y=4, background=color['darkgray']),
                widget.NetGraph(graph_color=color['blue'], fill_color=color['blue'], border_width=3, margin_x=12, margin_y=4, frequency=0.5, background=color['darkgray'], **powerline_rounded_right),
                # widget.PulseVolume(),
                widget.Volume(background=color['dark'], font='sans', emoji=True), 
                widget.Battery(background=color['dark'], format='BT: {percent:2.0%}'),
                # widget.OpenWeather(font='sans', location='Philadelphia', format='{location_city}: {icon}'),
                # widget.Wlan(font='sans', interface='wlan0'), # not displaying
                # widget.Systray(),
                # widget.Pomodoro(),
            ],
            34,
            background=color['bg'],
            margin=[5,4,2,4],
            border_width=[0, 0, 4, 0],
            border_color=["000000", "000000", color['darkgray'], "000000"], #550000 maroon
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod], 
        "Button1", 
        lazy.window.set_position_floating(), 
        start=lazy.window.get_position()
    ),
    Drag(
        [mod], 
        "Button3", 
        lazy.window.set_size_floating(), 
        start=lazy.window.get_size()
    ),
    Click(
        [mod], 
        "Button2", 
        lazy.window.bring_to_front()
    ),
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
wl_xcursor_theme = None
wl_xcursor_size = 24

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
