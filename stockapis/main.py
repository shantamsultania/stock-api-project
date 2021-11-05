from stockapis.agent_handler import api_handler
from stockapis.helper_classes.helper import info

if __name__ == "__main__":
    info("Debug : api started ")
    api_handler.web_app.run()
