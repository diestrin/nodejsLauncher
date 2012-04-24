import commands, re
import sublime, sublime_plugin

class nodeLauncher(sublime_plugin.TextCommand):
  def run(self, edit):
    self.save()
    self.launch(edit)

  def save(self):
    self.view.run_command("save")

  def launch(self, edit):
    regx = re.compile(" ")
    log = commands.getoutput("node " +
      regx.sub("\ ", self.view.file_name()))

    #if len(html) > 0:
    #  self.view.replace(edit, sublime.Region(0, self.view.size()), html.decode('utf-8'))
    #  sublime.set_timeout(self.save, 100)