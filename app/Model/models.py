from app import db
from enum import unique
from datetime import datetime
from werkzeug.security import generate_password_hash, generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from sqlalchemy import Date


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    happiness_level = db.Column(db.Integer, default = 3)

class Student(UserMixin, db.Model):
    permissions = db.Column(db.Boolean, default = 0)
    username = db.Column(db.String(64)) # I may want to add unique=True, I'm not sure if I want to assume they're going to use their WSU email
    passwordHash = db.Column(db.String(64), unique = True, index = True)
    # --- Contact information ---
    firstName = db.Column(db.String(128), default = "Butchy") 
    lastName = db.Column(db.String(128), default = "Boi")
    address = db.Column(db.String(256))
    email = db.Column(db.String(120), unique = True, index = True) # The requirements document didn't specify if this had to be their WSU email
    phoneNumber = db.Column(db.String(32)) # Made it len of 32 because theres no way someone has a phone number that long
    #----------------------------
    major = db.Column( db.String(64)) # One to many relationship?
    cumGPA = db.Column(db.Integer)
    expectedGraduationDate = db.Column(db.String(64)) # May want to change this to an actual date type
    technicalCourses = db.Column( db.String(64))
    technicalCourseGPA = db.Column(db.Float) # Should round this
    researchFields = db.Column( db.String(64))  # One to many relationship?
    programLang = db.Coumn(db.String(64)) # One to many relationship?
    experienceDescription = db.Column(db.String(500)) # Research Experience Description

class Faculty(UserMixin, db.Model):
    permissions = db.Column(db.Boolean, default = 1) 
    username = db.Column(db.String(64)) 
    # --- Contact information ---
    firstName = db.Column(db.String(128)) 
    lastName = db.Column(db.String(128))
    address = db.Column(db.String(256))
    email = db.Column(db.String(120), unique = True, index = True) # The requirements document didn't specify if this had to be their WSU email
    phoneNumber = db.Column(db.String(32)) # Made it len of 32 because theres no way someone has a phone number that long
    #----------------------------


class researchPos(db.Model):
    title  = db.Column(db.String(64))
    researchDesc = db.Column(db.String(500))
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date)
    requiredHours = db.Column(db.Integer)
    researchFields = db.Column(db.String(64))
    requiredQualifications = db.Column(db.String(250))





