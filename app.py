from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import get_db_connection

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'  # Change this in production

# Initialize variables
name = ""
registration_number = ""
course = ""
edit_id = None
message = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page - displays form and student list"""
    global name, registration_number, course, edit_id, message
    
    # Handle delete
    delete_id = request.args.get('delete')
    if delete_id:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE student_id = %s", (delete_id,))
            conn.commit()
            cursor.close()
            conn.close()
            flash("Student record deleted successfully.", "success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Error deleting record: {str(e)}", "error")
            return redirect(url_for('index'))
    
    # Initialize form fields (will be overridden if editing or posting)
    if request.method == 'GET':
        name = ""
        registration_number = ""
        course = ""
        edit_id = None
    
    # Handle edit (fetch existing data)
    edit_id_param = request.args.get('edit')
    if edit_id_param:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT student_id, name, registration_number, course FROM students WHERE student_id = %s", (edit_id_param,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if row:
                edit_id = row[0]
                name = row[1]
                registration_number = row[2]
                course = row[3]
            else:
                edit_id = None
                name = ""
                registration_number = ""
                course = ""
        except Exception as e:
            flash(f"Error fetching record: {str(e)}", "error")
            edit_id = None
            name = ""
            registration_number = ""
            course = ""
    
    # Handle form submission (add or update)
    if request.method == 'POST':
        print("POST request received!")
        print(f"Form data: {request.form}")
        name = request.form.get('name', '').strip()
        registration_number = request.form.get('registration_number', '').strip()
        course = request.form.get('course', '').strip()
        edit_id = request.form.get('student_id', '').strip()
        
        print(f"Parsed values - name: '{name}', reg: '{registration_number}', course: '{course}', edit_id: '{edit_id}'")
        
        if not edit_id:
            edit_id = None
        
        if not name or not registration_number or not course:
            flash("Please fill in all fields.", "error")
            print("Validation failed - empty fields")
        else:
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                
                if edit_id:
                    # Update existing record
                    cursor.execute(
                        "UPDATE students SET name = %s, registration_number = %s, course = %s WHERE student_id = %s",
                        (name, registration_number, course, edit_id)
                    )
                    conn.commit()
                    flash("Student record updated successfully.", "success")
                else:
                    # Insert new record
                    cursor.execute(
                        "INSERT INTO students (name, registration_number, course) VALUES (%s, %s, %s)",
                        (name, registration_number, course)
                    )
                    conn.commit()
                    flash("Student added successfully.", "success")
                    # Reset form fields
                    name = ""
                    registration_number = ""
                    course = ""
                    edit_id = None
                
                cursor.close()
                conn.close()
                return redirect(url_for('index'))
            except Exception as e:
                flash(f"Error saving record: {str(e)}", "error")
                import traceback
                print("Error details:", traceback.format_exc())
                # Don't redirect on error - continue to render page with form data preserved
    
    # Fetch all students
    students = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT student_id, name, registration_number, course FROM students ORDER BY student_id DESC")
        students = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Convert tuples to dictionaries for easier template rendering
        students_list = []
        for student in students:
            students_list.append({
                'student_id': student[0],
                'name': student[1],
                'registration_number': student[2],
                'course': student[3]
            })
        students = students_list
    except Exception as e:
        flash(f"Error fetching students: {str(e)}", "error")
        students = []
    
    return render_template('index.html', 
                         name=name, 
                         registration_number=registration_number, 
                         course=course, 
                         edit_id=edit_id, 
                         students=students)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5500)
