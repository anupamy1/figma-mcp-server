import os
import json
from dotenv import load_dotenv
load_dotenv()
from config import Config
from figma_service import FigmaService
Config.validate()
service = FigmaService()
node_ids = ['1:903','1:904','1:905','1:984','1:1002']
result, status = service.get_image_urls(node_ids)
print(status)
print(json.dumps(result, indent=2))
