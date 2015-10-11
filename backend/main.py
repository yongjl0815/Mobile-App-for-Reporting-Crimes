#Yong Lee
#leey2@onid.oregonstate.edu

import webapp2
from google.appengine.api import oauth

app = webapp2.WSGIApplication([
	('/login', 'account.Login'),
	('/rcreate', 'report.Create'),
], debug=True)
app.router.add(webapp2.Route(r'/create', 'account.Create'))
app.router.add(webapp2.Route(r'/see', 'account.See'))
app.router.add(webapp2.Route(r'/rupdate', 'report.Update'))
app.router.add(webapp2.Route(r'/rsee/<user:\w+>', 'report.See'))
app.router.add(webapp2.Route(r'/rsee2/<id:[0-9]+><:/?>', 'report.See2'))
app.router.add(webapp2.Route(r'/rdelete/<id:[0-9]+><:/?>', 'report.Delete'))
app.router.add(webapp2.Route(r'/tcreate', 'type.Create'))
app.router.add(webapp2.Route(r'/tsee/V', 'type.SeeV'))
app.router.add(webapp2.Route(r'/tsee/W', 'type.SeeW'))
app.router.add(webapp2.Route(r'/tsee/P', 'type.SeeP'))
app.router.add(webapp2.Route(r'/tsearch/<id:[0-9]+><:/?>', 'type.Search'))
app.router.add(webapp2.Route(r'/tdelete/<id:[0-9]+><:/?>', 'type.Delete'))