import os
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

# Simule un "état" applicatif pour rendre le healthcheck un peu réaliste
APP_VERSION = os.environ.get("APP_VERSION", "dev")

PRODUCTS = [
    {"id": 1, "name": "Clavier mécanique", "price": 79.90},
    {"id": 2, "name": "Souris sans fil", "price": 24.50},
    {"id": 3, "name": "Casque audio", "price": 59.00},
]


@app.route("/")
def index():
    return jsonify(
        {
            "service": "microshop",
            "message": "Bienvenue sur l'API MicroShop",
            "version": APP_VERSION,
        }
    )


@app.route("/health")
def health():
    """Utilisé par Kubernetes pour le readinessProbe/livenessProbe."""
    return jsonify({"status": "ok", "time": datetime.now(timezone.utc).isoformat()}), 200


@app.route("/api/products")
def products():
    return jsonify(PRODUCTS)


@app.route("/api/products/<int:product_id>")
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Produit introuvable"}), 404
    return jsonify(product)


if __name__ == "__main__":
    # Pratique pour tester en local : python app.py
    app.run(host="0.0.0.0", port=5000)
