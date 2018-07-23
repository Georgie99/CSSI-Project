import webapp2
import jinja2
import os
from model import Character
from model import User
from google.appengine.api import users


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

class LoginPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
          email_address = user.nickname()
          cssi_user = User.get_by_id(user.user_id())
          signout_link_html = '<a href="%s">sign out</a>' % (
              users.create_logout_url('/'))
          if cssi_user:
            self.response.write('''
                Welcome %s %s (%s)!<form action="/">
                <button>Go to Bank</button>
                 <br> %s <br>
                </form><br>''' % (
                  cssi_user.first_name,
                  cssi_user.last_name,
                  email_address,
                  signout_link_html))
          else:
            self.response.write('''
                Welcome to our site, %s!  Please sign up! <br>
                <form method="get" action="/bank">
                <input type="text" name="first_name">
                <input type="text" name="last_name">
                <input type="submit">
                </form><br> %s <br>
                ''' % (email_address, signout_link_html))
        else:
          self.response.write('''
            Please log in to use our site! <br>
            <a href="%s">Sign in</a>''' % (
              users.create_login_url('/')))

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/prefs', PreferencePage),
    ('/abt', AboutPage),
    ('/login', LoginPage)
], debug=True)
