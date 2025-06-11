# 🏡 House Price Predictor - Flask Web App

This is a simple machine learning web application that predicts house prices in Bangalore based on user input like location, square footage, number of BHKs, and more. It uses a Ridge Regression model trained on cleaned housing data and is deployed using Flask on Render.

---

## Dateset on Kaggle and Notebook
 - Dataset : 🔗 [bengaluru-house-price-data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)  
### House Price Prediction - ML Notebook

**[This](https://github.com/Shivam-Shukl/Real-Estate-Price-Prediction---Bengaluru/blob/main/Predictor.ipynb) notebook includes the complete ML workflow:**

- Data Loading – Import and explore raw housing data

- Data Cleaning & Preprocessing – Handle missing values, outliers, and encode features

- Model Building – Train a Ridge Regression model for price prediction

- Model Evaluation – Check accuracy using R² score and RMSE

The final model and cleaned dataset are used in the deployed Flask web app.

---

## 🚀 Demo

🔗 [Live App on Render](https://house-price-predictor-jqhi.onrender.com)  

---

## 📸 Screenshots

The working website screenshot.

<img src="https://github.com/user-attachments/assets/cc9c49c7-b380-47c3-bf69-72859f1c0391"/>

<img src="https://github.com/user-attachments/assets/0983c582-91cb-4ece-8357-30142965a788"/>

---

## 📺 Demo Video
- Please click the below image to visit to video.
<a href="https://youtu.be/8xjxoG3V8L8">
  <img src="https://github.com/user-attachments/assets/c2749799-4867-4683-a7e1-e59bb4e0f205" width="1000"/>
</a>

---


## ⚙️ How It Works

1. **User Input** – The user enters data like location, sqft, BHK, etc.
2. **Model Prediction** – A trained Ridge Regression model processes the input.
3. **Output** – The app displays the predicted price of the house.

---

## 📦 Tech Stack

- **Frontend:** HTML, CSS (Bootstrap)
- **Backend:** Python, Flask
- **ML:** Scikit-learn (Ridge Regression)
- **Deployment:** Render
- **Others:** Pandas, NumPy

---

## 🛠️ Setup Instructions (Local)

1. **Clone the repository**
   
```bash
   git clone https://github.com/Shivam-Shukl/Real-Estate-Price-Prediction---Bengaluru.git
   cd Real-Estate-Price-Prediction
```


2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python main.py
```
5. **Visit in browser**

```cpp
http://127.0.0.1:5001
```

#### Option A: Manual Deploy

- Login to Render
- Click "New Web Service" → Connect to this repo
- Use:
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py

#### Option B: Auto Deploy using render.yaml

- Make sure your repo includes the following:

```yaml

services:
  - type: web
    name: any according to your intrest
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
    envVars:
      - key: FLASK_ENV
        value: production

```

---
### 6.Sample Prediction
```text
Input:
Location: Whitefield
Area: 1200 sqft
BHK: 3
Bath: 2

Predicted Price: ₹ 854000 Lakhs
```
---

## 📜 License

This project is open-source and free to use for educational purposes.

---
## 🙌 Acknowledgements

- Scikit-learn
- Render
- Bootstrap

---
### 🧑‍💻 Author

- #### Shivam Shukla
- Feel free to connect with me on 💼 [LinkedIn](https://www.linkedin.com/in/shivam-shukla-a462b3223/) 

---



