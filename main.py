#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from api import RoleHandler, UserByRoleHandler

class MainHandler(webapp2.RequestHandler):
    def get(self):
       self.response.out.write("""
<h1>Hello Clones!</h1>

<p>We have two service methods:</p>
<ul>
	<li>
		/api/getRoles
		<ul>
			<li>Uses HTTP GET</li>
			<li>Requires no parameters</li>
			<li>Returns JSON array of role names</li>
		</ul>
	</li>
	<li>
		/api/getUsersByRole
		<ul>
			<li>Uses HTTP POST</li>
			<li>Requires one parameter: role</li>
			<li>Returns JSON array of user names</li>
		</ul>
	</li>
</ul>	
""")

app = webapp2.WSGIApplication([
		('/', MainHandler),
		('/api/getRoles', RoleHandler),
		('/api/getUsersByRole', UserByRoleHandler),
	],debug=True)
