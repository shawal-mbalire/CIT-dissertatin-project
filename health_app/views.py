from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db,table
import json

views = Blueprint("views", __name__)

# home route
@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    """if request.method == 'POST':
    note = request.form.get('note')

    if len(note) < 1:
        flash('Note is too short!', category='error')
    else:
        new_note = Note(data=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added!', category='success')"""

    return render_template("home.html", user=current_user)


# delete note route
@views.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    # query the note to be deleted
    """note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)"""

    # delete the note
    """
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()"""

    return jsonify({})


# patient dashboard
@views.route("/patient-dashboard", methods=["GET", "POST"])
@login_required
def patient_dashboard():
    return render_template("patient-dashboard.html", user=current_user)


# doctor dashboard
@views.route("/doctor-dashboard", methods=["GET", "POST"])
@login_required
def doctor_dashboard():
    return render_template("doctor-dashboard.html", user=current_user)


# admin dashboard
@views.route("/admin-dashboard", methods=["GET", "POST"])
@login_required
def admin_dashboard():
    return render_template("admin-dashboard.html", user=current_user)

