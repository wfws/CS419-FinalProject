import webapp2
from jinja2 import Environment, PackageLoader
#from django.http import HttpResponse
#import jinja2
#code adapted from CS496 week 2 lectures 
	
#from jinja2 documentation
env = Environment(loader=PackageLoader('main', 'templates'))

template_variables = {} 

def render(self, template, template_variables={}):
    template = env.get_template(template)
    self.response.write(template.render(template_variables))


	
class MainPage(webapp2.RequestHandler):
		
	def get(self): 
		render(self, 'index.html')
		return