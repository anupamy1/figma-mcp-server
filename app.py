from flask import Flask, jsonify, Response

from config import Config
from figma_service import FigmaService
from code_generator import CodeGenerator

app = Flask(__name__)

figma_service = FigmaService()


@app.route("/")
def home():
    return jsonify({
        "message": "Figma MCP Server prototype is running",
        "available_routes": [
            "/figma-file",
            "/figma-pages",
            "/figma-frames",
            "/figma-landing-page",
            "/figma-clean-landing",
            "/figma-image-urls",
            "/generate-html",
            "/generate-html-v2"
        ]
    })


@app.route("/figma-file", methods=["GET"])
def get_figma_file():
    result, status_code = figma_service.get_file_info()
    return jsonify(result), status_code


@app.route("/figma-pages", methods=["GET"])
def get_figma_pages():
    result, status_code = figma_service.get_pages()
    return jsonify(result), status_code


@app.route("/figma-frames", methods=["GET"])
def get_figma_frames():
    result, status_code = figma_service.get_frames()
    return jsonify(result), status_code


@app.route("/figma-landing-page", methods=["GET"])
def get_landing_page_details():
    result, status_code = figma_service.get_landing_page_details()
    return jsonify(result), status_code


@app.route("/figma-clean-landing", methods=["GET"])
def get_clean_landing_page():
    result, status_code = figma_service.get_clean_landing_page_structure()
    return jsonify(result), status_code


@app.route("/figma-image-urls", methods=["GET"])
def get_figma_image_urls():
    image_node_ids = [
        "1:1495",  # Hero Image
        "1:1499",  # Card image 1
        "1:1504",  # Card image 2
        "1:1509",  # Card image 3
        "1:1513",  # Large right image
        "1:1517",  # Bottom card image 1
        "1:1522",  # Bottom card image 2
        "1:1422",  # Avatar 1
        "1:1429",  # Avatar 2
        "1:1436"   # Avatar 3
    ]

    result, status_code = figma_service.get_image_urls(image_node_ids)
    return jsonify(result), status_code


@app.route("/generate-html", methods=["GET"])
def generate_html():
    html_code = CodeGenerator.generate_basic_html()
    return Response(html_code, mimetype="text/html")


@app.route("/generate-html-v2", methods=["GET"])
def generate_html_v2():
    image_node_ids = [
        "1:1495",  # Hero Image
        "1:1499",  # Card image 1
        "1:1504",  # Card image 2
        "1:1509",  # Card image 3
        "1:1513",  # Large right image
        "1:1517",  # Bottom card image 1
        "1:1522",  # Bottom card image 2
        "1:1422",  # Avatar 1
        "1:1429",  # Avatar 2
        "1:1436"   # Avatar 3
    ]

    result, status_code = figma_service.get_image_urls(image_node_ids)

    if status_code != 200:
        return jsonify(result), status_code

    image_urls = result.get("images", {})
    html_code = CodeGenerator.generate_landing_page_html_v2(image_urls)

    return Response(html_code, mimetype="text/html")


if __name__ == "__main__":
    app.run(debug=Config.FLASK_DEBUG)