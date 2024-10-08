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


