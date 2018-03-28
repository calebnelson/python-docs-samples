# Copyright 2016 Google Inc.
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

import webapp2
from aiapi import AiRequest, AiResponse
from aibasic import AiRand, AiLeft
from aicorner import AiCorner
from aiscore import AiScore
from aiquality import AiQuality
from ailookahead import AiLookahead

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
	input_dict = {}
	for key in ['board', 'score', 'gid', 'ai', 'arg']:
		input_dict[key] = self.request.get(key)
	aireq = AiRequest(input_dict)
	if aireq.ai == 'lookahead':
		airesp = AiLookahead(aireq)
	elif aireq.ai == 'quality':
		airesp = AiQuality(aireq)
	elif aireq.ai == 'score':
		airesp = AiScore(aireq)
	elif aireq.ai == 'corner' or aireq.ai == 'ul':
		airesp = AiCorner(aireq)
	elif aireq.ai == 'left':
		airesp = AiLeft(aireq)
	else:
		airesp = AiRand(aireq)
	self.response.write(airesp)


app = webapp2.WSGIApplication([
    ('/ai/ai.py', MainPage),
], debug=True)
