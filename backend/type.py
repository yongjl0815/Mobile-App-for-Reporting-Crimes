#Yong Lee
#leey2@onid.oregonstate.edu

import webapp2
from google.appengine.ext import ndb
import db_def
import json


class	Create(webapp2.RequestHandler):
	def post(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return	
		
		name = self.request.get('name', default_value=None)
		
		new = db_def.Type()	
		
		if name:
			new.name = name
		else:	
			self.response.write(json.dumps("Name is required"))
			return
			
		key = new.put()	
		out = new.to_dict()
		self.response.write(json.dumps(out))
			

class SeeV(webapp2.RequestHandler):
	def get(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return
		results = ''			
		a = db_def.Type.query(db_def.Type.name == 'Victim').fetch()
		for s in a:
			results = {'reports' : [k.id() for k in s.reports]}
			
		self.response.write(json.dumps(results))			

		
class SeeW(webapp2.RequestHandler):
	def get(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return
		results = ''
		a = db_def.Type.query(db_def.Type.name == 'Witness').fetch()
		for s in a:
			results = {'reports' : [k.id() for k in s.reports]}
			
		self.response.write(json.dumps(results))	

		
class SeeP(webapp2.RequestHandler):
	def get(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return
		results = ''
		a = db_def.Type.query(db_def.Type.name == 'Perpetrator').fetch()
		for s in a:
			results = {'reports' : [k.id() for k in s.reports]}
			
		self.response.write(json.dumps(results))	

			
class Search(webapp2.RequestHandler):
	def get(self, **kwargs):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return

		if 'id' in kwargs:
			out = ndb.Key(db_def.Report, int(kwargs['id'])) #.get().to_dict()
			a = out.get()
			if a:
				results = { 'title' : a.title, 'when' : a.when ,'where' : a.where , 'description' : a.description, 'type' : a.type, 'user' : a.username}
				self.response.write(json.dumps(results))			
			else:	
				results = { 'keys' : 'No'}
				self.response.write(json.dumps(results))	

			
class Delete(webapp2.RequestHandler):
	def delete(self, **kwargs):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return

		if 'id' in kwargs:
			out = ndb.Key(db_def.Type, int(kwargs['id'])) #.get().to_dict()
			a = out.get()
			if a:
				a.key.delete()
				results = { 'keys' : 'Deleted'}
				self.response.write(json.dumps(results))			
			else:	
				results = { 'keys' : 'Not Deleted'}
				self.response.write(json.dumps(results))	
			
			
			
			
			
			
			