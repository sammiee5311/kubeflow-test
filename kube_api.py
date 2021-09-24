import requests
import json
from collections import defaultdict
from requests_toolbelt.multipart.encoder import MultipartEncoder


namespace = 
url = 

headers = {'Content-Type': 'application/json'}
cookies = { }

def get_pipelines_info(pipelines):
    res = defaultdict(dict)

    for pipeline in pipelines:
        description = pipeline['description'] if 'description' in pipeline else 'None'
        res[pipeline['id']] = {'name': pipeline['name'], 'description':description, 'created_at':pipeline['created_at'] }
    
    return res

def get_experiments_info(experiments):
    res = defaultdict(dict)

    for experiment in experiments:
        res[experiment['id']] = {'name': experiment['name'], 'created_at':experiment['created_at'] }
    
    return res

def get_all_pipelines():
    response = requests.get(f'http://{url}/pipeline/apis/v1beta1/pipelines', headers=headers, cookies=cookies, verify=False)
    file = json.loads(response.content.decode('utf-8'))

    res = get_pipelines_info(file['pipelines'])

    return res

def get_pipeline(pipeline_id):
    response = requests.get(f'http://{url}/pipeline/apis/v1beta1/pipelines/{pipeline_id}', headers=headers, cookies=cookies, verify=False)
    res = json.loads(response.content.decode('utf-8'))

    return res

def delete_pipeline(pipeline_id):
    requests.delete(f'http://{url}/pipeline/apis/v1beta1/pipelines/{pipeline_id}', headers=headers, cookies=cookies, verify=False)


def get_experiments():
    response = requests.get(f'http://{url}/pipeline/apis/v1beta1/experiments?page_token=&page_size=10&resource_reference_key.type=NAMESPACE&resource_reference_key.id={namespace}', headers=headers, cookies=cookies, verify=False)
    file = json.loads(response.content.decode('utf-8'))

    res = get_experiments_info(file['experiments'])
    
    return res

def delete_experiment(experiment_id):
    requests.delete(f'http://{url}/pipeline/apis/v1beta1/experiments/{experiment_id}', headers=headers, cookies=cookies, verify=False)

def archive_experiment(experiment_id):
    requests.post(f'http://{url}/pipeline/apis/v1beta1/experiments/{experiment_id}:archive', headers=headers, cookies=cookies, verify=False)

def unarchive_experiment(experiment_id):
    response = requests.post(f'http://{url}/pipeline/apis/v1beta1/experiments/{experiment_id}:unarchive', headers=headers, cookies=cookies, verify=False)
    file = json.loads(response.content.decode('utf-8'))

    print(file)

def create_pipeline(pipe_line_name, file):
    file_data = MultipartEncoder(
        fields={
            'uploadfile': (file, open(file, 'rb'))
        }
    )
    response = requests.post(f'http://{url}/pipeline/apis/v1beta1/pipelines/upload?name={pipe_line_name}', headers={'Content-Type': file_data.content_type}, cookies=cookies, verify=False, data=file_data)

    if response.status_code == 200:
        print('success to create a pipeline.')
    else:
        print('fail to create a pipeline.')

def create_experiment(name):
    response = requests.post(f'http://{url}/pipeline/apis/v1beta1/experiments', headers=headers, cookies=cookies, verify=False, data={'name': name})

    if response.status_code == 200:
        print('success to create a experiment.')
    else:
        print('fail to create a experiment.')

def create_run(name, experiment_id, pipeline_id):
    pipeline_spec = {'pipeline_id': pipeline_id}
    body = {'name': name, 'pipeline_spec': pipeline_spec, 'resource_references': [{"key":{"id":experiment_id,"type":"EXPERIMENT"},"relationship":"OWNER"}]}
    response = requests.post(f'http://{url}/pipeline/apis/v1beta1/runs', headers=headers, cookies=cookies, verify=False, json=body)

    if response.status_code == 200:
        print('success to create a run.')
    else:
        print('fail to create a run.')

def get_all_jobs():
    response = requests.get(f'http://{url}/pipeline/apis/v1beta1/jobs?page_token=&page_size=10&resource_reference_key.type=NAMESPACE&resource_reference_key.id={namespace}', headers=headers, cookies=cookies, verify=False)

    print(response.content)

def get_all_runs():
    response = requests.get(f'http://{url}/pipeline/apis/v1beta1/runs?page_token=&page_size=10&resource_reference_key.type=NAMESPACE&resource_reference_key.id={namespace}', headers=headers, cookies=cookies, verify=False)

    print(response.content)


if __name__ == '__main_':

    # pipelines_res = get_all_pipelines()

    # experiments_res = get_experiments()

    # delete_experiment()

    # create_pipeline(name, file)

    # create_run(name, experiment, pipeline)

    # get_all_runs()

    pass
