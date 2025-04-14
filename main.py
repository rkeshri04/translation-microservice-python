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
        # Directly await the asynchronous translate function
        translation = await translator.translate(text, src=src, dest=dest)
        # Log more details from the translation object
        print(f"Translation result: text='{translation.text}', detected_src='{translation.src}', origin='{translation.origin}'")
        return jsonify({
            'text': translation.text,
            'detected_source_language': translation.src  # Add detected source language to response
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8002)