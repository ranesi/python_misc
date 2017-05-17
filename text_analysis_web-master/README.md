# TEXT ANALYSIS FLASK APPLICATION
HOW DO:  
pip3 install flask nltk textrazor
-python3 interpreter:  
  import nltk  
  nltk.download()  
-search for, install cmudict from the list  
-ensure global flask settings are set (ensure that you've navigated to the application directory):  
  export FLASK_DEBUG=False  
  export FLASK_APP=text_analysis.py  
-execute this command to initialize the database  
  python3 -m flask initdb  
-running the app:  
  python3 -m flask run  
-navigate to localhost:5000  
