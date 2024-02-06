# file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip converted to package
import sys
import os
from random import Random
sys.path.append("/opt")
from python_Client.client import RestClient # noqa


def lambda_handler(event, context):
     # You can download this file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip
    client = RestClient(os.environ.get('RestEmail'), os.environ.get('RestPassword'))
    
    rnd = Random()
    post_data = dict()
    # example #1 - a simple way to set a task
    post_data[rnd.randint(1, 30000000)] = dict(
        url="https://dataforseo.com/apis/on-page-api"
    )
    # example #2 - a way to set a task with additional parameters
    post_data[rnd.randint(1, 30000000)] = dict(
        url = "https://dataforseo.com/blog",
        enable_javascript=True,
        custom_js="meta = {}; meta.url = document.URL; meta;"
    )
    # POST /v3/on_page/instant_pages
    # the full list of possible parameters is available in documentation
    response = client.post("/v3/on_page/instant_pages", post_data)
    #   you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
    if response["status_code"] == 20000:
        return (response)
        # do something with result
    else:
        return ("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
