
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, EzKey
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

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
    Key(
        [], "XF86AudioRaiseVolume",
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    ),
    Key(
        [], "XF86AudioLowerVolume",
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    ),
    Key(
        [], "XF86AudioMute",
        "pactl set-sink-volume @DEFAULT_SINK@ toggle"
    ),
    Key(
        [], "XF86AudioNext",
        ""
    ),
    Key(
        [], "XF86AudioPrev",
        ""
    ),

    # Brightness
    Key(
        [], "XF86MonBrightnessUp",
        "brightnessctl set +5%"
    ),
    Key(
        [], "XF86MonBrightnessDown",
        "brightnessctl set 5%-"
    ),
]

# GROUPS
group_names = "𝕬 𝕭 𝕮 𝕯 𝕰 𝕱 𝕲".split()
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
    layout.MonadWide(**layout_default_config),
    layout.RatioTile(**layout_default_config),
    layout.TreeTab(**layout_default_config),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font="Jetbrains Mono Nerd Font",
    font="Darkcastle PERSONAL USE", # URW Bookman L # Darkcastle PERSONAL USE
    foreground=color['fg'],
    fontsize=20,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(" ⚚", background=color['darkgray'], foreground=color['fg'], fontsize=28, width=47, margin_x=4, margin_y=2, padding=5), #550000 maroon
                widget.GroupBox(highlight_method='line', active=color['green'], inactive=color['darkgray'], highlight_color=color['dark']),
                widget.Prompt(),
                widget.WindowName(font="Darkcastle PERSONAL USE", width=350, max_chars=30),
                widget.Systray(),
                widget.Spacer(bar.STRETCH), # LEFT background="#FFFF00"
                widget.Clock(format="%Y-%m-%d %a %I:%M %p", font="Routed Gothic"), # JetBrainsMono Nerd Font Mono
                widget.Spacer(bar.STRETCH), # RIGHT background="#964B00"
                # widget.Spacer(bar.STRETCH, background="#FF0000"), # RIGHT
                widget.CurrentLayout(),
                widget.Wlan(font='sans', interface='wlan0'), # not displaying
                # widget.Systray(),
                widget.Pomodoro(),
            ],
            34,
            background=color['black'],
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
