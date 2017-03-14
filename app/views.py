"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os, json, time
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify
from forms import profileForm
from werkzeug.utils import secure_filename
from models import UserProfile

###
# Routing for your application.
###
@app.route('/')
def home():
    """Render profile page"""
    return render_template('profile.html')
def date():
    return time.strftime("%D")
    
@app.route('/profile', methods=['POST', 'GET'])
def profile():
    """Render website's profile page."""

    file_folder = app.config['UPLOAD_FOLDER']
    proform = profileForm()
    if request.method == 'POST':
        # Accept profile details
        username=proform.username.data
        firstname = proform.firstname.data
        lastname = proform.lastname.data
        age = proform.age.data
        biography = proform.biography.data
        gender = proform.gender.data
        file = request.files['file']
        filename = secure_filename(file.filename)
        path = "./app/static/Profilepics/"+ filename
        file.save(path)
        file = path
        user = UserProfile(100,username,firstname,lastname,age,gender,biography,file,date())
        db.session.add(user)
        db.session.commit() 
        return redirect(url_for('profile'))
    else:
        flash('There was an error! lets try again', 'oops')

    return render_template('profile.html', form = proform)
    
@app.route('/profile/<userid>',methods=["GET","POST"])
def viewprof(userid):
    profiles={}
    x=0
    if request.method=='POST':
        user= db.session.query(UserProfile).filter_by(username=userid)
        for i in user:
            prof={'userid':str(user.id),'username':user.username,'age':str(user.age),'firstname':user.firstname, 'lastname':user.lastname, 'gender':user.gender,'biography':user.biography, 'picture':user.filename,'profile_date':user.date_created}
            x+=1
        return jsonify(prof)
    user= db.session.query(UserProfile).filter_by(username=userid)
    return render_template('profileview.html',user=user)

@app.route('/profiles/', methods= ['GET', 'POST'])
def profiles():
    """Render the website's profiles page."""
    user_profile=[]
    p_l=[]
    profiles={}
    x=0
    print request.method
    if request.method=="POST":
        users= db.session.query(UserProfile).all()
        for user in users:
            profiles={'username':user.username,'userid':str(user.id)}
            user_profile.insert(x,profiles)
            x+=1
        p_up={'users':jsonify(user_profile)}
        p_l.insert(0,p_up)
        print x
        return jsonify(user_profile)
    users = db.session.query(UserProfile).all()
    print "ABOVE"
    print users
    
    for user in users:
        user_profile.append((user.firstname, user.username))
        print user.firstname
        print "IN ABOVE"
    return render_template('profiles.html', users=users) 


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
