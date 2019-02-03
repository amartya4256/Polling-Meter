

import requests
import json

URL = 'http://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(phoneNo, textMessage):
  req_params = {
  'apikey':'YRIJRGPLJ1YN8ZVL1I7A7RTH323V97PN',
  'secret':'WSKE4WXSQWOW2NCM',
  'usetype':'stage',
  'phone': phoneNo,
  'message':textMessage,
  # 'senderid':'+919934785875'
  }
  return requests.post(URL, req_params)

# get response
# response = sendPostRequest(URL,'9934785875', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""