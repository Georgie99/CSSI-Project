import webapp2
import jinja2
import os
from model import Character
from model import User
from google.appengine.api import users


jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = False)

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
            characters = character_query.filter(Character.skill==int(skill),Character.color==color,Character.strength>5).order(-Character.strength).fetch()
        else:
            characters = character_query.filter(Character.skill==int(skill),Character.color==color,Character.speed>5).order(-Character.speed).fetch()
        prefs_template = jinja_environment.get_template('templates/prefs.html')
        character = []
        for i in characters:
            character.append('<img src="%s"><br>' % i.image_url)
            character.append('<p>%s</p><br>' % i.name)
            character.append('<p>Wiki Link: %s</p><br>' % i.wiki_link)
            character.append('<p>Special Moves: %s, %s, %s</p><br>' % (i.up_b,i.side_b,i.down_b))
        if(character==[]):
            character.append('Sorry, we don\'t have exactly what you\'re looking for, but try these similar characters!')
            if(pref=="strength"):
                characters = character_query.filter(Character.skill==int(skill),Character.strength>5).order(-Character.strength).fetch()
            else:
                characters = character_query.filter(Character.skill==int(skill),Character.speed>5).order(-Character.speed).fetch()
            for i in characters:
                character.append('<br><img id="image" src="%s">' % i.image_url)
                character.append('<p class="text">%s</p><br>' % i.name)
                character.append('<p class="text">Wiki Link: %s</p><br>' % i.wiki_link)
                character.append('<p class="text">Moves: %s, %s, %s</p><br>' % (i.up_b,i.side_b,i.down_b))
        character_dict = {'character':"".join(character)}
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
