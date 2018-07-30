# Mydairy3
challenge3
FEATURES OF MYDIARY

		-Creating an account

		-logging into the account

		-Entering content(Writitng)

		-Viewing all entries

		-Viewing a specific entry

		-Updating an entry
MY DIARY'S ENDPOINTS

		METHOD             ACTIVITY                     ENDPOINT
		-POST             registering a user            /API/v1/auth/users/signup
		
		-POST             logging in                    /API/v1/auth/users/login

		-GET             fetching all entries           /API/v1/entries

		-POST            Creating an entry              /API/v1/entries

		-GET             Fething a specific entry       /API/v1/entries/<int:entryid>

		-PUT             Updating a specific entry      /API/v1/entries/<int:entryid>
		
GETTING STARTED WITH MY DIARY
1- Clone the repository to your computer

-git clone https://github.com/kenneth051/Mydairy3.git 
 
 2-Install a virtual enviroment
 
			-pip install virtaulenv
			-in the projects root directory, create a virtual enviroment
			-virtualenv "Name of virtaulenv here without the qoutes"
			-activate the virtual env, in your project's root directory

		-on windows
			"virtual_env_folder_name_here"\Scripts\activate
        -on a mac
            source bin/activate

3-Install the dependencies in your virtual enviroment

		    -pip install -r requirements.txt

4- Install postgres SQL on your computer.In the sql shell
                    -*create databases*
		         -create database test_db;
			 -create database diary;

4-Run the application when you are in it's parent directory

		    -python run.py

**Testing**

To run tests
#in root directory

            -pytest

            -pytest --cov  (pytest with coverage)


 The endpoints have been developed Using Python OOP based together with Flask framework implementing non persistent data using data structures for storage.
 
