from flask import Flask, render_template, request, redirect
import json, os

# Flask App
template_dir = os.path.abspath("./templates")
app = Flask(__name__, template_folder = template_dir)

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
    
    return render_template("index.html", events = events)

@app.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == 'POST':
        with open(EVENTS_DB, "r") as file:
            events = json.load(file)
            
        new_event = Event(
            event_id = len(events) + 1,
            name = request.form["name"],
            location = request.form["location"],
            date = request.form["date"],
            time = request.form["time"],
            guests = request.form["guests"].split(",")
        )
        
        events.append(new_event.__dict__)
        
        with open(EVENTS_DB, 'w') as file:
            json.dump(events, file, indent=4)
        
    return render_template("add_event.html")

@app.route("/edit/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    with open(EVENTS_DB, "r") as file:
        events = json.load(file)
        
    modify_event = None
    for event in events:
        if int(event["ID"]) == event_id:
            modify_event = event
            break
        
    if request.method == 'POST':    
        modify_event["Name"] = request.form["name"]
        modify_event["Location"] = request.form["location"]
        modify_event["Date"] = request.form["date"]
        modify_event["Time"] = request.form["time"]
        modify_event["Guests"] = request.form["guests"].split(",")

        with open(EVENTS_DB, 'w') as file:
            json.dump(events, file, indent=4)
        
    return render_template("edit_event.html", event = modify_event)

if __name__ == "__main__":
    app.run(debug=True)