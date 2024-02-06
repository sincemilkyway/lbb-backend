# file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip converted to package
import sys
sys.path.append("/opt")
import os
from python_Client.client import RestClient # noqa


def lambda_handler(event, context):
     # You can download this file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip
    client = RestClient(os.environ.get('RestEmail'), os.environ.get('RestPassword'))
    
    # 1 - using this method you can get a list of completed tasks
    # GET /v3/serp/yahoo/organic/tasks_ready
    # in addition to 'yahoo' and 'organic' you can also set other search engine and type parameters
    # the full list of possible parameters is available in documentation
    
    response = client.get("/v3/serp/yahoo/organic/tasks_ready")
    # you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
    if response['status_code'] == 20000:
        results = []
        for task in response['tasks']:
            if (task['result'] and (len(task['result']) > 0)):
                for resultTaskInfo in task['result']:
                    # 2 - using this method you can get results of each completed task
                    # GET /v3/serp/yahoo/organic/advanced/$id
                    if(resultTaskInfo['endpoint_advanced']):
                        results.append(client.get(resultTaskInfo['endpoint_advanced']))                
                    '''
                    # 3 - another way to get the task results by id
                    # GET /v3/serp/yahoo/organic/task_get/advanced/$id                
                    if(resultTaskInfo['id']):
                        results.append(client.get("/v3/serp/yahoo/organic/task_get/advanced/" + resultTaskInfo['id']))
                    '''
        return (response)
        # do something with result
    else:
        return ("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
