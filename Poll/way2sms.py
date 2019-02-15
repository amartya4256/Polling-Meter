

import requests
import json

URL = 'http://www.way2sms.com/api/v1/sendCampaign'

# get request
def sendPostRequest(phoneNo, textMessage):
  req_params = {
  'apikey':'MD4CSLB4X1GDN0WAWMWITXT1DRWXU53Y',
  'secret':'SK2PUA4B0BEOKF6O',
  'usetype':'stage',
  'phone': phoneNo,
  'message':textMessage,
  # 'senderid':'+917903601431'
  }
  return requests.post(URL, req_params)

# get response
# response = sendPostRequest(URL,'7903601431', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""