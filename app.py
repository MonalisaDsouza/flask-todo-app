import os
from flask import Flask, send_from_directory
from config import Config
from models import db
from routes import bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(bp)

SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"

swagger_ui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "FlaskTodo API"},
)
app.register_blueprint(swagger_ui_bp, url_prefix=SWAGGER_URL)


@app.route("/static/<path:filename>")
def swagger_static(filename):
    return send_from_directory(os.path.join(app.root_path, "static"), filename)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
