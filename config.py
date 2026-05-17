import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FIGMA_ACCESS_TOKEN = os.getenv("FIGMA_ACCESS_TOKEN")
    FIGMA_FILE_ID = os.getenv("FIGMA_FILE_ID")
    LANDING_PAGE_NODE_ID = os.getenv("LANDING_PAGE_NODE_ID")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"

    @staticmethod
    def validate():
        missing_values = []

        if not Config.FIGMA_ACCESS_TOKEN:
            missing_values.append("FIGMA_ACCESS_TOKEN")

        if not Config.FIGMA_FILE_ID:
            missing_values.append("FIGMA_FILE_ID")

        if not Config.LANDING_PAGE_NODE_ID:
            missing_values.append("LANDING_PAGE_NODE_ID")

        if missing_values:
            raise ValueError(
                "Missing environment values in .env file: "
                + ", ".join(missing_values)
            )