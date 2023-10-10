
from flask import Blueprint, render_template, jsonify, request, send_from_directory, Flask, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    add_review,
    list_review_log_json,
)

rate_views = Blueprint('rate_views', __name__, template_folder='../templates')

@rate_views.route('/rate/review/<string:title>/<string:description>', methods=['POST'])
def add_review_route():
    try:
        data = request.get_json()

        success, message = add_review(data.get('studentID'), data.get('userID'), data.get('title'), data.get('description'))

        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'error': message}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500
 

@rate_views.route('/rate/show-rating/<int:id>', methods=['GET'])
def display_data(sID):
    try:
        reviews = Rating.query.filter_by(studentID=sID).all()
        review_data = [review.get_json() for review in reviews]
        return review_data
    except Exception as e:
        return False, str(e)

@rate_views.route('/rate/list-review-log/', methods=['GET'])
def list_review_log_route():
    try:
        reviews = Rating.query.filter_by(studentID=sID).all()
        review_data = [review.get_json() for review in reviews]
        return review_data
    except Exception as e:
        return False, str(e)

