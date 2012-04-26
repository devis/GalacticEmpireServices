#!/usr/bin/env python
#

import webapp2
import json

roles = ["Darth Vader", "Luke Skywalker", "Princess Leia", "Han Solo", "C-3PO", "Yoda", "Wookie", "Sith", "Clone", "Jedi"]
users = {
    roles[0]:["Chris Kagy"],
	roles[1]:["Martin Hudson"],
	roles[2]:["Tina Mossi"],
	roles[3]:["Dennis Lauder"],
	roles[4]:["Heidi Acquino"],
	roles[5]:["Randy Smith"],
	roles[6]:["Steve Curtis", "Jake Stone", "Lee Crank", "Peter Kaplan", "Chris Kaby"],
	roles[7]:["Adam Kendall", "Nick Matthews", "Ben Wetzel", "Catherine Seguin", "Matt Steele", "Alan Johnston"],
	roles[8]:["Donald Oellerich", "Jennifer Iacono", "Greg Henley", "Roberto Osorio", "Robert Byrne"],
	roles[9]:["Rob Tirserio", "Justin Stockton", "Lex Berezhny", "David Detweiler", "Tirna Singh", "Vihar Parikh"],	
}

class RoleHandler(webapp2.RequestHandler):
    def get(self):        
        self.response.out.write(json.dumps(roles))

class UserByRoleHandler(webapp2.RequestHandler):
    def post(self):
        incomingRole = self.request.get('role')
        if incomingRole:
            try:
				self.response.out.write(json.dumps(users[incomingRole]))
            except:
                self.response.out.write(json.dumps([]))
        else:
            self.response.out.write(json.dumps([]))

