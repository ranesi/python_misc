CAPSTONE PROJECT 4  
===================  
feat. Rich, Alyssa, Natalman
Steps to run:
-------------
1) either install the package (untested!) or:  
2) `pip install flask flask_sqlalchemy foursquare requests googlemaps` (in your venv)  
3) cd to ./Project4/  
4) open the Python interpreter  
5) type `from tables import db`  
6) THEN `db.create_all()`  
7) exit, then set the following:
1. for Windows, `set FLASK_DEBUG=False` and `set FLASK_APP=Project4` *or* `set FLASK_APP=main.py` from capstone_project_4/Project4  
2. for Linux/Mac, `export FLASK_DEBUG=False && export FLASK_APP=Project4` (or main.py)  

8) type `py -m flask run` (Windows) or `python3 -m flask run` (Unix)  
