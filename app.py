import psutil       # This is the library we will be working with, for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python
from flask import Flask, render_template, jsonify # our web framework, and render_template is to render our index.html file, jsonify for the json response

app = Flask(__name__)       # this is our app definiftion

@app.route("/")         
def index():            # I am defining the scope of the app
    return render_template('index.html')     # Instead of returning plain text, I am rendering our index.html, which we will create in the templates folder.

@app.route("/metrics") 
def metrics():          # This is my API route, it will give us live data in JSON
    cpu_percent = psutil.cpu_percent()          # This is the metric i want to capture input from, so i allocate variable "cpu_percent" to the function from psutil
    mem_percent = psutil.virtual_memory().percent       # like wise here, i did the same, as these are two metrics i am interested in . I want this in percentage.
    Message = None                                      
    if cpu_percent > 80 or mem_percent > 80:            # This is my conditional block, what I am looking out for, basically it should return something if the values exceed 80%
        Message = "High CPU or Memory Detected, scale up!!"         # THis is the message it should notify me with if that condition is met.
    return jsonify(cpu=cpu_percent, memory=mem_percent, message=Message)     # I am returning the data in JSON so my front end can use it dynamically

if __name__ == '__main__':                  
    app.run(debug=True, host='0.0.0.0')     # I want to be able to view this on this host ip.
