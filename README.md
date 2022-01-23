# Overview

I have written a simple python program that connects to a Firebase Data Base and stores sales data coresponding with accounts in various countries. The program both authenticates the user who is accessing the data as well as provides multiple CRUD statements to add, delete, and read the data from the database.

This software is intended to showcase the connection we can make on a local machine to a cloud database and transfer data. This project is special in that it takes a raw csv file, sorts through it, converts it into JSON format, and then sends it to the database.

Here is a link to a demonstration on how the database is used.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

I am using Firebase for the cloud database for this project. While not using the pages in Firestore, I used Firebase as a simple and fast solution to the non invasive and low maintanaince purpose of my data.

# Development Environment

While primarily focusing the majority of the work in VS code, within my IDE, I used pyrebase to connect to Firebase, csv, json, and time modules to help with accessing the data I was using and timing the process. Finally, I used a getpass module, to help securely use passwords within the program.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [CSV Data](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html)
* [Helpful Key Commands for Firebase](https://github.com/codefirstio/Python-Firebase-Realtime-Database-CRUD-Series/blob/master/createdata.py)

# Future Work

A few things I will improve as the first part of this project nears completion.
* Increased CRUD statements that organize the DB more efficiently.
* More substance to the authentication process