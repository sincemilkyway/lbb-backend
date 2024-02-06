# file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip converted to package
from random import Random
import sys
import os
sys.path.append("/opt")
from python_Client.client import RestClient # noqa

def lambda_handler(event, context):
     # You can download this file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip
    client = RestClient(os.environ.get('RestEmail'), os.environ.get('RestPassword'))
    # using this method you can get the results for task
    # GET /v3/on_page/lighthouse/task_get/json/$id
    id = "07281559-0695-0216-0000-c269be8b7592"
    response = client.get("/v3/on_page/lighthouse/task_get/json/" + id)
    # you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
    if response["status_code"] == 20000:
        return (response)
        # do something with result
    else:
        return ("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
