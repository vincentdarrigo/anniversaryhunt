# Anniversary Scavenger Hunt 🌍💖

A custom-built scavenger hunt game made with Flask, Leaflet, and a sprinkle of Billy Joel magic 🎶.

---

## 🛠 Tech Stack:
- **Flask** (Python backend)
- **Leaflet.js** (interactive maps)
- **HTML/CSS/JavaScript**
- **Hosted**: Render.com
- **Version Control**: Git/GitHub

---

## 📁 Project Structure:
```
/static
    /media
        (All images, videos, mp3s)
    style.css (optional extra CSS)
/templates
    index.html
    map.html
Anniversary.csv (clues and dummy data)
app.py
requirements.txt
README.md (this file)
```

---

## 🚀 Running Locally:

1. **Clone this repo:**
    ```
    git clone https://github.com/vincentdarrigo/anniversaryhunt.git
    cd anniversaryhunt
    ```

2. **Create a virtual environment (optional but recommended):**
    ```
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    .\venv\Scripts\activate  # Windows
    ```

3. **Install the required packages:**
    ```
    pip install -r requirements.txt
    ```

4. **Run the app:**
    ```
    python app.py
    ```

5. Open your browser at **http://localhost:5000**

---

## 🌐 Deployment (example config used for Render.com):

- **Environment:**
  - Runtime: Python 3.11
  - Build Command: *Leave Blank*
  - Start Command: 
    ```
    gunicorn app:app
    ```
- **Free Plan Settings:**
  - Allow free instance spin down (expected)
  - No persistent disk needed
  - No scaling needed

---

## 🧹 Git Ignore Settings:
In your `.gitignore` file:
```
__pycache__/
*.pyc
.env
```

---

## 📚 Extra Notes:
- **Billy Joel music** auto plays and shuffles through a 31-song playlist.
- **Flight of the Conchords videos** can appear randomly on dummy markers.
- **Swimbim mini-game** QR code included on sidebar.
- **Final Clue unlocks a bonus map and a Cat Island video!**

---

## ✨ Special Thanks
- Built with love for a very special anniversary gift ❤️
