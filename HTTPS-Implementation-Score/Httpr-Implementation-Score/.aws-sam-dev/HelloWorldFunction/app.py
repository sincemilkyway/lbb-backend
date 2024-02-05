# file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip converted to package
from python_Client.client import RestClient


def lambda_handler(event, context):
     # You can download this file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip
    client = RestClient("toufeek@seocontent.ai", "66755310cf1ef237")
    
    post_data = dict()
    # simple way to get a result
    post_data[len(post_data)] = dict(
        id="07281559-0695-0216-0000-c269be8b7592",
        filters=[
            ["resource_type", "=", "html"],
            "and", 
            ["meta.scripts_count", ">", 40]
        ],
        order_by=["meta.content.plain_text_word_count,desc"],
        limit=10
    )
    # POST /v3/on_page/pages
    # the full list of possible parameters is available in documentation
    response = client.post("/v3/on_page/pages", post_data)
    # you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
    if response["status_code"] == 20000:
        return (response)
    # do something with result
    else:
        return ("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
