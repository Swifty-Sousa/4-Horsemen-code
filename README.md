This project was created by Robert Specht and Christian Sousa in order to aid the event programs specifically through the Honors College at CU Boulder. 
The current system used to log student information is inefficient and impractical. 
Through this upgraded system, students are more easily tracked when they attend events.
Additionally, students have access to their event history and are suggested future events based on recommendations created by the system.
  HTML:
    This is actually contained in the NodeJS folder. It was uplaoded first seperately for others to work on and view. It contains all the HTML pages for the login, mainpage, events and profile. 
  NodeJS:
  This folder is the meat of this program. It contains the views(HTML files for the pages.) Along with
the front end and back end javascript. Along with the queries in the DAL folder inside NODEJS.
This folder also holds the information for login. Mainly in the middleware. Then holds the server connection for each page through the routes folder. Then the SQL folder just holds example sql code. Lastly, sequelize folder connects
the database. (Run the program in this foulder).

Directions: 
1) Download pgAdmin this will be the database.Enter the password then look for the
database called der1qqcar9k6mv.

2)Move to the NodeJS file once you havedownloaded the entire repository.Enter the command Node app.js

3)Enter localserver/3000/local into the url

4)Login as any of the 3 users. There info is inside the google docs.

5)Look at the main page and click on the events tab.

6)These events are updated based on the user preference.

7)This holds true for the past events and suggested events.
(Change the user and watch the events change)

8)Last feature is click on the profile tab and view the info for that specific user

9)This changes based on the user and is updated from the database

10)Click on the logout button. This will logout the user and take you back into the login main page


This repo is the source of all code for our project, the project hieirachy is as follows:

Pie-1-Swiper:
  this is the gui program for taking in student data to signify a student has attended an event. Under the "final folder 
is where the program files are held. In this folder there are two files, gui.py and logic.py. When running the gui only the gui.py 
file needs to be ran, the logical funcions will be pulled in automatically. The files can be run by opening a terminal shell, 
navigating to the folder and typing "python3 gui.py". The file dependancies are python3 and the Tkinter library which usually comes 
standard with python3 builds.
