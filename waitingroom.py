"""
Python module for using the AlertCaster API
http://developer.alertcaster.com/developer/apiguide
"""

import httplib
import urllib
try:
  import json
except ImportError:
  import simplejson as json

API_KEY = '' # Enter your API Key here...
SERVER = 'developer.alertcaster.com'
BASE_URL = 'http://developer.alertcaster.com/'
SIMPLE_ALERT = BASE_URL + 'developer/api/alert-create-simple'
DELETE_ALERT = BASE_URL + 'developer/api/alert-delete'
DELETE_RECIP_GROUP = BASE_URL + 'developer/api/recipient-group-delete'


class Unauthorized(Exception):
  """
  Raised when 401 Response is received from server.
  """

class WaitingRoomFailure(Exception):
  """
  Raised when an Error Response is received from server.
  """

class WaitingRoom(object):
  def __init__(self, key=API_KEY):
    self.key = key

  def _request(self, method, body, url, content_type=None):
    h = httplib.HTTPConnection(SERVER)
    headers = {}

    if content_type:
      headers['Content-Type'] = content_type

    h.request(method, url, body, headers)
    resp = h.getresponse()

    if resp.status == 401:
      raise Unauthorized

    return resp.status, json.loads(resp.read())

  def simple(self, alerts={}, recipients=[]):
    response = self.createAlert(alerts, recipients)

    self.triggerAlert(response['trigger'])
    self.deleteAlert(response['id'])
    self.deleteRecipientGroup(response['details']['recipient_group_id'])

    print "YAY! Your alert was a success."

  def createAlert(self, alerts={}, recipients=[]):
    if self.key == '':
      raise WaitingRoomFailure('No API Key was initialized or set.')

    data = {}
    data['apikey'] = self.key
    data['name'] = "Temporary Alert"

    for index, rec in enumerate(recipients):
      data['recipient[%s][name]' % index] = "%s, %s" % \
                        (rec['name']['first'], rec['name']['last'])

      if 'email' in alerts:
        data['recipient[%s][email]' % index] = rec['email']

      if 'sms' in alerts:
        data['recipient[%s][mobile]' % index] = rec['mobile']
      elif 'audio' in alerts:
        data['recipient[%s][mobile]' % index] = rec['mobile']

    if 'email' in alerts:
      data['email-subject'] = alerts['email']['subject']
      data['email-body'] = alerts['email']['body']
      
    if 'sms' in alerts:
      data['sms'] = alerts['sms']

    if 'audio' in alerts:
      data['audio'] = alerts['audio']

    body = urllib.urlencode(data)

    status, response = self._request('POST', body,
      SIMPLE_ALERT, 'application/x-www-form-urlencoded')

    if not status == 200 or 'error' in str(response['status']):
      raise WaitingRoomFailure('createAlert', status, response)

    return response

  def triggerAlert(self, url):
    if self.key == '':
      raise WaitingRoomFailure('No API Key was initialized or set.')

    status, response = self._request('GET', '', url)

    if not status == 200 or 'error' in str(response['status']):
      raise WaitingRoomFailure('triggerAlert', status, response)

    return response

  def deleteAlert(self, alertID):
    if self.key == '':
      raise WaitingRoomFailure('No API Key was initialized or set.')

    data = {'apikey': self.key, 'id': alertID}
    body = urllib.urlencode(data)

    status, response = self._request('POST', body, 
      DELETE_ALERT, 'application/x-www-form-urlencoded')

    if not status == 200 or 'error' in str(response['status']):
      raise WaitingRoomFailure('deleteAlert', status, response)

    return response

  def deleteRecipientGroup(self, recipientGroupID):
    if self.key == '':
      raise WaitingRoomFailure('No API Key was initialized or set.')

    data = {'apikey': self.key, 'id': recipientGroupID}
    body = urllib.urlencode(data)

    status, response = self._request('POST', body, 
      DELETE_RECIP_GROUP, 'application/x-www-form-urlencoded')

    if not status == 200 or 'error' in str(response['status']):
      raise WaitingRoomFailure('deleteRecipientGroupID', status, response)

    return response