import unittest
from google.appengine.ext import testbed
import webapp2, webtest

from api import RoleHandler, UserByRoleHandler 

class api_tests(unittest.TestCase):

  def setUp(self):
    app = webapp2.WSGIApplication([
			('/getRoles', RoleHandler),
			('/getUsersByRole', UserByRoleHandler),
		])
    self.testapp = webtest.TestApp(app)
    self.testbed = testbed.Testbed()
    self.testbed.activate()

  def tearDown(self):
     self.testbed.deactivate()

  def test_RolesHandler_returns_roles(self):
    response = self.testapp.get('/getRoles')
    self.assertEqual(response.normal_body, 'ROLES!')

  def test_UserByRoleHandler_returns_nothing_when_no_request_param(self):
	params = {}
	response = self.testapp.post('/getUsersByRole', params)
	self.assertEquals(response.normal_body, "")
	
  def test_UserByRoleHandler_returns_role_when_passed_role(self):
	params = {'role': 'Foo'}
	response = self.testapp.post('/getUsersByRole', params)
	self.assertEqual(response.normal_body, 'Foo')

if __name__ == '__main__':
    unittest.main()