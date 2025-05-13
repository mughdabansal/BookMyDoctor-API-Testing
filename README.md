# BookMyDoctor – API Testing with Postman & Newman

🚀 A simple and efficient API testing project for a doctor appointment booking system, built using **Flask** for the backend and tested using **Postman** and **Newman**.

## 📌 Features

- User Registration & Login
- Book, View, and Cancel Appointments
- View Doctor List
- API Testing using Postman
- Automated Reports via Newman (HTML + JSON)

## 🛠️ Tech Stack

- Backend: Python + Flask
- API Testing: Postman
- CLI Test Runner: Newman
- Reports: HTML & JSON via Newman

## 🔁 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/mughdabansal/BookMyDoctor-API-Testing.git
   cd BookMyDoctor-API-Testing
Install Flask (if not already):

bash
Copy
Edit
pip install flask
Run the Flask app:

bash
Copy
Edit
python app.py
Import the collection into Postman or run Newman directly:

bash
Copy
Edit
newman run BookMyDoctor_API_Testing.postman_collection.json \
  --reporters html,json \
  --reporter-html-export reports/report.html \
  --reporter-json-export reports/report.json
📊 Newman Report
You can find generated reports in the reports/ folder:

HTML Report

JSON Report

🧪 Sample API Endpoints
Method	Endpoint	Description
POST	/register	Register new user
POST	/login	Login user
POST	/appointments	Book appointment
GET	/appointments/<id>	View appointments by user
DELETE	/appointments/<id>	Cancel appointment
GET	/doctors	List all doctors

📚 Learnings
Practiced REST API design and testing

Automated test execution using Newman

Learned to generate and share test reports

Integrated Git and GitHub for project version control

🔗 Connect
Feel free to connect or collaborate:

Mughda Bansal
📧 mughdabansal1414@gmail.com
🔗 https://github.com/mughdabansal
