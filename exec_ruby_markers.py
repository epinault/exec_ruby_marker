import sublime, sublime_plugin, subprocess

class ExecuteAndUpdateRubyMarkers(sublime_plugin.TextCommand):
    def run(self, edit):
        r = sublime.Region(0, self.view.size())
        text = self.view.substr(r)
        settings = self.view.settings() 

        ruby_exec = '' if settings.get('ruby_exec') == None else '/usr/bin/ruby'
        xmpfilter = '' if settings.get('xmpfilter') == None else '/usr/bin/xmpfilter'

        s = subprocess.Popen(
            [
                '/usr/bin/env',
                ruby_exec,
                xmpfilter
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        out = s.communicate(text)

        if s.returncode != None and s.returncode != 0:
            sublime.message_dialog("There was an error: " + out[1])
            return

        viewlines = self.view.full_line(r)
        outlines = out[0].split('\n')

        self.view.erase(edit, r)
        self.view.replace(edit, viewlines, out[0])
