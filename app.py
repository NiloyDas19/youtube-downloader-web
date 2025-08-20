from flask import Flask, request, render_template, send_file
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import re

# Flask app
app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# Function to sanitize filenames (Windows safe)
def sanitizeFilename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            return "Please enter a YouTube URL!"
        
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            # Get highest progressive 720p MP4 (video + audio)
            stream = yt.streams.filter(progressive=True, file_extension="mp4") \
                               .order_by("resolution").desc().first()
            
            safe_title = sanitizeFilename(yt.title)
            filepath = os.path.join(DOWNLOAD_FOLDER, f"{safe_title}.mp4")
            
            # Download temporarily to server
            stream.download(output_path=DOWNLOAD_FOLDER, filename=f"{safe_title}.mp4")
            
            # Send to browser with Save As dialog
            response = send_file(filepath, as_attachment=True, download_name=f"{safe_title}.mp4")
            
            return response
        except Exception as e:
            return f"Error: {str(e)}"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
