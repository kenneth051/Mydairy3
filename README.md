[![Build Status](https://travis-ci.org/kenneth051/Mydairy3.svg?branch=develop)](https://travis-ci.org/kenneth051/Mydairy3)

[![Coverage Status](https://coveralls.io/repos/github/kenneth051/Mydairy3/badge.svg?branch=develop)](https://coveralls.io/github/kenneth051/Mydairy3?branch=develop)

<a href="https://codeclimate.com/github/kenneth051/Mydairy3/maintainability"><img src="https://api.codeclimate.com/v1/badges/71e2fe5f21796ab00102/maintainability" /></a>

# PROJECT TITLE

**Mydairy3**

Is a Diary website where users register, login and then start noting down their daily activities, personal feelings that are saved in a database.

# GETTING STARTED

These instructions will enable you to run the project

**Prerequisites**

Below are the things you need to get the project up and running.

git : To update and clone the repository

python3: Language used to develop the api

pip: A python package used to install modules specified in the requirements text file.


**Clone the repository to your computer**

     git clone https://github.com/kenneth051/Mydairy3.git 

-  Install the dependencies

    
         pip install -r requirements.txt
    
    
    
-  Install postgres SQL on your computer.In the sql shell

       CREATE DATABASE test_db;
    
       CREATE DATABASE diary;    
    
-  Run the application when you are in it's parent directory

       python run.py
       
 **Testing**

To run tests
*in project's root directory*

    pytest

    pytest --cov  (pytest with coverage)

**MY DIARY'S ENDPOINTS**

		METHOD             ACTIVITY                     ENDPOINT
		-POST             registering a user            /API/v1/auth/users/signup
		
		-POST             logging in                    /API/v1/auth/users/login

		-GET             fetching all entries           /API/v1/entries

		-POST            Creating an entry              /API/v1/entries

		-GET             Fething a specific entry       /API/v1/entries/<int:entryid>

		-PUT             Updating a specific entry      /API/v1/entries/<int:entryid>

-  When creating a user

			     {
				"firstname":"dumba",
				"lastname":"kenneth",
				"username":"kenneth051",
				"password":"123456",
				"gender":"male"
						}

-  when creating and updating an entry 

                         { "title":"This is it",
		          "body":"WHY u gotta go"
						 }
**Authors**
Dumba Kenneth					 
						 
**Acknowledgments**

Desire to make a difference in allowing people access a diary on an device at any time
 
