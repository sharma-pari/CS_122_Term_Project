from flask import Flask, render_template, jsonify, request
import requests
import numpy as np
from scipy import stats
from collections import Counter
from datetime import datetime

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

# Data Analysis Functionality
def analyze_events(events):
    if not events:
        return {}
    
    cat_counts = Counter()
    monthly = Counter()
    coords = []
    
    for e in events:
        for cat in e.get("categories", []):
            cat_counts[cat["title"]] += 1
        for geo in e.get("geometry", []):
            d = geo.get("date", "")[:7]
            if d:
                monthly[d] += 1
            c = geo.get("coordinates", [])
            if c and isinstance(c[0], (int, float)):
                coords.append(c)
    
    # Trend analysis
    sorted_months = sorted(monthly.items())
    trend = None
    if len(sorted_months) >= 3:
        y = [v for _, v in sorted_months]
        x = list(range(len(y)))
        slope, intercept, r, p, se = stats.linregress(x, y)
        trend = {"slope": round(slope, 3), "r2": round(r**2, 3), "direction": "increasing" if slope > 0 else "decreasing"}
    
    # Geographic clusters
    geo_regions = Counter()
    for lon, lat in coords:
        if lat > 66: geo_regions["Arctic"] += 1
        elif lat > 23: geo_regions["Northern Temperate"] += 1
        elif lat > -23: geo_regions["Tropical"] += 1
        elif lat > -66: geo_regions["Southern Temperate"] += 1
        else: geo_regions["Antarctic"] += 1
    
    return {
        "total": len(events),
        "categories": dict(cat_counts.most_common(10)),
        "monthly": dict(sorted_months[-12:]),
        "trend": trend,
        "geo_regions": dict(geo_regions),
        "avg_per_month": round(np.mean(list(monthly.values())), 2) if monthly else 0,
        "std_per_month": round(np.std(list(monthly.values())), 2) if monthly else 0,
    }


@app.route("/")
def index():
    categories = fetch_categories() # categories: One or more categories assigned to the event.
    return render_template("eonet_index.html", categories=categories)

@app.route("/api/events")
def api_events():
    days = request.args.get("days", 30, type=int)
    category = request.args.get("category", None)
    status = request.args.get("status", "open")
    events = fetch_events(days, category, status)
    analysis = analyze_events(events)

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

@app.route("/api/event/<event_id>")
def api_event_detail(event_id):
    r = requests.get(f"{EONET_BASE}/events/{event_id}", timeout=10)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True, port=5000)