import os
import json
from dotenv import load_dotenv
load_dotenv()
from config import Config
from figma_service import FigmaService
import requests

Config.validate()
service = FigmaService()
url = f'{service.base_url}/files/{service.file_id}'
resp = requests.get(url, headers=service.get_headers())
print('status', resp.status_code)
data = resp.json()

def traverse(node, path):
    nid = node.get('id')
    name = node.get('name')
    typ = node.get('type')
    if typ in ['FRAME', 'CANVAS', 'COMPONENT_SET', 'COMPONENT', 'GROUP', 'INSTANCE', 'PAGE']:
        if name and 'landing' in name.lower():
            print('FOUND/LANDING', path + '/' + name, nid, typ)
    if nid == '1:1413':
        print('FOUND ID', path + '/' + name, nid, typ)
    for child in node.get('children', []):
        traverse(child, path + '/' + name)

traverse(data['document'], '')
print('done')
