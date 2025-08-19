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
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Deployment on Render.com

1. Push your repository to GitHub.
2. Sign up on [Render.com](https://render.com).
3. Create a **New Web Service** → Connect your GitHub repo.
4. Set **Environment**: Python 3
5. Set **Start Command**:

```bash
gunicorn app:app
```

6. Render builds and deploys your app → you get a public URL.

---

## Disclaimer

* This project is for **educational and testing purposes only**.
* **Do not** use this app to download copyrighted content without permission.
* Free hosting IPs may be rate-limited by YouTube (HTTP 429).

---

## License

MIT License

```

---

If you want, I can also **enhance this README** with **screenshots of your web app** and **demo link instructions** to make it look even more professional for GitHub.  

Do you want me to do that?
```
