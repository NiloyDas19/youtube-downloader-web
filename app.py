from flask import Flask, request, render_template, send_file
from pytubefix import YouTube
from pytubefix.cli import on_progress
import tempfile
import re
import os

app = Flask(__name__)

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
            stream = yt.streams.filter(progressive=True, file_extension="mp4") \
                               .order_by("resolution").desc().first()
            
            safe_title = sanitizeFilename(yt.title)
            
            # Temporary file
            tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
            tmp_file.close()  # Close so pytubefix can write to it
            
            # Download into temp file
            stream.download(output_path=os.path.dirname(tmp_file.name),
                            filename=os.path.basename(tmp_file.name))
            
            # Send file to browser
            response = send_file(tmp_file.name, as_attachment=True,
                                 download_name=f"{safe_title}.mp4")
            
            # Delete after download
            @response.call_on_close
            def remove_temp_file():
                try:
                    os.remove(tmp_file.name)
                except Exception as e:
                    print(f"Error deleting temp file: {e}")
            
            return response
        except Exception as e:
            return f"Error: {str(e)}"
    
    return render_template("index.html")


if __name__ == "__main__":
    # Run the Flask server locally on port 5000
    app.run(debug=True)
