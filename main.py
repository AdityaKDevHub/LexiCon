from flask import Flask, request, jsonify, send_from_directory
import summarizer
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data.get('text', '')
        summary = summarizer.Summarize(text)

        return jsonify({'summary': summary})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
