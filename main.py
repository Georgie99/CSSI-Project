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
        mario = Character(strength=2,skill=3,speed=8,name="Mario",wiki_link="no")
        mario.put()
        skill = self.request.get("skill")
        pref = self.request.get("pref")
        color = self.request.get("color")
        character_query = Character.query()
        if(skill=="beginner"):
            characters = character_query.filter(Character.skill==3).fetch()
        elif(skill=="medium"):
            characters = character_query.filter(Character.skill==2).fetch()
        else:
            characters = character_query.filter(Character.skill==1).fetch()
        if(pref=="strength"):
            characters = character_query.filter(Character.strength>5).fetch()
        else:
            characters = character_query.filter(Character.speed>5).fetch()
        prefs_template = jinja_environment.get_template('templates/prefs.html')
        character_dict = {'character':characters}
        self.response.write(prefs_template.render(character_dict))

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/prefs', PreferencePage)
], debug=True)
