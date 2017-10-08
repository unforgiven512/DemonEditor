import gi
from ftplib import FTP

from main.properties import get_config, write_config
from main.eparser.lamedb import parse

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

__status_bar = None
__options = get_config()
__services_model = None


def on_about_app(item):
    builder = Gtk.Builder()
    builder.add_from_file("editor_ui.glade")
    dialog = builder.get_object("about_dialog")
    dialog.run()
    dialog.destroy()


def get_handlers():
    return {
        "on_close_main_window": Gtk.main_quit,
        "on_about_app": on_about_app,
        "on_preferences": on_preferences,
        "on_download": on_download,
        "on_upload": on_upload,
        "on_data_dir_field_icon_press": on_path_open,
        "on_data_open": on_data_open,
        "on_tree_view_key_release": on_tree_view_key_release
    }


def on_data_open(item):
    if isinstance(item, Gtk.ListStore):
        channels = parse(get_config()["data_dir_path"] + "lamedb_example")
        for ch in channels:
            item.append(ch)
        # item.append()


def on_path_open(*args):
    builder = Gtk.Builder()
    builder.add_from_file("editor_ui.glade")
    dialog = builder.get_object("path_chooser_dialog")
    response = dialog.run()
    if response == -12:  # for fix assertion 'gtk_widget_get_can_default (widget)' failed
        args[0].set_text(dialog.get_filename())
    dialog.destroy()


def on_preferences(item):
    builder = Gtk.Builder()
    builder.add_from_file("editor_ui.glade")
    builder.connect_signals(get_handlers())
    dialog = builder.get_object("settings_dialog")
    host_field = builder.get_object("host_field")
    host_field.set_text(__options["host"])
    port_field = builder.get_object("port_field")
    port_field.set_text(__options["port"])
    login_field = builder.get_object("login_field")
    login_field.set_text(__options["user"])
    password_field = builder.get_object("password_field")
    password_field.set_text(__options["password"])
    services_field = builder.get_object("services_field")
    services_field.set_text(__options["services_path"])
    user_bouquet_field = builder.get_object("user_bouquet_field")
    user_bouquet_field.set_text(__options["user_bouquet_path"])
    satellites_xml_field = builder.get_object("satellites_xml_field")
    satellites_xml_field.set_text(__options["satellites_xml_path"])
    data_dir_field = builder.get_object("data_dir_field")
    data_dir_field.set_text(__options["data_dir_path"])

    if dialog.run() == Gtk.ResponseType.OK:
        __options["host"] = host_field.get_text()
        __options["port"] = port_field.get_text()
        __options["user"] = login_field.get_text()
        __options["password"] = password_field.get_text()
        __options["services_path"] = services_field.get_text()
        __options["user_bouquet_path"] = user_bouquet_field.get_text()
        __options["satellites_xml_path"] = satellites_xml_field.get_text()
        __options["data_dir_path"] = data_dir_field.get_text()
        write_config(__options)
    dialog.destroy()


def on_tree_view_key_release(widget, event):
    key = event.keyval
    if key == Gdk.KEY_Tab:
        print("Tab")
    if key == Gdk.KEY_Delete:
        print("Delete")
    if key == Gdk.KEY_Up:
        print("Up")
    if key == Gdk.KEY_Down:
        print("Down")

    print(widget.get_name())


def on_upload(item):
    connect(__options, False)


def on_download(item):
    connect(__options)


def connect(properties, download=True):
    assert isinstance(properties, dict)
    try:
        with FTP(properties["host"]) as ftp:
            ftp.login(user=properties["user"], passwd=properties["password"])
            if download:
                __status_bar.push(1, ftp.voidcmd("NOOP"))
                ftp.cwd(properties["services_path"])
                ftp.retrlines("LIST")
            else:
                pass
    except Exception as e:
        __status_bar.remove_all(1)
        __status_bar.push(1, getattr(e, "message", repr(e)))  # Or maybe so: getattr(e, 'message', str(e))


def init_ui():
    builder = Gtk.Builder()
    builder.add_from_file("editor_ui.glade")
    main_window = builder.get_object("main_window")
    global __status_bar
    __status_bar = builder.get_object("status_bar")
    builder.connect_signals(get_handlers())
    main_window.show_all()


def start_app():
    init_ui()
    Gtk.main()


def close_app():
    Gtk.main_quit()


if __name__ == "__main__":
    start_app()
