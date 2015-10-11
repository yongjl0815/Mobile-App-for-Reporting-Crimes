#Yong Lee
#leey2@onid.oregonstate.edu

import webapp2
from google.appengine.ext import ndb
import db_def
import json


class Create(webapp2.RequestHandler):
	def post(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return

		title = self.request.get('title', default_value=None)
		when = self.request.get('when', default_value=None)
		where = self.request.get('where', default_value=None)
		description = self.request.get('description', default_value=None)
		username = self.request.get('username', default_value=None)
		type = self.request.get('type', default_value=None)

		new_p = db_def.Report()	
				
		if title:
			new_p.title = title
		else:	
			results = { 'keys' : 'required'}
			self.response.write(json.dumps(results))	
			return
			
		if when:
			new_p.when = when
		else:	
			results = { 'keys' : 'required'}
			self.response.write(json.dumps(results))	
			return
			
		if where:
			new_p.where = where
		else:	
			results = { 'keys' : 'required'}
			self.response.write(json.dumps(results))	
			return
			
		if description:
			new_p.description = description
		else:	
			results = { 'keys' : 'required'}
			self.response.write(json.dumps(results))	
			return
			
		if username:		
			new_p.username = username
		else:
			results = { 'keys' : 'Unauthorized'}
			self.response.write(json.dumps(results))	
			return
			
		new_p.type = type
				
		t = db_def.Type.query(db_def.Type.name == type).fetch()
		
		new_p.put()	
	
		for s in t:
			rel = ndb.Key(db_def.Type, s.key.id()).get()
			rel1 = ndb.Key(db_def.Report, new_p.key.id())
			rel.reports.append(rel1)
			rel.put()
			
		results = { 'keys' : 'Done'}
		self.response.write(json.dumps(results))	


class See(webapp2.RequestHandler):
	def get(self, user):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return

		if user:		
			#self.response.write(json.dumps([p.to_dict() for p in db_def.Report.query(db_def.Report.username == user).fetch()]))
			a = db_def.Report.query(db_def.Report.username == user).fetch()

			for s in a:
				if s:
					results = { 'reports' : [k.key.id() for k in a], 'title' : [q.title for q in a]}
				else:
					results = { 'reports' : "No Record"}
			self.response.write(json.dumps(results))

		else:
			results = { 'keys' : 'Unauthorized'}
			self.response.write(json.dumps(results))	
			return

			
class See2(webapp2.RequestHandler):
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
				results = { 'title' : a.title, 'when' : a.when ,'where' : a.where , 'description' : a.description, 'type' : a.type}
				self.response.write(json.dumps(results))			
			else:	
				results = { 'keys' : 'No'}
				self.response.write(json.dumps(results))					

class Update(webapp2.RequestHandler):
	def options(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "http://web.engr.oregonstate.edu")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		
	def put(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "http://web.engr.oregonstate.edu")
		self.response.headers.add_header('Content-Type', 'application/json')	
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return
			
		username = self.request.get('username', default_value=None)	
		id = self.request.get('id', default_value=None)	
		if id:
			b = ndb.Key(db_def.Report, int(id))#.get().to_dict()
			c = b.get()	
			
		if username == c.username :	
			if id:
				out = ndb.Key(db_def.Report, int(id))#.get().to_dict()
				a = out.get()
				if a:
					title = self.request.get('title', default_value=None)
					when = self.request.get('when', default_value=None)
					where = self.request.get('where', default_value=None)
					description = self.request.get('description', default_value=None)
				
					if title:
						a.title = title
						
					if when:
						a.when = when
						
					if where:
						a.where = where
						
					if description:
						a.description = description

					a.put()
					results = { 'keys' : 'Updated'}
					self.response.write(json.dumps(results))	
				else:	
					results = { 'keys' : 'Not Updated'}
					self.response.write(json.dumps(results))					
		else:
			results = { 'keys' : 'Unauthorized'}
			self.response.write(json.dumps(results))	
			return


		
class Delete(webapp2.RequestHandler):
	def options(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "http://web.engr.oregonstate.edu")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE, OPTIONS")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		
	def delete(self, **kwargs):
		self.response.headers.add_header("Access-Control-Allow-Origin", "http://web.engr.oregonstate.edu")
		self.response.headers.add_header('Content-Type', 'application/json')	
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return

		if 'id' in kwargs:
			out = ndb.Key(db_def.Report, int(kwargs['id'])) #.get().to_dict()
			a = out.get()
			if a:
				a.key.delete()
				results = { 'keys' : 'Deleted'}
				self.response.write(json.dumps(results))			
			else:	
				results = { 'keys' : 'Not Deleted'}
				self.response.write(json.dumps(results))	


		