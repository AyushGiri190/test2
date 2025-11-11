from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from response import get_chatbot_response
app = Flask(__name__)
CORS(app)  # Allow all origins (for development)

@app.route('/chatbot', methods=["POST","GET"])
def chatbot():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Missing 'message' in request body"}), 400

    user_message = data['message']
    if not isinstance(user_message, str) or not user_message.strip():
        return jsonify({"error": "'message' must be a non-empty string"}), 400
    bot_reply = get_chatbot_response(user_message,chat_history)
    # Dummy chatbot logic — echo back the message with some prefix
   # bot_reply = f"You said: {user_message}. This is a demo response."

    # TODO: Replace the above with your AI/chatbot logic

    return jsonify({"reply": bot_reply})




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
