from flask import Flask
app = Flask(__name__) # creates an instance of the Flask object
@app.route("/") #url routing - the function directly below this should be called whenever a user visits the main root of our web application(which is defined by the single forward slash)
def index():
    return("Hello, World!")
if __name__ == '__main__': # evaluated to True if our application is called directly. Used to prevent Python scripts from being run unintentionally when they are imported into other python files
    app.run(port = 5000, debug = True) # post = 80 for production, debug = T - detailed errorrs in the browser