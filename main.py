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
        skill = self.request.get("skill")
        pref = self.request.get("pref")
        color = self.request.get("color")
        character_query = Character.query()
        if(pref=="strength"):
            characters = character_query.filter(Character.skill==int(skill)).filter(Character.color==color).filter(Character.strength>5).fetch(3)
        else:
            characters = character_query.filter(Character.skill==int(skill)).filter(Character.color==color).filter(Character.speed>5).fetch(3)
        prefs_template = jinja_environment.get_template('templates/prefs.html')
        character = ""
        for i in characters:
            character = character + "\n" + i.name
        character_dict = {'character':character}
        self.response.write(prefs_template.render(character_dict))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_environment.get_template('templates/about.html')
        self.response.write(home_template.render())

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/prefs', PreferencePage),
    ('/abt', AboutPage)
], debug=True)
