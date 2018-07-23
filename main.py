import webapp2
import jinja2
import os
from model import Character

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_environment.get_template('templates/home.html')
        self.response.write(home_template.render())

class PreferencePage(webapp2.RequestHandler):
    def get(self):
        prefs_template = jinja_environment.get_template('templates/prefs.html')
        self.response.write(prefs_template.render())
    def post(self):
        prefs_template = jinja_environment.get_template('templates/prefs.html')
        # mario = Character(name="Mario",speed=8,strength=9,color="red",wiki_link="no")


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/prefs', PreferencePage)
], debug=True)
