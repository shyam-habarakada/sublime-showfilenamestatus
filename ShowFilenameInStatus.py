import sublime, sublime_plugin, os

class ShowFilenameInStatus(sublime_plugin.EventListener):
	def on_activated_async(self, view):
	    filename = os.path.split(view.file_name())[1]
	    if filename is None:
	        view.erase_status('_filename')
	    else:
	        view.set_status('_filename', "File: " + filename)
