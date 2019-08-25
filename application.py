import azure.cosmos.cosmos_client as cosmos_client
from flask import Flask, request

config = {
    'ENDPOINT': 'https://holy-dream.documents.azure.com:443/',
    'PRIMARYKEY': '',
    'DATABASE': 'CosmosDatabase',
    'CONTAINER': 'CosmosContainer'
}

database_link = 'dbs/' + config['DATABASE']
collection_link = database_link + '/colls/' + config['CONTAINER']

app = Flask(__name__)

client = cosmos_client.CosmosClient(url_connection=config['ENDPOINT'], auth={'masterKey': config['PRIMARYKEY']})

@app.route('/', methods=['POST'])
def hello():
    
    data = request.get_json(force=True);

    print(data)
    
    client.CreateItem(collection_link, data)
    
    return "hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
