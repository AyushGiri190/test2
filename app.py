from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins (for development)


@app.route("/check-age", methods=["POST","GET"])
def check_age():
    #data = request.get_json()
    #age = data.get("age", 0)
    age =12 
    if age >= 18:
        return jsonify({"message": "✅ You are eligible to vote!"})
    else:
        return jsonify({"message": "❌ You are not eligible to vote!"})
if __name__ == '__main__':
    # Use 5000 for local development if PORT is not set
    port = int(os.environ.get('PORT', 5000))
    print(f"Running locally on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port)
