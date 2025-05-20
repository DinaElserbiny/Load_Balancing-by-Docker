from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)

workers = ["http://worker1:5000", "http://worker2:5000", "http://worker3:5000"]
counter = 0

@app.route("/cal")
def load_balance():
    global counter
    target = workers[counter % len(workers)]
    counter += 1
    try:
        n = request.args.get("n", 1)
        response = requests.get(f"{target}/cal", params={"n": n})
        return response.json(), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090)
