from flask import Flask, jsonify
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Home Route
    @app.route("/")
    def home():
        return jsonify({
            "message": "Flask Backend Mastery ",
            "chapter": "Fundamentals",
            "day": "01"
        })

    # Health Check (used in real backend systems)
    @app.route("/health")
    def health():
        return jsonify({
            "status": "OK",
            "app_name": app.config["APP_NAME"]
        })

    # Dynamic Route
    @app.route("/user/<string:name>")
    def greet_user(name):
        return jsonify({
            "message": f"Hello {name}",
            "status": "success"
        })

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)