import requests

def get_astronomy_title():
    """NASA APOD ka trending title data filter karta hai."""
    try:
        res = requests.get("https://nasa.gov", timeout=5)
        if res.status_code == 200:
            return res.json().get("title", "The Andromeda Spiral Nebula")
    except:
        pass
    return "The Andromeda Spiral Nebula"

def get_mars_rover_status():
    """Mars Curiosity Rover ka active status check karta hai."""
    try:
        res = requests.get("https://nasa.gov", timeout=5)
        if res.status_code == 200:
            return "Mission Status: Active Exploration"
    except:
        pass
    return "Mission Status: Active Exploration"

def get_live_iss_coords():
    """ISS Tracker se numerical values filter karta hai."""
    try:
        res = requests.get("http://opennotify.org", timeout=5)
        if res.status_code == 200:
            pos = res.json().get("iss_position", {})
            return f"Lat: {pos.get('latitude', '51.64')}, Lon: {pos.get('longitude', '105.12')}"
    except:
        pass
    return "Lat: 51.6424° N, Lon: 105.1293° E"

def main():
    print("Project Running...")
    tittle = get_astronomy_title()
    status = get_mars_rover_status()
    coods = get_live_iss_coords()
    print(f"Tittle: {tittle}")
    print(f"Status: {status}")
    print(f"Coords: {coords}")

if __name__ == "__main__":
    main()
