from quart import Quart, request, jsonify
from googletrans import Translator

app = Quart(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
async def translate():
    data = await request.json
    text = data.get('text')
    src = data.get('src', 'auto')  # Default source language is auto-detect
    dest = request.headers.get('Destination-Language', 'en')  # Default destination language is English
    print(f"Translating from {src} to {dest} for text: {text}")
    if not text:
        return jsonify({'error': 'Text to translate is required'}), 400

    try:
        translation = await translator.translate(text, src=src, dest=dest)
        return jsonify({
            'text': translation.text,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8002)