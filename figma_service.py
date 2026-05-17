import requests
from config import Config


class FigmaService:
    def __init__(self):
        Config.validate()

        self.access_token = Config.FIGMA_ACCESS_TOKEN
        self.file_id = Config.FIGMA_FILE_ID
        self.landing_page_node_id = Config.LANDING_PAGE_NODE_ID
        self.base_url = "https://api.figma.com/v1"

    def get_headers(self):
        return {
            "X-Figma-Token": self.access_token
        }

    def handle_error_response(self, response, custom_message):
        return {
            "error": custom_message,
            "status_code": response.status_code,
            "details": response.text
        }

    def get_file_info(self):
        url = f"{self.base_url}/files/{self.file_id}"
        response = requests.get(url, headers=self.get_headers())

        if response.status_code != 200:
            return self.handle_error_response(response, "Failed to fetch Figma file"), response.status_code

        data = response.json()

        return {
            "message": "Figma file fetched successfully",
            "file_name": data.get("name"),
            "last_modified": data.get("lastModified"),
            "version": data.get("version"),
            "document_name": data.get("document", {}).get("name")
        }, 200

    def get_pages(self):
        url = f"{self.base_url}/files/{self.file_id}"
        response = requests.get(url, headers=self.get_headers())

        if response.status_code != 200:
            return self.handle_error_response(response, "Failed to fetch Figma pages"), response.status_code

        data = response.json()
        document = data.get("document", {})
        pages = document.get("children", [])

        result = []

        for page in pages:
            result.append({
                "page_name": page.get("name"),
                "page_id": page.get("id"),
                "type": page.get("type"),
                "children_count": len(page.get("children", []))
            })

        return {
            "message": "Figma pages fetched successfully",
            "pages": result
        }, 200

    def get_frames(self):
        url = f"{self.base_url}/files/{self.file_id}"
        response = requests.get(url, headers=self.get_headers())

        if response.status_code != 200:
            return self.handle_error_response(response, "Failed to fetch Figma frames"), response.status_code

        data = response.json()
        document = data.get("document", {})
        pages = document.get("children", [])

        frames_result = []

        for page in pages:
            page_name = page.get("name")
            children = page.get("children", [])

            for item in children:
                box = item.get("absoluteBoundingBox", {})

                frames_result.append({
                    "page_name": page_name,
                    "name": item.get("name"),
                    "id": item.get("id"),
                    "type": item.get("type"),
                    "width": box.get("width"),
                    "height": box.get("height"),
                    "x": box.get("x"),
                    "y": box.get("y"),
                    "children_count": len(item.get("children", []))
                })

        return {
            "message": "Figma frames fetched successfully",
            "frames": frames_result
        }, 200

    def get_landing_page_document(self):
        url = f"{self.base_url}/files/{self.file_id}/nodes"
        params = {
            "ids": self.landing_page_node_id
        }

        response = requests.get(
            url,
            headers=self.get_headers(),
            params=params
        )

        if response.status_code != 200:
            return None, response

        data = response.json()
        nodes = data.get("nodes", {})
        landing_node_data = nodes.get(self.landing_page_node_id, {})
        landing_document = landing_node_data.get("document", {})

        return landing_document, response

    def collect_nodes(self, node, result):
        box = node.get("absoluteBoundingBox", {})

        item = {
            "id": node.get("id"),
            "name": node.get("name"),
            "type": node.get("type"),
            "x": box.get("x"),
            "y": box.get("y"),
            "width": box.get("width"),
            "height": box.get("height"),
            "children_count": len(node.get("children", []))
        }

        if node.get("type") == "TEXT":
            item["text"] = node.get("characters", "")

        result.append(item)

        for child in node.get("children", []):
            self.collect_nodes(child, result)

    def get_landing_page_details(self):
        landing_document, response = self.get_landing_page_document()

        if response.status_code != 200:
            return self.handle_error_response(response, "Failed to fetch landing page details"), response.status_code

        if not landing_document:
            return {
                "error": "Landing page node not found"
            }, 404

        result = []
        self.collect_nodes(landing_document, result)

        return {
            "message": "Landing page details fetched successfully",
            "frame_name": landing_document.get("name"),
            "frame_id": landing_document.get("id"),
            "total_elements": len(result),
            "elements": result
        }, 200

    def get_clean_landing_page_structure(self):
        landing_document, response = self.get_landing_page_document()

        if response.status_code != 200:
            return self.handle_error_response(response, "Failed to fetch landing page details"), response.status_code

        if not landing_document:
            return {
                "error": "Landing page node not found"
            }, 404

        all_elements = []
        self.collect_nodes(landing_document, all_elements)

        headings = []
        paragraphs = []
        buttons = []
        images = []
        sections = []
        cards = []

        for item in all_elements:
            name = item.get("name", "")
            item_type = item.get("type", "")
            text = item.get("text", "")

            lower_name = name.lower()
            lower_text = text.lower()

            if item_type == "TEXT":
                if "heading" in lower_name or "title" in lower_name:
                    headings.append({
                        "id": item.get("id"),
                        "text": text,
                        "x": item.get("x"),
                        "y": item.get("y"),
                        "width": item.get("width"),
                        "height": item.get("height")
                    })
                elif text:
                    paragraphs.append({
                        "id": item.get("id"),
                        "text": text,
                        "x": item.get("x"),
                        "y": item.get("y"),
                        "width": item.get("width"),
                        "height": item.get("height")
                    })

            if "button" in lower_name or "button" in lower_text:
                buttons.append({
                    "id": item.get("id"),
                    "name": name,
                    "text": text,
                    "type": item_type,
                    "x": item.get("x"),
                    "y": item.get("y"),
                    "width": item.get("width"),
                    "height": item.get("height")
                })

            if "image" in lower_name or item_type in ["RECTANGLE", "ELLIPSE"]:
                images.append({
                    "id": item.get("id"),
                    "name": name,
                    "type": item_type,
                    "x": item.get("x"),
                    "y": item.get("y"),
                    "width": item.get("width"),
                    "height": item.get("height")
                })

            if item_type == "FRAME" and (
                "navigation" in lower_name
                or "section" in lower_name
                or "footer" in lower_name
                or "copy" in lower_name
                or "text" in lower_name
            ):
                sections.append({
                    "id": item.get("id"),
                    "name": name,
                    "type": item_type,
                    "x": item.get("x"),
                    "y": item.get("y"),
                    "width": item.get("width"),
                    "height": item.get("height"),
                    "children_count": item.get("children_count")
                })

            if "card" in lower_name:
                cards.append({
                    "id": item.get("id"),
                    "name": name,
                    "type": item_type,
                    "x": item.get("x"),
                    "y": item.get("y"),
                    "width": item.get("width"),
                    "height": item.get("height"),
                    "children_count": item.get("children_count")
                })

        return {
            "message": "Clean landing page structure generated successfully",
            "frame_name": landing_document.get("name"),
            "frame_id": landing_document.get("id"),
            "summary": {
                "total_elements": len(all_elements),
                "headings_count": len(headings),
                "paragraphs_count": len(paragraphs),
                "buttons_count": len(buttons),
                "images_count": len(images),
                "sections_count": len(sections),
                "cards_count": len(cards)
            },
            "headings": headings,
            "paragraphs": paragraphs,
            "buttons": buttons,
            "images": images,
            "sections": sections,
            "cards": cards
        }, 200

    def get_image_urls(self, node_ids, scale=2, image_format="png"):
        url = f"{self.base_url}/images/{self.file_id}"

        params = {
            "ids": ",".join(node_ids),
            "format": image_format,
            "scale": scale
        }

        response = requests.get(
            url,
            headers=self.get_headers(),
            params=params
        )

        if response.status_code != 200:
            return self.handle_error_response(response, "Failed to fetch Figma image URLs"), response.status_code

        data = response.json()

        return {
            "message": "Figma image URLs fetched successfully",
            "images": data.get("images", {})
        }, 200