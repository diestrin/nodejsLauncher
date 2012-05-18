from subprocess import Popen
import re
import sublime, sublime_plugin

p = 0

class NodelauncherCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.set_timeout(self.launch, 100)

  #def endS(self,):
  #  p.terminate()

  def launch(self):
    regx = re.compile(" ")
    cmd = "cmd.exe /K node " + regx.sub("\ ", self.view.file_name());
    p = Popen(cmd)
    #sublime_plugin.on_query_context(self, "ctrl+o+p", sublime.OP_EQUAL, endS, true)