import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = False)

class HomePage(webapp2.RequestHandler):
    home_template = jinja_environment.get_template('home.html')

app = webapp2.WSGIApplication([
    ('/', HomePage)
], debug=True)
