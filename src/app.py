from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def serve_index():
    index_path = os.path.join("src", "static", "index.html")
    return FileResponse(index_path)

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Sports related activities
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": []
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly games",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    # Artistic activities
    "Art Workshop": {
        "description": "Explore painting, drawing, and sculpture techniques",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": []
    },
    "Drama Club": {
        "description": "Act, direct, and produce school plays and performances",
        "schedule": "Fridays, 3:30 PM - 5:30 PM",
        "max_participants": 20,
        "participants": []
    },
    # Intellectual activities
    "Mathletes": {
        "description": "Solve challenging math problems and compete in contests",
        "schedule": "Thursdays, 4:00 PM - 5:00 PM",
        "max_participants": 16,
        "participants": []
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": []
    }
}

# Example endpoint to get activities
@app.get("/activities")
async def get_activities():
    return activities

# Example endpoint to sign up for an activity
@app.post("/activities/{activity_name}/signup")
async def signup(activity_name: str, email: str):
    activity = activities.get(activity_name)
    if not activity:
        return JSONResponse(status_code=404, content={"detail": "Activity not found"})
    if email in activity["participants"]:
        return JSONResponse(status_code=400, content={"detail": "Already signed up"})
    if len(activity["participants"]) >= activity["max_participants"]:
        return JSONResponse(status_code=400, content={"detail": "Activity is full"})
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
