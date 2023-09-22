from flask import Flask, render_template, request, jsonify
from flask import request
from datetime import datetime

app = Flask(__name__)

# Create a list to store messages with their sender IPs and timestamps
messages = []

@app.route('/')
def index():
    # Sort the messages by timestamp
    sorted_messages = sorted(messages, key=lambda x: x['timestamp'])
    return render_template('index.html', messages=sorted_messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message_content = request.form.get('message')
    if message_content:
        # Get the sender's IP address from the request
        sender_ip = request.remote_addr

        # Get the current timestamp
        timestamp = datetime.now().strftime('%H:%M')

        # Create a dictionary to store the message data
        message_data = {
            'ip': sender_ip,
            'time': timestamp,
            'message': message_content,
            'timestamp': datetime.now()
        }

        # Add the message data to the list of messages
        messages.append(message_data)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
