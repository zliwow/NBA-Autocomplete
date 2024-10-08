# NBA Autocomplete Project

This project implements an autocomplete search engine for an internal web application used by an NBA team’s front office, scouts, and coaching staff. Users can search for players, and the system fetches relevant player details and visualizes their game performance. The project consists of a backend powered by Django and PostgreSQL and a frontend built using Angular. 

## Project Overview

The project’s key objective is to provide a fast, efficient, and scalable search solution for player and team lookups. The backend processes raw game, player, and team data, stores it in a PostgreSQL database, and exposes a REST API for the frontend to consume. The frontend handles user interactions, search input, and data visualization.

Key features:
- **Autocomplete**: The search engine leverages an autocomplete feature, allowing users to start typing a name and see suggestions for matching players.
- **Player Summary**: For each player, a detailed summary of their game statistics, including minutes played, points scored, assists, rebounds, and more, is displayed.
- **Shot Visualization**: Shot data, including the location of each shot relative to the basket, is displayed graphically on a basketball court diagram, helping users analyze shot performance.

This system is designed to support up to 100 users concurrently and is optimized for speed and data accuracy.

## Project Structure

```bash
backend/
  ├── app/
  │   ├── views/               # API views for player summaries
  │   ├── models/              # Django models for database schema
  ├── scripts/                 # Data processing and loading scripts
  ├── requirements.txt         # Backend dependencies
frontend/
  ├── src/
  │   ├── app/
  │   │   ├── player-summary/   # Player summary component
  ├── package.json             # Frontend dependencies


Installation Instructions
Backend Setup
Install PostgreSQL
Download and install PostgreSQL from PostgreSQL Downloads.

Set up Database
Run the following commands in your terminal to set up the database:

bash
Copy code
createuser okcapplicant --createdb;
createdb okc;
psql okc
create schema app;
alter user okcapplicant with password 'thunder';
grant all on schema app to okcapplicant;
Install Python and Dependencies
You can install Python dependencies using pyenv and virtualenv. Run the following commands:

bash
Copy code
pyenv install 3.10.1
pyenv virtualenv 3.10.1 okc
pyenv local okc
pip install -r backend/requirements.txt
Run Backend
Start the backend server:

bash
Copy code
cd backend
python manage.py runserver
The backend server will run on http://localhost:8000/.

Load Data into Database
Run the data processing script to load the data into PostgreSQL:

bash
Copy code
python backend/scripts/load_data.py
Frontend Setup
Install Node.js
Download and install Node.js (version 16.x.x).

Install Dependencies
Navigate to the frontend directory and install dependencies:

bash
Copy code
cd frontend
npm install --force
Run Frontend
Start the frontend server:

bash
Copy code
npm start
The frontend server will run on http://localhost:4200/.

Usage
Visit http://localhost:4200/ to use the application.
Use the search bar to find players or teams, and the player summary will be displayed with shot visualizations on a court diagram.
System Design
Overview
The autocomplete system is designed to provide fast and efficient search functionality. The backend manages data storage and provides an API for querying player and team data. The frontend handles user input, displaying search suggestions and player summaries. The system is optimized to handle up to 100 concurrent users, ensuring low-latency responses.

Key Design Goals:
Performance: The system is optimized for speed, using a lightweight database and minimal dependencies to ensure quick searches.
Scalability: The design supports 100 simultaneous users, leveraging efficient data structures and APIs.
Maintainability: Clear separation between the frontend and backend, making it easier to maintain and extend.
Technologies Used:
Frontend: Angular for handling UI interactions and visualization.
Backend: Django and PostgreSQL for data storage and REST API creation.
Architectural Flow:
User Input: Users enter search terms, which are processed by the frontend.
Autocomplete Request: The frontend sends requests to the backend’s search API for player or team suggestions.
Database Query: The backend queries the PostgreSQL database to fetch relevant player/team data.
API Response: The backend returns search results and player summaries via RESTful endpoints.
UI Rendering: The frontend processes the response, updates the UI, and displays relevant player data and shot visualizations.
Project Features
Autocomplete Search: The autocomplete feature helps users quickly find players by fetching matching results as they type.
Player Summary: Detailed player statistics are fetched and displayed in real-time, including points, rebounds, assists, and more.
Shot Visualization: Player shot data is plotted on a basketball court diagram, showing whether the shots were made or missed.
Contributing
Feel free to open an issue or submit a pull request if you'd like to contribute to the project.
