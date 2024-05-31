###################################################################
import os
import subprocess

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown

from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, BorderDecoration




######################  Startup ########################
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')
    subprocess.Popen([home])
########################################################

mod = "mod4"
terminal = "kitty"
#terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
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

    # Move to the next group (workspace)
    Key([mod], "Right", lazy.screen.next_group(), desc="Move to the next group"),
    # Move to the previous group (workspace)
    Key([mod], "Left", lazy.screen.prev_group(), desc="Move to the previous group"),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
   
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),            # close window
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window",),

    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # shutdown with path to Rofi custom
    #Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),        #default
    Key([mod, "control"], "q", lazy.spawn(".config/rofi/Customtheme/powermenu/powermenu.sh"), desc="powermenu"),    #UI shutdown
## custom apps
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),     # launch Rofi
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "d", lazy.spawn("Thunar"), desc="Launch Thunar"),

    

]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

# workspace 
groups = [Group(i) for i in "12345"]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

#set workspace to a symbol
@hook.subscribe.setgroup
def setgroup():
    for i in range(0, 5):
        qtile.groups[i].label = ""    #occupied
    qtile.current_group.label = ""    #current

##--------------------------------------
##        Scratchpads & Keys
##--------------------------------------

groups.append(ScratchPad("quickpad", [
            DropDown("term", "kitty", x=0.23, y=0.25, width=0.5, lenth=0.3, on_focus_lost_hide=True),
]))

keys.extend([
        Key([mod, "control"], "Return", lazy.group['quickpad'].dropdown_toggle('term'))
])
    
###################################

layouts = [
    layout.MonadTall(border_focus="#00FFFF", border_normal="#236363", border_width=3, margin=10),
    layout.Columns(border_focus_stack=["#00FFFF", "#f0f0f0"], border_width=3, margin=10),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(border_width=5, margin=10),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#################   BAR  ##############################
#ProFontIIxNerdFont-Regular

# topbar default settings
widget_defaults = dict(
    font="ProFontIIxNerdFont",
    foreground="#00FFFF",
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()

############################################
screens = [
    ## Bar 1
    Screen(
        wallpaper='/home/trevor/Documents/backgrounds/wallpaper2.png',    #sets wallpaper
        wallpaper_mode='fill',                                            #sets fill mode
        
        top=bar.Bar(
            [

                widget.TextBox(width=20),            # add space

                widget.TextBox(
                        width=8,
                        decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF',        # border color
                            line_width=2,                 # border width
                            radius=13,                    # corner
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ], 
                ),

                widget.CurrentLayoutIcon(
                        use_mask=True,
                        forground='#00FFFF',
                        scale=0.7,
                        decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF', 
                            line_width=2, 
                            radius=13, 
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ],                
                ),

                

                # needs: python-psutil
                widget.CPUGraph(
                       # type='box',
                        graph_color='#F801E8',
                        frequency=0.15,
                        
                        decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF',        # border color
                            line_width=2,                 # border width
                            radius=13,                    # corner
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ],
                ),

                widget.Memory(
                        format='󰍛{MemUsed: .0f}{mm}',
                        update_interval=1,
                        decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF',        # border color
                            line_width=2,                 # border width
                            radius=13,                    # corner
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ],
                ),

                widget.Net(
                        format='| {down:.0f}{down_suffix}',
                        decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF',        # border color
                            line_width=2,                 # border width
                            radius=13,                    # corner
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ],
                ),
               
                #widget.WindowName(max_chars=10),        #text out put of curent window
                #widget.Prompt(),            # default app launcher-for backup
                
                #center group widget with text padding
                widget.TextBox(" ", width=bar.STRETCH, align="center"),

                widget.GroupBox(
                        active = "#00FFFF",        #all that have stuff
                        inactive = "#ffffff",
                       # block_highlight_text_color = "#00FFFF",
                       # urgent_text = color
                        highlight_method = "text",
                        active_highlight_color = "#ffffff",
                        urgent_alert_method = "text",
                        urgent_border = "#F801E8",
                        this_current_screen_border = "#00FFFF",        # colors text of current
                       # this_screen_border = "#00FFFF",
                       # other_current_screen_border = "#00FFFF",
                       # other_screen_border = "00FFFF",
                       # foreground = "#00FFFF",
                       # background = "#00FFFF",                      # the whole background

                      decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF', 
                            line_width=2, 
                            radius=13, 
                            filled=True, 
                            padding_y=0
                            ),                    
                        ],
                ),

                widget.TextBox(" ", width=bar.STRETCH),
                
                

                widget.Chord(
                    chords_colors={
                        "launch": ("#00FFFF", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                #widget.StatusNotifier(),
                widget.Systray(),

                widget.Bluetooth(
                       
                ),

                widget.Volume(
                      #fmt = '  {}',
                       emoji = True,
                       emoji_list = [' ', ' ', ' ', ' '],  
                       foreground='#F801E8',                       # icons for volume
                       padding = 5,
                       mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},  # Left-click to open volume control
                       decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF', 
                            line_width=2, 
                            radius=13, 
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ],
                       
               ),

               #needs lib: sudo pacman -S python-iwlib 
               widget.WiFiIcon(
                        padding_y=7,
                        
                        active_colour='#D1E2EA', 
                        background='#F801E8', 
                        foreground='#00FFFF', 
                        inactive_colour='#236363', 
                        decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF', 
                            line_width=2, 
                            radius=13, 
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ], 
               ),
                
                
                widget.TextBox("|",
                        decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF', 
                            line_width=2, 
                            radius=13, 
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ],                
                ),
                
                widget.Clock(format="%a %I:%M%p %m/%d", foreground="#00FFFF",
                        decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF',        # border color
                            line_width=2,                 # border width
                            radius=13,                    # corner
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ],                         
                
                ),
               
                #write text with click run script
                widget.TextBox(text=" ⏻ ", foreground="#F801E8", 
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("sh .config/rofi/Customtheme/powermenu/powermenu.sh")},
                            decorations=[
                            RectDecoration(colour='#14111f',
                            extrawidth=5,                 # add width/spacing to right
                            line_colour='#00FFFF',        # border color
                            line_width=2,                 # border width
                            radius=13,                    # corner
                            filled=True, 
                            padding_y=0,
                            group=True
                            ),                    
                        ],  
                ),
                
                
                
                #widget.QuickExit(), #default logout
            ],
           
            size=30,                     # bar height
            border_width=[0, 0, 0, 0],   # Draw top and bottom borders
            background='#00000000',        # bar background color  #14111f
            
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),


    ),

]
##############################################################

####################    Window rules   ###########################
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []          # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

floating_layout = layout.Floating(
         border_focus='#F801E8',
      #  border_normal ='#00FFFF',
         border_width = 3,

    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry

       # Match(title="Thunar"),      #file manager
        Match(title="Qalculate!"),  #calulator
    ]
)
#########################################
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
