import sublime, sublime_plugin, os

class ShowFilenameInStatus(sublime_plugin.EventListener):
    status_key = 'filename'

    def set_filename_status(self, view):
        filename = os.path.split(view.file_name())[1]
        if filename is None:
            view.erase_status(status_key)
        else:
            view.set_status(status_key, "File: " + filename)

    def on_activated(self, view):
        self.set_filename_status(view)
