import webapp2
import jinja2
import os
from model import Character
from model import User
from google.appengine.api import users
from google.appengine.ext import ndb

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
<<<<<<< HEAD
            for i in characters:
                character.append('<img src="%s">' % i.image_url)
                character.append('<p class="chartext" id="charline1">%s</p><br>' % i.name)
                character.append('<p class="chartext" id="charline2">Wiki Link: %s</p><br>' % i.wiki_link)
                character.append('<p class="chartext" id="charline3">Moves: %s, %s, %s</p></div>' % (i.up_b,i.side_b,i.down_b))
        character_dict = {'character':"".join(character)}
=======
        character_dict = {'characters':characters}
>>>>>>> 7ca4da3afe6cfb51e998a9e2c004a565d15ef6dc
        self.response.write(prefs_template.render(character_dict))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_environment.get_template('templates/about.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = jinja_environment.get_template('templates/login.html')
        user = users.get_current_user()
        user_query = User.query()
        user_fetch = user_query.fetch()
        print(user_fetch)
        if user:
            email_address = user.nickname()
            signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
            for i in user_fetch:
                if(str(i.email_address)==email_address):
                    previous_user = True
                    now_user = i
                    break
                else:
                    previous_user = False
            if previous_user:
                text = "Welcome %s %s (%s)!<form action='/home'><button>Go to Site</button><br> %s <br></form><br>" % (now_user.first_name,now_user.last_name,email_address,signout_link_html)
            else:
                text = "Welcome to our site, %s!  Please sign up! <br><form method='post'><input type='text' name='first_name'><input type='text' name='last_name'><input type='submit'></form><br> %s <br>" % (email_address, signout_link_html)
        else:
            text = "Please log in to use our site! <br><a href='%s'>Sign in</a>" % (users.create_login_url('/'))
        text_dict = {'text':text}
        self.response.write(login_template.render(text_dict))
    def post(self):
        user = users.get_current_user()
        email_address = user.nickname()
        first_name = self.request.get("first_name")
        last_name = self.request.get("last_name")
        new_user = User(email_address=email_address,first_name=first_name,last_name=last_name)
        new_user.put()
        self.redirect('/home')

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        profile_template = jinja_environment.get_template('templates/profile.html')
        user = users.get_current_user()
        email_address = user.nickname()
        user_query = User.query()
        user_fetch = user_query.fetch()
        signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
        line1 = ""
        line2 = ""
        line3 = ""
        if user:
            for i in user_fetch:
                if(i.email_address==email_address):
                    now_user = i
            line1 = "Welcome to your profile page!"
            line2 = "Your name: " + now_user.first_name + " " + now_user.last_name
            line3 = "Your email address: " + now_user.email_address
        else:
            line1 = "Sorry, please log in to continue."
        lines_dict = {'line1':line1,'line2':line2,'line3':line3}
        self.response.write(profile_template.render(lines_dict))


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/home',HomePage),
    ('/prefs', PreferencePage),
    ('/abt', AboutPage),
    ('/profile',ProfilePage)
], debug=True)
