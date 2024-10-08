## Database Architecture Description

The database for this project is structured using PostgreSQL and is designed to store detailed information about players, teams, and their performances in games. The key components of the database include normalized tables for **players**, **teams**, **games**, and **shots**, ensuring efficient querying and data retrieval.

### Key Tables:
1. **Players**: This table contains information about individual players, such as their name, player ID, minutes played, points scored, and various game-related statistics (assists, rebounds, steals, etc.). Each player has a unique identifier and can be linked to multiple games.

2. **Teams**: This table stores the names of teams that players belong to. The relationship between teams and players is many-to-one, as a team can have multiple players, but each player belongs to only one team at any given time.

3. **Games**: This table logs each game played, storing game-specific information such as the date, home team, and away team. Each game is linked to multiple players through player performance in that game.

4. **Shots**: This table captures detailed shot information for each player during a game, including the shot’s x and y coordinates (measured in feet from the basket), whether the shot was made, and the type of shot (two-pointer or three-pointer). This data allows for precise shot chart visualizations.

### Relationships:
- **Players** are linked to **teams** and **games**, ensuring that the system can easily retrieve a player's performance across multiple games and teams.
- **Shots** are linked to individual **players** and **games**, allowing for accurate visualization of player statistics and shot locations.

