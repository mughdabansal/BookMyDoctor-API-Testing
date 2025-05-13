
from flask import Flask, request, jsonify

app = Flask(__name__)

users = []
doctors = [
    {"id": 1, "name": "Dr. Smith", "specialization": "Cardiologist"},
    {"id": 2, "name": "Dr. Emma", "specialization": "Dermatologist"},
    {"id": 3, "name": "Dr. John", "specialization": "Neurologist"}
]
appointments = []
reviews = []

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "email": data.get("email"),
        "password": data.get("password")
    }
    users.append(user)
    return jsonify({"message": "User registered", "user": user}), 201

@app.route("/doctors", methods=["GET"])
def get_doctors():
    specialization = request.args.get("specialization")
    if specialization:
        filtered = [d for d in doctors if d["specialization"].lower() == specialization.lower()]
        return jsonify(filtered)
    return jsonify(doctors)

@app.route("/doctor/<int:id>", methods=["GET"])
def get_doctor(id):
    doc = next((d for d in doctors if d["id"] == id), None)
    return jsonify(doc if doc else {"message": "Doctor not found"}), 200 if doc else 404

@app.route("/appointments", methods=["POST"])
def book_appointment():
    data = request.get_json()
    appointment = {
        "id": len(appointments) + 1,
        "user_id": data.get("user_id"),
        "doctor_id": data.get("doctor_id"),
        "date": data.get("date"),
        "time_slot": data.get("time_slot")
    }
    appointments.append(appointment)
    return jsonify({"message": "Appointment booked", "appointment": appointment}), 201

@app.route("/appointments/<int:user_id>", methods=["GET"])
def get_appointments(user_id):
    user_appointments = [a for a in appointments if a["user_id"] == user_id]
    return jsonify(user_appointments)

@app.route("/appointments/<int:id>", methods=["DELETE"])
def cancel_appointment(id):
    global appointments
    appointments = [a for a in appointments if a["id"] != id]
    return jsonify({"message": "Appointment cancelled"})

@app.route("/reviews", methods=["POST"])
def submit_review():
    data = request.get_json()
    review = {
        "id": len(reviews) + 1,
        "user_id": data.get("user_id"),
        "doctor_id": data.get("doctor_id"),
        "rating": data.get("rating"),
        "comment": data.get("comment")
    }
    reviews.append(review)
    return jsonify({"message": "Review submitted", "review": review}), 201

@app.route("/reviews/doctor/<int:doctor_id>", methods=["GET"])
def get_reviews(doctor_id):
    doc_reviews = [r for r in reviews if r["doctor_id"] == doctor_id]
    return jsonify(doc_reviews)

if __name__ == "__main__":
    app.run(debug=True)
