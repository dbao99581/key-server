from flask import Flask, request, jsonify

app = Flask(__name__)

keys = {
    "gbaocute": None
}

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    key = data.get("key")
    device = data.get("device")

    if key not in keys:
        return jsonify({"status": "error"})

    if keys[key] is None:
        keys[key] = device
        return jsonify({"status": "ok"})

    if keys[key] == device:
        return jsonify({"status": "ok"})

    return jsonify({"status": "error"})

app.run(host="0.0.0.0", port=5000)
