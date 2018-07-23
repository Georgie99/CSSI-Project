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
        if(color=="red"):
            characters = character_query.filter(Character.color=="red").fetch()
        elif(color=="black"):
            characters = character_query.filter(Character.color=="black").fetch()
        elif(color=="orange"):
            characters = character_query.filter(Character.color=="orange").fetch()
        elif(color=="yellow"):
            characters = character_query.filter(Character.color=="yellow").fetch()
        elif(color=="green"):
            characters = character_query.filter(Character.color=="green").fetch()
        elif(color=="blue"):
            characters = character_query.filter(Character.color=="blue").fetch()
        elif(color=="pink"):
            characters = character_query.filter(Character.color=="pink").fetch()
        prefs_template = jinja_environment.get_template('templates/prefs.html')
        character_dict = {'character':characters}
        self.response.write(prefs_template.render(character_dict))
        # mario = Character(name="Mario",speed=8,strength=9,color="red",wiki_link="no")


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/prefs', PreferencePage)
], debug=True)
