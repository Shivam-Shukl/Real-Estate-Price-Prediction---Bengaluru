# 🏡 House Price Predictor - Flask Web App

This is a simple machine learning web application that predicts house prices in Bangalore based on user input like location, square footage, number of BHKs, and more. It uses a Ridge Regression model trained on cleaned housing data and is deployed using Flask on Render.

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
   git clone https://github.com/your-username/house-price-predictor.git
   cd house-price-predictor

```

---

## 🛠 Tech Stack

| Component      | Technology       |
|----------------|------------------|
| Bot Platform   | Telegram (via Dialogflow integration) |
| Backend        | Python + Flask   |
| Webhook Server | Render           |
| Data Source    | [Open Trivia DB](https://opentdb.com/api_config.php) |
| Bot Logic      | Dialogflow CX/ES |

---

## 🚀 Setup & Deployment

### 1 Clone the Repository
```bash
git clone https://github.com/yourusername/Tech_questions_Bot.git
cd Tech_questions_Bot
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `main.py` with this code

```bash
python app.py
```

---
Visit: http://localhost:5000
### 4. Deploy on Render

#### Option A: Manual Deploy

- Login to Render
- Click "New Web Service" → Connect to this repo
- Use:
   - Build Command: pip install -r requirements.txt
   - Start Command: python app.py

#### Option B: Auto Deploy using render.yaml

- Make sure your repo includes the following:

```yaml
# render.yaml
services:
  - type: web
    name: tech-question-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: FLASK_ENV
        value: production

```

---

### 5. Webhook Integration
- Go to Dialogflow Console
- Enable Webhook Fulfillment
- Use your Render-deployed HTTPS URL (e.g. https://your-app.onrender.com/)
- Attach this webhook to your Get_Tech_Question intent
---

### 6.Sample Commands (Telegram)
```text
/start
get me a question
A
Yes
```
---
### 📁 Project Structure

```bash
house-price-predictor/
├── main.py # Flask app
├── Cleaned_data.csv # Input dataset for predictions
├── RidgeModel.pkl # Trained ML model
├── requirements.txt # Python dependencies
└── templates/
└── index.html # Frontend page

```
---
### 🧑‍💻 Author

- #### Shivam Shukla
- Feel free to connect with me on 💼 [LinkedIn](https://www.linkedin.com/in/shivam-shukla-a462b3223/) 


---



