import json
from cloudant.client import CouchDB

USERNAME = 'admin'
PASSWORD = 'password'
DATABASE = 'dbname'

client = CouchDB(USERNAME, PASSWORD, url='http://127.0.0.1:5984', connect=True)

# Open an existing database
db = client[DATABASE]

# Define the end point and parameters
endpoint = DATABASE + '/_find'
params = {'selector': {'source': 'CNN', 'category': 'news'}, 'execution_stats': True}

def endpointAccess(params, endpoint):
    end_point = '{0}/{1}'.format(client.server_url, endpoint)
    headers = {'Content-Type': 'application/json'}
    response = db.r_session.post(end_point, headers=headers, data=json.dumps(params, cls=db.client.encoder))
    response = response.json()
    return response

response = endpointAccess(params, endpoint)
print(response['execution_stats']['results_returned']
