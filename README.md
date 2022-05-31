# Shorewise Assignment

Answers & Explainations:

Question 1 : Write a code to add the mailing feature in the Flask Application?

Answer:

Files/Folder:- FlaskApp

To complete this Feature, I have created Simple Flask Application which sends one email on running the server.
I have User Flask and Flask-Mail packages.

Please do the changes to Email Properties before running it:-
MAIL_USERNAME - your email
MAIL_PASSWORD - your password

Change the sender and recipients email also.

It will send one email upon running. 
I have attached one screenshot below
![Screenshot from 2022-05-31 16-45-16](https://user-images.githubusercontent.com/106593233/171161352-77f9a7dc-3383-4e5b-a5c4-a1ab05de1ad6.png)

Question 2: What is OpenCV? Give some examples of OpenCV usage.

Answer:

Files/Folder:- opencvsw.py
inputfiles/Folder:- input.png

OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human. When it integrated with various libraries, such as NumPy, python is capable of processing the OpenCV array structure for analysis. To Identify image pattern and its various features we use vector space and perform mathematical operations on these features.

OpenCV Applications:-
1. face recognition
2. Automated inspection and surveillance
3. number of people – count (foot traffic in a mall, etc)
4. Vehicle counting on highways along with their speeds
5. Interactive art installations
6. Anamoly (defect) detection in the manufacturing process (the odd defective products)
7. Street view image stitching
8. Video/image search and retrieval
9. Robot and driver-less car navigation and control
10. object recognition
11. Medical image analysis
12. Movies – 3D structure from motion
13. TV Channels advertisement recognition

Here I have given some examples of Image processing using OpenCV.

Question 3: What is pandas? Write down a code to join two dataframes.

Answer:

Files/Folder:- joinfw.py
inputfiles/folder:- dat

Pandas is a software library written for the Python programming language that is used mainly for data manipulation and analysis.

In a nutshell, Pandas is like excel for Python, with tables (which in pandas are called DataFrames), rows and columns (which in pandas are called Series), and many functionalities that make it an awesome library for processing and data inspection and manipulation. Over these post we will see many of these functionalities.

Pandas relies on Numpy and Matplotlib, two of the other main libraries that should be present in the toolkit of any Data Scientist, and as we will see there are many pandas functions which are naturally derived from them.

Here i have written one Python Program Which takes Two .dat Files and create DataFrame and joins them and print.

.dat files

Data.dat
Data1.dat




Question 4: Write python code to establish connection with any database (SQL/MongoDB).

Answer:

Files/Folder:- dbcon.py

I have written one Python program to establish connection with PosgreSQL database.

Please do changes to the Database connection parameters before running.

Question 5: Create a simple POST API in python using any python framework of your choice
                (Django/Flask), which can do following:-
                
                - Takes name, date of birth and country as input
                - Saves this information in Excel file
                - Returns=&gt; if success =&gt; {“status”:”successful”}
                Else =&gt; {“status”:”failed”}

Answer:

Files/Folder:- djangoapi
output:- data.xlsx
           
I have created one Web App in Django Rest Framework with JWT Authentication. I have implemented one endpoint ("http://127.0.0.1:8000/account/api/insert_data") where you can send data via payload like below:-

![Screenshot from 2022-05-31 17-41-52](https://user-images.githubusercontent.com/106593233/171170346-a9929f8f-464c-4799-9abe-f63adeff91af.png)

After calling the API Excel File Looks like:-

![Screenshot from 2022-05-31 17-45-10](https://user-images.githubusercontent.com/106593233/171170913-cd577585-32f4-415c-8031-034193a92d9e.png)
