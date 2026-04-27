from flask import Flask, request, jsonify
from branch_handler import handle_event

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.json

    # Optional: verify GitHub secret here

    handle_event(payload)

    return jsonify({"status": "received"}), 200


if __name__ == "__main__":
    app.run(port=4000)
