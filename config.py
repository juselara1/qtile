from juselara_qtile.keys import KeyManager, GroupManager, MouseManager
from juselara_qtile.dataclasses import PathsConfig
from juselara_qtile.generals import (
        load_groups, load_layouts, load_widget_defaults, create_screens,
        load_float_layouts
        )
from yacmmal.load.toml import TOMLLoader
from yacmmal import BaseModel

class Config(BaseModel):
    paths: PathsConfig

cfg = (
        TOMLLoader(base_path="/home/juselara/.config/qtile")
        .add_path("conf", "paths", PathsConfig)
        .extract()
        )
def load_managers(cfg: Config):
    groups = load_groups(cfg.paths.keys)
    managers = dict(
        groups = groups,
        groupmanager = GroupManager(cfg.paths.keys, groups),
        keymanager = KeyManager(cfg.paths.keys),
        mousemanager = MouseManager(cfg.paths.keys)
        )
    return managers

managers = load_managers(cfg)
layouts = load_layouts(cfg.paths)
floating_layout = load_float_layouts(cfg.paths)
screens = create_screens(cfg.paths)
widget_defaults = load_widget_defaults(cfg.paths)
extension_defaults = widget_defaults.copy()
groups = managers["groups"]
keys = managers["groupmanager"]() + managers["keymanager"]()
mouse = managers["mousemanager"]()

mod = "mod4"
terminal = "kitty"
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
