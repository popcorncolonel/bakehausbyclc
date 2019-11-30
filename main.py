import endpoints
import jinja2
import logging
import os
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True,
)


class LocationHandler(webapp2.RequestHandler):
    '''
    Location page with the address and a map.
    '''
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('location.html')
        self.response.write(template.render(template_values))


class MenuHandler(webapp2.RequestHandler):
    '''
    Menu page. Figure out if it should just be a pdf or a menu in a database.
    '''
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('menu.html')
        self.response.write(template.render(template_values))


class ContactHandler(webapp2.RequestHandler):
    '''
    Contact info page.
    '''
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.write(template.render(template_values))


class MainHandler(webapp2.RequestHandler):
    '''
    Main page.
    '''
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    (r'/', MainHandler),
    (r'/location', LocationHandler),
    (r'/menu', MenuHandler),
    (r'/contact', ContactHandler),
], debug=True)

