# YouTube Downloader Web App (Educational Purpose)

This is a **YouTube video downloader web app** built using **Flask** and **Pytubefix**. It allows users to download **720p MP4 videos with audio** directly from YouTube for **educational and testing purposes** only.  

> ⚠️ **Important:** This project is strictly for learning, testing, and educational purposes. Only download videos you **have permission** to use. Do not violate YouTube’s Terms of Service or copyright laws.

---

## Features

- Simple and **responsive single-page web interface**  
- Supports downloading **720p MP4 videos**  
- **Temporary download files** – automatically deleted after sending to the user  
- **Gorgeous, professional UI** with Tailwind CSS  
- Works locally or deployed on **Render.com** or similar free hosting  
- Educational focus: Learn Flask, Python web deployment, and Pytubefix usage  

---

## How It Works

1. User enters a **YouTube video URL** in the input box.  
2. The app uses **Pytubefix** to fetch the **highest progressive MP4 video** (720p).  
3. The video is downloaded **temporarily** to the server.  
4. The user is prompted with a **Save As dialog** to select a location.  
5. The temporary file is **automatically deleted** after the download completes.  

---

## Tech Stack

- **Backend:** Python, Flask  
- **Downloader:** Pytubefix (YouTube video handling)  
- **Frontend:** HTML, Tailwind CSS  
- **Deployment:** Render.com / Railway / Any Python-supported hosting  
- **Server-side video management:** Temporary files via Python `tempfile`  

---

## Installation & Run Locally

1. Clone the repository:
```bash
git clone https://github.com/NiloyDas19/youtube-downloader-web.git
cd youtube-downloader-web
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Disclaimer

* This project is for **educational and testing purposes only**.
* **Do not** use this app to download copyrighted content without permission.
* Free hosting IPs may be rate-limited by YouTube (HTTP 429).

---
