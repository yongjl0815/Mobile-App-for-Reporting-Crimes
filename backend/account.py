#Yong Lee
#leey2@onid.oregonstate.edu

import webapp2
from google.appengine.ext import ndb
import db_def
import json


class	Login(webapp2.RequestHandler):
	def post(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return	
		
		username = self.request.get('username', default_value=None)
		password = self.request.get('password', default_value=None)
		
		a = db_def.Account.query(db_def.Account.username == username).fetch()
		for s in a:
			if s.username == username:
				if s.password == password:
					results = { 'keys' : username}
					self.response.write(json.dumps(results))
					return
		results = { 'keys' : 'nnnNo'}
		self.response.write(json.dumps(results))

		
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
		
		username = self.request.get('username', default_value=None)
		password = self.request.get('password', default_value=None)
		
		qry = ""
		qry = db_def.Account.query(db_def.Account.username == username).fetch()
		
		if qry:
			results = { 'keys' : 'aaaNo'}
			self.response.write(json.dumps(results))
		else:
			new_p = db_def.Account()	
				
			if username:
				new_p.username = username
			else:	
				results = { 'keys' : 'uuuNo'}
				self.response.write(json.dumps(results))
				return
			if password:
				new_p.password = password
			else:	
				results = { 'keys' : 'pppNo'}
				self.response.write(json.dumps(results))
				return
			key = new_p.put()	
			out = new_p.to_dict()
			self.response.write(json.dumps(out))
			

class See(webapp2.RequestHandler):
	def get(self):
		self.response.headers.add_header("Access-Control-Allow-Origin", "*")
		self.response.headers.add_header("Access-Control-Allow-Methods", "GET, POST, DELETE")
		self.response.headers.add_header("Access-Control-Allow-Headers", "origin, x-requested-with, content-type, accept")
		self.response.headers.add_header('Content-Type', 'application/json')
		if 'application/json' not in self.request.accept:
			self.response.status = 406
			self.response.status_message = "Not valid"
			return

		a = db_def.Account.query().fetch()
		
		for s in a:
			self.response.out.write(s.username)
			self.response.out.write(" ")
			self.response.out.write(s.password)
			self.response.out.write("\n")

			
			
			
			
			
			