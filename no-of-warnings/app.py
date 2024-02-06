# file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip converted to package
import sys
sys.path.append("/opt")
import os
from python_Client.client import RestClient # noqa



def lambda_handler(event, context):
     # You can download this file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip
    client = RestClient(os.environ.get('RestEmail'), os.environ.get('RestPassword'))
    post_data = dict()
    post_data[len(post_data)] = dict(
        limit=10,
        offset=0,
        filtered_function="pingback_url"
    )
    # POST /v3/domain_analytics/errors
    # the full list of possible parameters is available in documentation
    response = client.post("/v3/domain_analytics/errors", post_data)
    # you can find the full list of the response codes here https://docs.dataforseo.com/v3/domain_analytics/errors
    if response["status_code"] == 20000:
        return response['tasks']
    
        # do something with result
    else:
        return ("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))

