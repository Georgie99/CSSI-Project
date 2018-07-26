import webapp2
import jinja2
import random
import os
from model import Character
from model import User
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = False)

class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_environment.get_template('templates/home.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = jinja_environment.get_template('templates/login.html')
        user = users.get_current_user()
        user_query = User.query()
        user_fetch = user_query.fetch()
        if user:
            email_address = user.nickname()
            signout_link_html = '<a class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect starttext" href="%s">sign out</a>' % (users.create_logout_url('/'))
            previous_user = False
            for i in user_fetch:
                if(str(i.email_address)==email_address):
                    previous_user = True
                    now_user = i
            if previous_user:
                text1 = "Welcome %s!" % (now_user.first_name)
                text2 ="<form action='/home'><button class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect starttext'>Go to Site</button><br> %s <br></form><br>" % signout_link_html
            else:
                text1 = "Welcome, %s!  Please sign up!" % (email_address)
                text2 = "<br><form method='post'><input type='text' name='first_name'><input type='text' name='last_name'><input type='submit'></form><br> %s <br>" %  (signout_link_html)
        else:
            text1 = "Welcome! Please log in!"
            text2 = "<br><a class='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect starttext' href='%s'>Sign in</a>" % (users.create_login_url('/'))
        text_dict = {'text1':text1,'text2':text2}
        self.response.write(login_template.render(text_dict))
    def post(self):
        user = users.get_current_user()
        email_address = user.nickname()
        first_name = self.request.get("first_name")
        last_name = self.request.get("last_name")
        new_user = User(email_address=email_address,first_name=first_name,last_name=last_name,saved_chars=[ndb.Key('Character',4977764016848896)])
        new_user.put()
        self.redirect('/home')

class PreferencePage(webapp2.RequestHandler):
    def get(self):
        prefs_template = jinja_environment.get_template('templates/prefs.html')
        self.response.write(prefs_template.render())
        user = users.get_current_user()
        print(user)
    def post(self):
        user = users.get_current_user()
        print(user)
        if(self.request.get("type")=="show"):
            skill = self.request.get("skill")
            pref = self.request.get("pref")
            color = self.request.get("color")
            character_query = Character.query()
            if(pref=="strength"):
                characters = character_query.filter(Character.skill==int(skill),Character.color==color,Character.strength>5).order(-Character.strength).fetch()
            else:
                characters = character_query.filter(Character.skill==int(skill),Character.color==color,Character.speed>5).order(-Character.speed).fetch()
            prefs_template = jinja_environment.get_template('templates/prefs.html')
            if(characters==[]):
                if(pref=="strength"):
                    characters = character_query.filter(Character.skill==int(skill),Character.strength>5).order(-Character.strength).fetch()
                else:
                    characters = character_query.filter(Character.skill==int(skill),Character.speed>5).order(-Character.speed).fetch()
            character_dict = {'characters':characters}
            self.response.write(prefs_template.render(character_dict))
        elif(self.request.get("type")=="addChar"):
            print(user)
            user_query = User.query()
            user_fetch = user_query.fetch()
            if user:
                for i in user_fetch:
                    email_address = user.nickname()
                    if(i.email_address==email_address):
                        now_user = i
                now_user.saved_chars.append(ndb.Key('Character',int(self.request.get("characterKey"))))
                print(self.request.get("characterKey"))
                now_user.put()
            else:
                self.response.write('''Log in first!''')
class AboutPage(webapp2.RequestHandler):
    def get(self):
        n = ''
        home_template = jinja_environment.get_template('templates/about.html')
        character_query = Character.query()
        characters= character_query.order(Character.name).fetch()
        character_dict = {'characters':characters}
        # def NameandrandomNumber(name):
        #     thing="../%s/%d.gif"%(name, random.randint(1,4))
        #     return thing
        self.response.write(home_template.render(character_dict))

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        profile_template = jinja_environment.get_template('templates/profile.html')
        user = users.get_current_user()
        print(user)
        user_query = User.query()
        user_fetch = user_query.fetch()
        signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
        line1 = ""
        line2 = ""
        line3 = ""
        if user:
            for i in user_fetch:
                email_address = user.nickname()
                if(i.email_address==email_address):
                    now_user = i
            line2 = "Welcome " + now_user.first_name + " " + now_user.last_name
            line3 = "Your email address: " + now_user.email_address
        else:
            line2 = "Sorry, please log in to continue."
            line3 = ""
        lines_dict = {'line2':line2,'line3':line3, 'line1':now_user.saved_chars}
        self.response.write(profile_template.render(lines_dict))


app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/home',HomePage),
    ('/prefs', PreferencePage),
    ('/abt', AboutPage),
    ('/profile',ProfilePage)
], debug=True)
