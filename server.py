from flask import Flask, render_template, request, redirect
import json, os

# Flask App
template_dir = os.path.abspath("./templates")
app = Flask(__name__, template_folder=template_dir)

# Events DB
EVENTS_DB = "./db/events.json"

# Events Class
class Event:
    def __init__(self, event_id, name, location, date, time, guests):
        self.ID = event_id
        self.Name = name
        self.Location = location
        self.Date = date
        self.Time = time
        self.Guests = guests
        
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.Name
    
    def getLocation(self):
        return self.Location
    
    def getDate(self):
        return self.Date
    
    def getTime(self):
        return self.Time
    
    def getGuests(self):
        return self.Guests
    
#Root / Path for Index Page at URL http://127.0.0.0:5000/
@app.route("/", methods=["GET"])
def index():
    with open(EVENTS_DB, "r") as file:
        events = json.load(file)
    
    return render_template("index.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)