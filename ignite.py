from openfabric_pysdk.starter import Starter
from flask import Flask, request, jsonify
from bot_logic import BotLogic

app = Flask(__name__)
bot_logic = BotLogic()

@app.route('/execute', methods=['POST'])
def execute():
    try:
        # Get the input text from the request JSON
        data = request.get_json()
        input_text = data['text']

        # Process the input text using your bot logic
        response = bot_logic.generate_response(input_text)

        # Return the bot's response
        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    Starter.ignite(debug=False, host="0.0.0.0", port=5500)


