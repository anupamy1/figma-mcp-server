import os
import json
from dotenv import load_dotenv
load_dotenv()
from config import Config
from figma_service import FigmaService
import requests

Config.validate()
service = FigmaService()
service.landing_page_node_id = '1:902'
url = f'{service.base_url}/files/{service.file_id}/nodes'
params = {'ids': service.landing_page_node_id, 'depth': 2}
resp = requests.get(url, headers=service.get_headers(), params=params)
print('status', resp.status_code)
data = resp.json()
node = data['nodes'][service.landing_page_node_id]['document']

image_nodes = []

# collect all nodes recursively

def collect(node, path):
    nid = node.get('id')
    name = node.get('name', '')
    typ = node.get('type', '')
    if typ in ['RECTANGLE', 'ELLIPSE', 'VECTOR', 'FRAME', 'COMPONENT', 'INSTANCE']:
        if 'image' in name.lower() or typ in ['RECTANGLE', 'ELLIPSE', 'VECTOR']:
            image_nodes.append({'id': nid, 'name': name, 'type': typ, 'path': path + '/' + name})
    if node.get('children'):
        for child in node['children']:
            collect(child, path + '/' + name)

collect(node, '')
print(json.dumps(image_nodes, indent=2))
