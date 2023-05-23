"""
Password generator with DearPyGui
"""
# TODO: force parameters for warranted symbols

import dearpygui.dearpygui as dpg
import pyperclip
from constants import TAG_AZ, TAG_AZ_UPPER, TAG_NUM, TAG_SYMBOL, TAG_LENGTH, TAG_PASSWORD, DEFAULT_LENGTH
from generate_random_password import generate_random_password


def copy_password_and_exit(sender, app_data):
    """
    Get generated password from label of button and put on clipboard; exit
    """
    pyperclip.copy(dpg.get_item_label(TAG_PASSWORD))
    dpg.stop_dearpygui()


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
