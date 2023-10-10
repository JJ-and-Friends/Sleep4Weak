from flask import Blueprint, render_template, jsonify, request, send_from_directory, Flask, redirect, url_for


from App.controllers import (
    add_student,
    get_student_by_id,
    get_students_by_name,
    get_all_students,
    update_student,
    delete_student,
    update_karma
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')

@student_views.route('/student/add-student/<string:sname>/<string:degree>/<int:year>/<int:karma>', methods=['POST'])
def add_student_route(sname, degree, year, karma):
    try:
        # Get JSON data from the request
        data = request.get_json()
        # Call the controller function to add a student
        success, message = add_student(sname, degree, year, karma)
        if success:
            return jsonify({'message': message}), 201  # 201 Created status code for successful addition
        else:
            return jsonify({'error': message}), 400  # 400 Bad Request status code for errors

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error for unexpected exceptions

# Get a student by ID via GET request
@student_views.route('/student/<int:sid>', methods=['GET'])
def get_student_by_id_route(sid):
    try:
        # Call the controller function to get a student by ID
        student = get_student_by_id(sid)
        #return student
        if student:
            # Convert the student object to a dictionary
            student_dict = {
                'studentName': student.studentName,
                'degree': student.degree,
                'year': student.year,
                'karma': student.karma
            }
            return jsonify(student_dict), 200  # 200 OK status code for successful retrieval
        else:
            return jsonify({'error': 'Student not found'}), 404  # 404 Not Found status code if student not found

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error for unexpected exceptions
 

@student_views.route('/student/get-students-by-name/<string:studentName>', methods=['GET'])
def get_students_by_name_route(studentName):
    try:
        # Get the 'sname' query parameter from the request
        sname = request.args.get('studentName')
        # Call the controller function to get students by name
        students = get_students_by_name(sname)
        if students:
            # Convert the list of student objects to a list of dictionaries
            students_list = [
                {
                    'studentID': student.studentID,
                    'studentName': student.studentName,
                    'degree': student.degree,
                    'year': student.year,
                    'karma': student.karma
                }
                for student in students
            ]
            return jsonify(students_list), 200  # 200 OK status code for successful retrieval
        else:
            return jsonify({'error': 'No students found with the provided name'}), 404  # 404 Not Found status code if no students found

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error for unexpected exceptions

# Get all students via GET request
@student_views.route('/student/get-all-students', methods=['GET'])
def get_all_students_route():
    try:
        # Call the controller function to get all students
        students = get_all_students()

        if students:
            # Convert the list of student objects to a list of dictionaries
            students_list = [
                {
                    'studentID': student.studentID,
                    'studentName': student.studentName,
                    'degree': student.degree,
                    'year': student.year,
                    'karma': student.karma
                }
                for student in students
            ]
            return jsonify(students_list), 200  # 200 OK status code for successful retrieval
        else:
            return jsonify({'error': 'No students found'}), 404  # 404 Not Found status code if no students found

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error for unexpected exceptions

# Update a student via POST request
@student_views.route('/student/update-student/<int:sid>', methods=['PUT'])
def update_student_route(sid):
    try:
        # Get JSON data from the request
        data = request.get_json()
        # Call the controller function to update a student
        success, message = update_student(sid, data.get('studentName'), data.get('degree'), data.get('year'), data.get('karma'))
        if success:
            return jsonify({'message': message}), 200  # 200 OK status code for successful update
        else:
            return jsonify({'error': message}), 400  # 400 Bad Request status code for errors

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error for unexpected exceptions

@student_views.route('/student/delete-student/<int:sid>', methods=['DELETE'])
def delete_student_route(sid):
    try:
        # Call the controller function to delete a student
        success, message = delete_student(sid)

        if success:
            return jsonify({'message': message}), 200  # 200 OK status code for successful deletion
        else:
            return jsonify({'error': message}), 400  # 400 Bad Request status code for errors

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error for unexpected exceptions

# Update a student's karma via POST request
@student_views.route('/student/update-karma/<int:sid>', methods=['PUT'])
def update_karma_route(sid):
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Call the controller function to update a student's karma
        success, message = update_karma(sid, data.get('karma'), data.get('score'))

        if success:
            return jsonify({'message': message}), 200  # 200 OK status code for successful update
        else:
            return jsonify({'error': message}), 400  # 400 Bad Request status code for errors

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # 500 Internal Server Error for unexpected exceptions