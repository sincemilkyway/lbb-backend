# file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip converted to package
from python_Client.client import RestClient


def lambda_handler(event, context):
     # You can download this file from here https://api.dataforseo.com/v3/_examples/python/_python_Client.zip
    client = RestClient("toufeek@seocontent.ai", "66755310cf1ef237")
    
    # 1 - using this method you can get a list of completed tasks
    # GET /v3/serp/google/dataset_search/tasks_ready
    response = client.get("/v3/serp/google/dataset_search/tasks_ready")
    # you can find the full list of the response codes here https://docs.dataforseo.com/v3/appendix/errors
    if response['status_code'] == 20000:
        results = []
        for task in response['tasks']:
            if (task['result'] and (len(task['result']) > 0)):
                for resultTaskInfo in task['result']:
                    # 2 - using this method you can get results of each completed task
                    # GET /v3/serp/google/dataset_search/task_get/advanced/$id
                    if(resultTaskInfo['endpoint_advanced']):
                        results.append(client.get(resultTaskInfo['endpoint_advanced']))                
                    '''
                    # 3 - another way to get the task results by id
                    # GET /v3/serp/google/dataset_search/task_get/advanced/$id                
                    if(resultTaskInfo['id']):
                        results.append(client.get("/v3/serp/google/dataset_search/task_get/advanced/" + resultTaskInfo['id']))
                    '''
        return (response)
        # do something with result
    else:
        return ("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
