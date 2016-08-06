import sublime, sublime_plugin, re, string

class WebifyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				print('1', s)
				news = s.replace('<', '&lt;')
				news = news.replace('>', '&gt;')
				print('2', news)	
				self.view.replace(edit, region, news)

class UnwebifyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				print('1', s)
				news = s.replace('&lt;', '<')
				news = news.replace('&gt;', '>')
				print('2', news)	
				self.view.replace(edit, region, news)