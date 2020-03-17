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


class MissionHandler(webapp2.RequestHandler):
    '''
    Gives a description of the mission.
    '''
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('mission.html')
        self.response.write(template.render(template_values))


class ContactHandler(webapp2.RequestHandler):
    '''
    Contact info page.
    '''
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('contact.html')
        self.response.write(template.render(template_values))

class NewsHandler(webapp2.RequestHandler):
    '''
    News info page.
    '''
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('news.html')
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
    (r'/mission', MissionHandler),
    (r'/news', NewsHandler),
    (r'/contact', ContactHandler),
], debug=True)
