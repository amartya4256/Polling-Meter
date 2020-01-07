# Polling-Meter

Contributors : 
1. Amartya Parijat (Flask, JavaScript)
2. Ayushi Batham (Html, Css)
3. Anugrah Bhatt (Html, JavaScript)
4. Apoorv Bhardwaj (Html, Css)
5. Utkarsh Saxena (Adobe Illustrator)

Polling Meter is a Python flask based web app. It is made for a secured implementation of Indian elections made online. We provide security to the polls by insulating the data of user within a time stamp in an offline database. This database can only be accessed by Flask application. The web app has been developed free of any application vulnerability. So, it tricks the attackers and makes it almost impossible for them to get access to the user information.

How does it work: 
First the user enters its ID on the login page. The application fetches the data from login screen by using jinja template that makes the application free of any XSS attacks. When the user clicks on send OTP, the engine generates an otp and sends it to the user's contact number. The otp is then hashed into some certain hashing format and inserted into the database. the database doesn't use any engine of its own and hence is only connected to the flask app by SQLITE3 engine. The database file is protected from being crawled, making it almost invincible.
Once the otp has been hashed and inserted in the database, a time count of 2 minutes starts after whcdich the otp will be automatically deleted from the database. Hence, an attacker is restricted to only 2 minutes to perform any sql injection attack over database to retrieve the hash, but as this application is SQL injection free, it is not possible to attack on the database through it.
Once the user inputs the OTP, it is provided access to the polling page. Once it is logged in, the otp is deleted by engine the moment it logs in. After polling, The user cannot visit the polling page again, to save the poll from biasing. The user is redirected to a "Thank you" page instead. The user can then logout of the application.
The admin section of the application is restrcted to the server itself. So no one else can connect to it remotely. This is another security measure taken to dodge from attacks.

The expertise of this system is only available to Government, as it would require the database of aadhar card to select the citizens elligible for voting and use their data to perform the polling. The system uses OTPs for the user logins and has been tested again and again in different conditions and is assured by our team to be free of any bugs or disorders. Hence, all the manipulations and calculation done by the engine is 100% accurate.
