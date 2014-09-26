Introduction to Django
=============================
 
This workshop/tutorial contains 3 different parts

  - Rampup
     - Simple Hello World 
     - Hello World using Templates
  - An Application to Add/List/Remove/Modify favourite movie names
  - Simple To-do application

Each part has corresponding branches to begin with and complete solution.

Part - 0   (Setup)
----
**For Windows 7:**
[Complete Setup Instructions](http://bit.ly/pycon-gswd-windows-setup)

**For GNU/Linux(Ubuntu) :**
[Complete Setup Instructions](http://bit.ly/pycon-gswd-linux-setup)

Part - 1   (Rampup)
---------
**Simple Hello World**
 - Hello World
 - Hello World with HTML tags
 - Hello World with current time
 - Hello World with Given Name (From Query String)

**Hello World using Templates**
 - Simple Hello World
 - Hello World with current time
 - Hello World with Given Name (From Query String)

**Guide**
[Step by Step Instructions](http://bit.ly/pycon-gswd-rampup)

**Branch Details**
 - Scratch space to start: **rampup_base**
 - Complete solution :     **rampup_complete**


Part - 2   (Favourite Movie Catalogue)
----------
It contains 11 steps(iterations) to develop a complete solution from scratch.

**Content**
 - **Step 0:** Create Movie app and register it
 - **Step 1:** Create HTML form for adding Movie Names 
 - **Step 2:** Implement Movie Add feature & Persist in the database with the successful message
 - **Step 3:** Implement messaging in the same page
 - **Step 4:** List all the movies  before Add form
 - **Step 5:** Implement Remove option (using HTTP GET) 
 - **Step 6:** Fix Integrity issues, exceptions, validations
 - **Step 7:** Use Django Forms instead of HTML Forms
 - **Step 8:** Move  validations to Django forms
 - **Step 9:** Implement Delete confirmation (using HTTP POST)
 - **Step 10:** Implement Edit/Modify feature
 - **Step 11:** Enable Admin

 The iteration steps are described in details in this [Gist](http://bit.ly/pycon-gswd-movie-app).

**Branch Details**
 - Scratch space to start: **movie_base**
 - Step 0 Completed :      **movie_00**
 - Step 1 Completed :      **movie_01**
 - Step 2 Completed :      **movie_02**
 - Step 3 Completed :      **movie_03**
 - Step 4 Completed :      **movie_04**
 - Step 5 Completed :      **movie_05**
 - Step 6 Completed :      **movie_06**
 - Step 7 Completed :      **movie_07**
 - Step 8 Completed :      **movie_08**
 - Step 9 Completed :      **movie_09**
 - Step 10 Completed :     **movie_010**
 - Step 11 Completed :     **movie_011**
 - Complete solution :     **movie_complete**

Part - 3   (To-do Application)
---------
**Content**

This To-do application can be implemented by following the steps described Part 2. Each task in todo list will have task name, priority, late_date and completed/done flag.

**Branch Details**

It has only a reference implementation branch called **todo**.

Others
-------
**Server Setup in AWS**
 - Branch : **movie_server_configs**
 - [Guide] (http://bit.ly/pycon-gswd-server-setup)
    
**Sample TDD Application**
 - Branch : **movie_sample_tdd**
 - [Guide] (http://bit.ly/pycon-gswd-tdd)
