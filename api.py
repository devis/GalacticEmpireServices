#!/usr/bin/env python
#

import webapp2

class RoleHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('ROLES!')

class UserByRoleHandler(webapp2.RequestHandler):
	def get(self):
		self.post()
		
	def post(self):
		incomingRole = self.request.get('role')
		self.response.out.write(incomingRole)

