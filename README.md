# CS_122_Term_Project
- **Project Title:** The Hikers Guide to the Galaxy

- **Authors:** Pari Sharma and Shannon Lo

- **Project Description:**
A natural disaster dashboard using data from the National Weather Service, National Park Service, and other federally funded government websites. By scraping this data from the websites, we'll be able to create a dashboard where different natural disasters can be reviewed and warnings will be submitted based on region and disaster type.

- **Project Outline/Plan:**
  - _**Interface Plan**_
    - The dashboard will consist of two main views: a home screen and a trail detail pop-up window. The home screen serves as the primary interface, displaying a filterable table or card grid of all scraped hiking trails and their current open/closed status. At the top of the home screen, a region/park drop-down menu allows users to filter trails by location (e.g., Sierra Nevada, Central Coast, Bay Area), and a second status filter drop-down lets users narrow results to only open trails, only closed trails, or all trails. A "Refresh Data" button triggers the Python scraper to re-fetch the latest trail conditions from the government websites and update the display in real time. A search bar allows users to type a trail name and instantly filter the visible results. When a user clicks on any trail in the list, a pop-up window opens displaying detailed information about that specific trail, including the full closure reason, the date the status was last updated, the park it belongs to, and any posted ranger notes or advisories scraped from the source page. The pop-up includes a "Close" button to dismiss it and return to the home screen. This two-window structure keeps the main view clean and scannable while still surfacing granular detail on demand.
      
  - _**Data Collection and Storage Plan**_
    - Region data will be collected by scraping publicly available information from federal and state government websites, specifically targeting sources such as the National Park Service (nps.gov), the USDA Forest Service (fs.usda.gov), and the California Department of Parks and Recreation (parks.ca.gov). A Python script using the requests library will fetch the raw HTML from each target page, and BeautifulSoup will parse the relevant fields including trail name, location, open/closed status, closure reason, and last updated date. Since government websites update trail conditions periodically rather than in real time, the scraper will be scheduled to run on a regular interval (e.g., once daily or on-demand before the dashboard loads) to keep data reasonably fresh. The cleaned and structured data will be stored locally in a CSV file, with each record timestamped to track when it was retrieved. This storage approach keeps the project self-contained without requiring a hosted database, while still allowing the dashboard to query and filter trail records efficiently by attributes like region, park name, or current status.
      
  - _**Data Analysis and Visualization Plan**_
    - The analysis component will use Python's `pandas` library to calculate campsite occupancy rates and trail closure frequencies across all scraped parks, identifying patterns in availability by region, season, and park type. Using `numpy`, the program will compute summary statistics such as average availability per park and percentage of trails marked as closed or hazardous at any given time. The visualization component will produce a bar chart comparing campsite availability across parks using `seaborn`, giving users a clear side-by-side view of which locations are most and least accessible. A second plot will display a heatmap or time series showing how trail conditions change over time, allowing users to spot seasonal trends or recurring closures at specific parks. Both visualizations will be embedded directly in the program interface, updating dynamically based on the user's selected filters such as park name, region, or status type.

### Resources
- https://eonet.gsfc.nasa.gov/docs/v3 
- https://eonet.gsfc.nasa.gov/how-to-guide
