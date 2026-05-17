import os
import json
from dotenv import load_dotenv
load_dotenv()
from config import Config
from figma_service import FigmaService
Config.validate()
service = FigmaService()
service.landing_page_node_id = '1:902'
result, status = service.get_clean_landing_page_structure()
print(status)
print(json.dumps(result, indent=2))
