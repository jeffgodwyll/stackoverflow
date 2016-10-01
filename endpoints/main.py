# from datetime import datetime

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

# from google.appengine.api import memcache
# from google.appengine.api import taskqueue
# from google.appengine.ext import ndb

# --- Setup Code

WEB_CLIENT_ID = 'app-id'


# --- Classes

class Hello(messages.Message):
    """String that stores a message."""
    greeting = messages.StringField(1)


class TestOne(messages.Message):
    ''' TestOne message '''
    msg = messages.StringField(1)


# --- API & Endpoints

@endpoints.api(name='whoamigame', version='v1')
class Api(remote.Service):

    @endpoints.method(message_types.VoidMessage, TestOne, path='testone',
                      http_method='GET', name='testonemethod')
    def testOneM(self, req):
        testOneMsgReturn = TestOne(msg='Test One...')
        return testOneMsgReturn


# --- API

api = endpoints.api_server([Api])
