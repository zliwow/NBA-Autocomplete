# System Design Description

## Overview
This system is designed to provide an autocomplete feature for an internal NBA team web application used by the front office, scouts, and coaching staff. The search engine enables users to search for players and teams, allowing for no more than 100 simultaneous users. The architecture below outlines how the system components work together to deliver this functionality.

## System Goals
The main goals of this autocomplete system are:
1. **Speed and Responsiveness**: Ensure that the search results are returned quickly as the user types. This is achieved by minimizing backend queries and processing.
2. **Accuracy**: The system must provide accurate player and team information. The backend ensures this by querying a well-organized, normalized database storing the processed data.
3. **Scalability**: While the system is designed for no more than 100 users, it is built to handle concurrent requests efficiently.

## System Components

### 1. **Frontend**:
   - The user interacts with the search engine through the frontend.
   - It captures the autocomplete input and sends it to the backend via an API call.
   - It then displays the relevant player or team data returned by the backend.
   - **Technologies**: Angular framework, HTTP client service.

### 2. **Backend**:
   - The backend serves as the bridge between the frontend and the database.
   - It processes the autocomplete input, queries the database, and returns the relevant information to the frontend.
   - It also handles the logic for fetching player summaries and teams based on user input.
   - **Technologies**: Django REST Framework (Python), PostgreSQL integration.

### 3. **Database (PostgreSQL)**:
   - The database stores all the processed player and team data.
   - Upon receiving an API request from the backend, it returns the relevant player or team information.
   - The backend ensures that the database is always queried efficiently by using well-structured, normalized tables.

## Data Flow

1. **Raw Data Processing**:
   - The raw data is first processed and then stored in a PostgreSQL database.
   
2. **Autocomplete Search**:
   - The user enters a search query in the frontend. 
   - The frontend sends this input to the backend.
   
3. **Backend Processing**:
   - The backend receives the query and communicates with the database.
   - Based on the search input, the backend retrieves relevant player/team data and sends it back to the frontend.

4. **Display of Player/Team Information**:
   - The frontend takes the data returned by the backend and displays it in real-time.
   - In the case of player summaries, shot charts and detailed statistics are displayed based on data from the database.

## Technologies Leveraged
- **Frontend**: Angular for the user interface and real-time display.
- **Backend**: Django REST Framework (Python) to handle API requests and process data.
- **Database**: PostgreSQL for structured, relational data storage, providing the backend with quick access to player/team information.

## Future Enhancements
To support more complex search requirements and larger datasets, **Elasticsearch** could be integrated as a dedicated search index. Elasticsearch provides advanced capabilities like fuzzy search, relevance scoring, and near-instantaneous query performance, which would enhance the quality of autocomplete suggestions and scale better as data grows.


