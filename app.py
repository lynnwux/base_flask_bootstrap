from flask import Flask, render_template, request, redirect, url_for, flash
from flask_cors import CORS
import requests
from requests.auth import HTTPBasicAuth
import json


app = Flask(__name__)
app.secret_key = "supersecretkey" 
CORS(app)


# API credentials
USERNAME = "_SYSTEM"
PASSWORD = "xwu"


# API endpoints
UD_API_URL = "http://localhost:9092/csp/StudentPerformance1/student"
C_API_URL = "http://localhost:9092/csp/StudentPerformance1/newstudent"
R_API_URL= "http://localhost:9092/csp/StudentPerformance1/allstudentperformance"


@app.route("/", methods=["GET"])
def home():
    # Fetch all students for display
    response = requests.get(R_API_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    students = response.json() if response.status_code == 200 else []
    
    return render_template("index.html", students=students)

    
@app.route("/student/<int:id>")
def delete_student(id):
    delete_url = f"{UD_API_URL}?id={id}"
    response = requests.delete(delete_url, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    if response.status_code in [200, 201]:
        flash(f"\U0001F5D1 Student ID {id} deleted successfully!", "success")
    else:
        flash(f"Error: {response.text}", "danger")
    
    return redirect(url_for("home")) 
    
@app.route("/modify", methods=["GET", "POST"])
def modify_student():
    student_id = request.args.get("ID")  
    if not student_id:
        flash("⚠️ No Student ID provided.", "warning")
        return redirect(url_for("home"))

    try:
        response = requests.get(
            f"http://localhost:9092/csp/StudentPerformance1/student?id={student_id}",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
        )
        response.raise_for_status()
        student_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching student data: {e}")  # ✅ Debugging log
        flash(f"❌ Could not fetch Student ID {student_id}: {e}", "danger")
        return redirect(url_for("home"))

    if request.method == "POST":
        updated_data = {
            "Name": request.form.get("name"),
            "School": request.form.get("school"),
            "LowIncome": request.form.get("low_income"),
            "Disability": request.form.get("disability"),
            "MCASELA": request.form.get("mcas_ela"),
            "MCASMath": request.form.get("mcas_math"),
        }

        # Send PUT request to update student data
        response = requests.put(
            f"http://localhost:9092/csp/StudentPerformance1/student?id={student_id}",
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"},
            json=updated_data,
        )

        if updated_data and response.status_code in [200, 201]:
            flash(f"🔄 Student ID {student_id} record updated successfully!", "success")
        else:
            flash(f"No changes detected in the student record. Error: {response.text}", "danger")

        return redirect(url_for("home"))

    return render_template("modify.html", student=student_data)

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        student_data = {
            "Name": request.form.get("name"),
            "School": request.form.get("school"),
            "LowIncome": request.form.get("low_income"),
            "Disability": request.form.get("disability"),
            "MCASELA": request.form.get("mcas_ela"),
            "MCASMath": request.form.get("mcas_math"),
        }

        try:
            response = requests.post(
                C_API_URL,
                auth=HTTPBasicAuth(USERNAME, PASSWORD),
                headers={"Content-Type": "application/json"},
                json=student_data,
                allow_redirects=False
            )

            if response.status_code in [200, 201]:
                flash("➕ New student added successfully!", "success")
                return redirect(url_for("home"))
            else:
                flash(f"❌ Failed to add student. Error: {response.text}", "danger")

        except requests.exceptions.RequestException as e:
            flash(f"❌ Error: {str(e)}", "danger")

    return render_template("add_student.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
