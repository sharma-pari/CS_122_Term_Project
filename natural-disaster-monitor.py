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

if __name__ == "__main__":
    app.run(port=5000)