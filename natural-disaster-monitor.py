from flask import Flask, Pylance, render_template
import requests
import numpy as np
from scipy import stats

app = Flask(__name__)
EONET_BASE = "https://eonet.gsfc.nasa.gov/api/v3"

# Data Access Functionality
## Fetching events
def fetch_events(days=30, category=None, status="open"): 
    params = {"days": days, "status": status}
    if category:
        params["category"] = category
    r = requests.get(f"{EONET_BASE}/events", params=params, timeout=10)
    return r.json().get("events", [])

## Fetching categories
def fetch_categories():
    r = requests.get(f"{EONET_BASE}/categories", timeout=10)
    return r.json().get("categories", [])


def analyze_events(events):


@app.route("/")
def index():
    categories = fetch_categories() # categories: One or more categories assigned to the event.
    return render_template("eonet_index.html", categories=categories)

@app.route("/api/events")
def api_events():

    
    # Format events for map
    mapped = []
    for e in events:
        geo = e.get("geometry", [])
        if geo:
            c = geo[-1].get("coordinates", [])
            if c and isinstance(c[0], (int, float)):
                mapped.append({
                    "id": e["id"],
                    "title": e["title"],
                    "categories": [cat["title"] for cat in e.get("categories", [])],
                    "lon": c[0], "lat": c[1],
                    "date": geo[-1].get("date", "")[:10],
                    "closed": e.get("closed")
                })
    
    return jsonify({"events": mapped, "analysis": analysis, "total_raw": len(events)})

if __name__ == "__main__":
    app.run(port=5000)