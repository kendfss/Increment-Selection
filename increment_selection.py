import sublime
import sublime_plugin


class IncrementSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, boost):
        boost = float(boost)
        for region in self.view.sel():
            if region.empty():
                continue
            content = self.view.substr(region)
            cast = int if content.isnumeric() else float
            try:
                number = cast(content) + boost
            except ValueError:
                continue
            self.view.replace(edit, region, str(cast(number)))
    def input(self, args):
        return IncrementDirectionHandler(self.view)

class PathChoiceHandler(sublime_plugin.TextInputHandler):
    def __init__(self, view):
        self.view = view

    def name(self):
        return "boost"

    def placeholder(self):
        return "path"

    def preview(self, text):
        return None



9
10
11