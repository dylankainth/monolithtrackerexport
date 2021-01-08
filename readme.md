# MonolithTrackerExport

Monolith Tracker is a collaborative effort on tracking the Monoliths that are appearing around the world

MonolithTrackerExport is a method of utilising the MonolithTracker API to create HTML and PDF files.

It is ideally used in a Docker Container and deployed using Docker-Compose;

**However,** it is possible to simply run the python script called `app.py`, *Note: By using this method, the output will be accessible through a flask webpage, hosted at `localhost:5000` or `youriphere:5000`*

It works by calling the JSON API (endpoint = `https://monolithtracker.com/json-export`) and Python to generate a `.html` file in the `web/templates` folder, which is then open to the web using a flask server.

## Installation
You'll want to use a Docker container and Docker Compose.
1. Ensure Docker and Docker-compose are both installed
2. Install the repository as a zip file and extract the contents to any folder
3. `cd` to that folder *Note you can double check that you're in the right place by typing the command `ls` on Linux or `dir` on Windows; Other files in the folder should be `docker-compose.yml` and a folder called `web`*
4. Run the command `docker-compose up --build`

Alternatively, using python;
1. Run the python script at `web/app.py` , *optionally, use venv for convenience*

## Usage
1. Simply open `http://localhost:5000` to load the output page
2. To regenerate open `http://localhost:5000/regen`
