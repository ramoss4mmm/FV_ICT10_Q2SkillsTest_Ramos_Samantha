from pyscript import document, display
from js import alert
#function  ran when button is clicked
def clubgen(e):
    selected = document.getElementById("clubs1").value #gets the club you choose from the dropdown form
    if not selected or selected == "Select a Club...": #gives an alert to the user to remind them to select a club to prevent empty outputs
        alert("Please select a club first.")   
        return

    info = clubs[selected] #accesses the information(dictionary) of the club 
    #shows the information neatly
    information = f"""
    Club: {selected}
    Moderator: {info['Moderator']}
    Meeting Time: {info['Time']}
    Location: {info['Location']}
    Members: {info['Members']}
    """
    #displays the f-string in the div
    document.getElementById("clubinfo").innerText = information
#dictionary containing all the club information
#number of members were random as it was not given in the guidelines
clubs = {
    
    "Math Club": {
        "Moderator": "Mr. Nicole Gabuya",
        "Time": "Monday 02:30 - 03:00 PM",
        "Location": "Room 404",
        "Members": 25
    },
    "Science Club": {
        "Moderator": "Ms. Jameelyn Maramag",
        "Time": "Tuesday 03:00 - 04:00 PM",
        "Location": "Room 404",
        "Members": 28
    },
    "Communications Arts Club": {
        "Moderator": "Ms. Yannis Fernandez",
        "Time": "Wed & Fri 03:00 - 04:00 PM",
        "Location": "Room 406",
        "Members": 20
    },
    "Social Science Club": {
        "Moderator": "Mr. Roberto Lim",
        "Time": "Tuesday 03:00 - 04:00 PM",
        "Location": "Room 409",
        "Members": 22
    },
    "Cadet Officer Candidate Course": {
        "Moderator": "SSgt. Jemima David PA (Res)",
        "Time": "Wednesday 02:30 - 04:30 PM",
        "Location": "Quadrangle / Teatro Preciosa",
        "Members": 50
    },
    "Volleyball Varsity": {
        "Moderator": "Mr. Adrian Ruiz",
        "Time": "Wednesday 03:00 - 04:00 PM",
        "Location": "Quadrangle",
        "Members": 18
    },
    "Basketball Varsity": {
        "Moderator": "Mr. Adrian Ruiz",
        "Time": "Monday 03:00 - 04:00 PM",
        "Location": "Quadrangle",
        "Members": 20
    },
    "Marching Band": {
        "Moderator": "Mr. Emilio Alumno",
        "Time": "Tuesday & Wednesday 03:00 - 4:30 PM",
        "Location": "Band Room",
        "Members": 40
    },
    "Glee Club": {
        "Moderator": "Mr. Denver Martin",
        "Time": "Monday 03:00 - 05:00 PM",
        "Location": "High School Music Room",
        "Members": 30
    },
    "Dance Club": {
        "Moderator": "Mr. Alfred Cases",
        "Time": "Tuesday 03:00 - 05:00 PM",
        "Location": "Teatro Preciosa",
        "Members": 35
    },
}

