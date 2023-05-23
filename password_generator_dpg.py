"""
Password generator with DearPyGui
"""
import string
import secrets
import dearpygui.dearpygui as dpg
import pyperclip

TAG_LENGTH = "length"
TAG_AZ = "az"
TAG_AZ_UPPER = "AZ"
TAG_NUM = "0..9"
TAG_SYMBOL = "@#$%"
TAG_PASSWORD = "password"

DEFAULT_LENGTH = 8


def copy_password_and_exit(sender, app_data):
    """
    Get generated password from label of button and put on clipboard; exit
    """
    pyperclip.copy(dpg.get_item_label(TAG_PASSWORD))
    dpg.stop_dearpygui()


def generate_random_password(length: int = DEFAULT_LENGTH, az: bool = True, az_upper: bool = True, num: bool = True,
                             symbol: bool = True) -> str:
    """
    :param length: length of password
    :param az: use lowercase letters - not used, always True
    :param az_upper: use uppercase letters
    :param num: use numbers
    :param symbol: use symbols
    :return: random password
    """
    alphabet = string.ascii_lowercase + \
               (string.ascii_uppercase if az_upper else "") + \
               (string.digits if num else "") + \
               (string.punctuation if symbol else "")

    return ''.join(secrets.choice(alphabet) for i in range(length))


def modify_form(sender, app_data):
    """
    call to generate password with form's parameters;
    put result into form for visualisation
    """
    random_password = generate_random_password(length=dpg.get_value(TAG_LENGTH), az=dpg.get_value(TAG_AZ),
                                               az_upper=dpg.get_value(TAG_AZ_UPPER), num=dpg.get_value(TAG_NUM),
                                               symbol=dpg.get_value(TAG_SYMBOL))
    dpg.set_item_label(TAG_PASSWORD, random_password)


dpg.create_context()
dpg.create_viewport(title='Random password generator', width=430, height=100, min_height=100, x_pos=-50)

with dpg.window(tag="primary_window"):
    with dpg.group(horizontal=True):
        dpg.add_checkbox(label="a-z", default_value=True, tag=TAG_AZ, enabled=False, callback=modify_form)
        with dpg.tooltip(dpg.last_item()):
            dpg.add_text("Not enabled")
        dpg.add_checkbox(label="A-Z", default_value=True, tag=TAG_AZ_UPPER, callback=modify_form)
        dpg.add_checkbox(label="0-9", default_value=True, tag=TAG_NUM, callback=modify_form)
        dpg.add_checkbox(label="@#$%", default_value=True, tag=TAG_SYMBOL, callback=modify_form)

        dpg.add_text("Length: ")
        dpg.add_slider_int(min_value=4, max_value=30, default_value=DEFAULT_LENGTH, width=100, tag=TAG_LENGTH,
                           callback=modify_form)

    with dpg.group(horizontal=True):
        dpg.add_button(label=generate_random_password(), width=-1,
                       tag=TAG_PASSWORD, callback=copy_password_and_exit)
        with dpg.tooltip(dpg.last_item()):
            dpg.add_text("Copy to clipboard and exit")

dpg.set_primary_window("primary_window",  True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
