

# 🏠 Bangalore House Price Prediction

This project is a **machine learning-based web app** that predicts house prices in Bangalore based on:
- Total Square Feet
- Number of Bedrooms (BHK)
- Number of Bathrooms
- Location  

It also features an **interactive map** where users can visualize the selected location.

---

## 🚀 Features
- Predicts estimated house price (in Lakh ₹).
- Clean, modern **glassmorphism UI** with interactive **OpenStreetMap** map background.
- Fetches & pins selected locations on the map.
- Fully responsive and fast.

---

## 📊 Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap, Leaflet.js, jQuery
- **ML Model:** Trained Linear Regression Model (Pickle)
- **API:** RESTful API with Flask


## 📂 Folder Structure

```
Bangalore-House-Price-Prediction/
│
├── static/                 # Static files (CSS, JS, Images)
├── templates/              # HTML Templates (Jinja2)
├── server.py               # Flask App with API
├── model.pkl               # Trained ML Model
├── .gitignore              # Git Ignore File
├── README.md               # Project Documentation
└── requirements.txt        # Python Dependencies
```


---

## 🛠️ Setup & Run Locally

### 1️⃣ Clone Repo
```bash
git clone https://github.com/Mohamed9786/Bangalore-House-Price-Prediction.git
cd Bangalore-House-Price-Prediction
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run App

```bash
python server.py
```

Open browser at:

```
http://127.0.0.1:5000/
```

---

## 🌐 Live Demo (Optional)

> *Add your deployed link here if available.*

---

## 📷 Screenshots (Optional)

![App Screenshot](https://github.com/Mohamed9786/Bangalore-House-Price-Prediction/blob/main/client/Screenshot.png?raw=true)

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

* Dataset sourced from Kaggle & other real estate resources.
* Built with ❤️ by [Mohamed Ali](https://github.com/Mohamed9786)

---

## 💡 Future Improvements

* Add user authentication.
* Support CSV file upload for bulk predictions.
* Improve mobile responsiveness.
* Deploy on cloud platforms (Render, Vercel, Heroku, etc.)




