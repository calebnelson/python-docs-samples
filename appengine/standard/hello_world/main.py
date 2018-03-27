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
from aiscore import AiScore
from ailookahead import AiLookahead

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
	input_dict = {}
	for key in ['board', 'score', 'gid', 'ai', 'arg']:
		input_dict[key] = self.request.get(key)
	aireq = AiRequest(input_dict)
        self.response.write(str(aireq))
	self.response.write(str(AiLookahead(aireq)))


app = webapp2.WSGIApplication([
    ('/ai', MainPage),
], debug=True)
