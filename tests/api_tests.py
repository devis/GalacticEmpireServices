import unittest
from google.appengine.ext import testbed
import webapp2, webtest, json

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
    jsonResp = json.loads(response.normal_body)
    self.assertEqual("Darth Vader", jsonResp[0])

  def test_RolesHandler_rejects_post(self):
	response = self.testapp.post('/getRoles', status="*")
	self.assertEqual(response.status_int, 405)

  def test_UserByRoleHandler_empty_response_with_no_params(self):
	params = {}
	response = self.testapp.post('/getUsersByRole', params)
	jsonResp = json.loads(response.normal_body)
	self.assertEquals([], jsonResp)
	
  def test_UserByRoleHandler_returns_users_when_passed_valid_role(self):
	params = {'role': 'Sith'}
	response = self.testapp.post('/getUsersByRole', params)
	jsonResp = json.loads(response.normal_body)
	self.assertEqual("Adam Kendall", jsonResp[0])
	
  def test_UserByRoleHandler_returns_empty_list_for_invalid_role(self):
	params = {'role': 'Foo'}
	response = self.testapp.post('/getUsersByRole', params)
	jsonResp = json.loads(response.normal_body)
	self.assertEquals([], jsonResp)	

if __name__ == '__main__':
    unittest.main()