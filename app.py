import os

from flask import Flask, abort, jsonify, request

# required at startup: the platform injects them, nothing is baked into the image
SHOP_NAME = os.environ["SHOP_NAME"]
ADMIN_TOKEN = os.environ["ADMIN_TOKEN"]

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>{SHOP_NAME}</h1><p>CloudMorph로 배포됐습니다.</p>"


@app.route("/admin")
def admin():
    if request.headers.get("Authorization") != f"Bearer {ADMIN_TOKEN}":
        abort(401)
    return jsonify(shop=SHOP_NAME, admin=True)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200
