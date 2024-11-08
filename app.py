from flask import Flask, request, send_file, jsonify, render_template
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    pinterest_url = data.get('url')

    ydl_opts = {
        'outtmpl': 'static/downloaded_video.mp4',
        'format': 'bestvideo+bestaudio/best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([pinterest_url])
        return send_file('static/downloaded_video.mp4', as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
