#Yong Lee
#leey2@onid.oregonstate.edu

from google.appengine.ext import ndb

class	Account(ndb.Model):
	username = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	
class	Report(ndb.Model):
	title = ndb.StringProperty(required=True)
	when = ndb.StringProperty(required=True)
	where = ndb.StringProperty(required=True)
	description = ndb.StringProperty(required=True)
	username = ndb.StringProperty(required=True)
	type = ndb.StringProperty(required=True)
	
class Type(ndb.Model):
	name = ndb.StringProperty(required=True)
	reports = ndb.KeyProperty(repeated=True)
	
