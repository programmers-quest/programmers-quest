from quest.engine import runtime
from direct.gui import DirectGuiGlobals

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

def set_default_dialog_geom(model_path: str) -> None:
    """
    Sets the property of DirectGuiGlobals.set_default_dialog_geom with a model
    loaded from the configured model path
    """

    model_inst = runtime.loader.load_model(model_path)
    DirectGuiGlobals.set_default_dialog_geom(model_inst)

def set_default_font(font_path: str) -> None:
    """
    Sets the property of DirectGuiGlobals.set_default_font with a font
    loaded from the configured font path
    """

    font_inst = runtime.loader.load_font(font_path)
    DirectGuiGlobals.set_default_font(font_inst)

def set_default_click_sound(sound_path: str) -> None:
    """
    Sets the property of DirectGuiGlobals.set_default_click_sound with a audio
    loaded from the configured sound path
    """

    sound_inst = runtime.loader.load_sfx(sound_path)
    DirectGuiGlobals.set_default_click_sound(sound_inst)

def set_default_rollover_sound(sound_path: str) -> None:
    """
    Sets the property of DirectGuiGlobals.set_default_rollover_sound with a audio
    loaded from the configured sound path
    """

    sound_inst = runtime.loader.load_sfx(sound_path)
    DirectGuiGlobals.set_default_rollover_sound(sound_inst)

default_dialog_button_geom = None

def set_default_dialog_button_geoms(model_path: str) -> None:
    """
    Sets the default dialog button geometry model used for querying button stylings from
    """

    global default_dialog_button_geom
    default_dialog_button_geom = runtime.loader.load_model(model_path)

def get_default_dialog_button_geoms() -> object:
    """
    Returns the configured global dialog button geometry models
    """

    return default_dialog_button_geom

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------- #