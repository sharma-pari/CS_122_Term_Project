# CS_122_Term_Project
- **Project Title:** EONET // Natural Disaster Monitor

- **Authors:** Pari Sharma and Shannon Lo

- **Project Description:**
A natural disaster dashboard using data from the National Weather Service, National Park Service, and other federally funded government websites. By scraping this data from the websites, we'll be able to create a dashboard where different natural disasters can be reviewed and warnings will be submitted based on region and disaster type.


- **Project Outline/Plan:**
  - _**Interface Plan**_
    - The dashboard consists of two main views: a home screen and an event detail pop-up window. The home screen serves as the primary interface, displaying a live interactive world map with color-coded markers representing active natural events pulled from NASA's EONET API. At the top of the home screen, a category drop-down menu allows users to filter events by type (e.g., Wildfires, Severe Storms, Volcanoes), and a status drop-down lets users toggle between open (ongoing) and closed (resolved) events. A days slider controls the time window for how far back events are fetched, and a Fetch button applies all selected filters and refreshes the display. Hovering over a marker previews the event type, location, and date. When a user clicks any marker, a pop-up window opens displaying the complete details for that event pulled from NASA's API. The pop-up includes a Close button to dismiss it and return to the home screen. This two-window structure keeps the main view clean and scannable while still surfacing full event detail on demand.

  - _**Data Collection and Storage Plan**_
    - Event data is collected by making live requests to NASA's Earth Observatory Natural Event Tracker (EONET) API (v3). A Python backend using the `requests` library fetches event data from the EONET `/events` and `/categories` endpoints, passing parameters such as time range, event category, and open/closed status. The API returns structured JSON containing event titles, categories, geographic coordinates, and dates, eliminating the need for HTML scraping. Since the data is fetched live on demand rather than stored, each user request retrieves the most current available information directly from NASA. This approach keeps the project self-contained without requiring a hosted database, while still allowing the dashboard to filter and display event records efficiently by category, status, and time window.

  - _**Data Analysis and Visualization Plan**_
    - The analysis component uses Python's `numpy` and `scipy` libraries to compute statistics on whichever set of events is currently loaded. Using `scipy.stats.linregress`, the program calculates a linear regression trend over monthly event frequency, producing a slope and R² value to indicate whether events are increasing or decreasing over the selected time period. Using `numpy`, it computes the mean and standard deviation of monthly event counts. Events are also clustered geographically into regions (Arctic, Northern Temperate, Tropical, Southern Temperate, and Antarctic) based on their coordinates. The visualization component uses Plotly.js to produce three interactive charts: a globe and map view with color-coded event categories, a monthly frequency bar chart with a trend line overlay, and a category distribution donut chart. All three visualizations update dynamically based on the user's selected filters.

## Features
 
### Interface (GUI)
- **Home screen** with live world map showing event locations
- **Event detail modal** (pop-up window): Click any map marker to view full event details, hover to preview event type, location, and date
- **4+ widgets**: Category dropdown, Status dropdown, Days slider, Fetch button
### Data Analysis (scipy/numpy)
- Linear regression trend (slope, R²) using `scipy.stats.linregress`
- Mean and standard deviation of monthly event frequency via `numpy`
- Geographic region clustering (Arctic / Temperate / Tropical)
### Visualization (Plotly)
- Interactive globe/map with color-coded event categories
- Monthly frequency bar chart with trend line overlay
- Category distribution donut chart

### Resources
- https://eonet.gsfc.nasa.gov/docs/v3 
- https://eonet.gsfc.nasa.gov/how-to-guide

  
## Division of Labor
 
**Shannon:**
- **Data Access:** wrote the functions to fetch live event data from NASA's EONET API, handling parameters like time range, category, and status filters
- **Data Organization:** structured and cleaned the raw API response into organized, map-ready event objects with coordinates, categories, and dates
  
**Pari:**
- **Visualization:** built the three interactive Plotly charts (globe map, monthly bar chart, and donut chart) that display event data dynamically based on user filters
- **Analysis:** developed the statistical analysis functions including linear regression trend, mean and standard deviation of monthly counts, and geographic region clustering

 
