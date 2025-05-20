from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route("/cal")
def calculate():
    try:
        n = int(request.args.get("n", 1))
        total = 0
        limit = n * 10**6
        for i in range(1, limit + 1):
            total += (math.sqrt(i) * math.sin(i)) / math.log(i + 1)
        return jsonify({"result": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
