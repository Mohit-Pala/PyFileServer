from flask import Flask
from flask_smorest import Api
from blueprints.test import blp as TestBlueprint

app = Flask(__name__)

# --- Flask-Smorest and OpenAPI Configuration ---
app.config["API_TITLE"] = "Modular API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(TestBlueprint)

if __name__ == "__main__":
    app.run(debug=True, port=8080)