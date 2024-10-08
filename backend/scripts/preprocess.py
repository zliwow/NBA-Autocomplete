import json
import math

# Load JSON files
def load_json_files():
    with open('backend/raw_data/players.json') as players_file, \
        open('backend/raw_data/teams.json') as teams_file, \
        open('backend/raw_data/games.json') as games_file:


        
        players_data = json.load(players_file)
        teams_data = json.load(teams_file)
        games_data = json.load(games_file)
        
        return players_data, teams_data, games_data

# Calculate distance from the hoop
def calculate_distance(locationX, locationY):
    return math.sqrt(locationX**2 + locationY**2)

# Determine the type of shot based on distance from the hoop
def classify_shot_type(locationX, locationY):
    distance = calculate_distance(locationX, locationY)
    if distance >= 22.0:  # Based on the court diagram
        return 'Three Pointer'
    else:
        return 'Two Pointer'

# Create mappings and process the data
def preprocess_data():
    players_data, teams_data, games_data = load_json_files()

    # Create mappings
    teams_map = {team['id']: team['name'] for team in teams_data}
    players_map = {player['id']: player for player in players_data}

    processed_games = []

    for game in games_data:
        game_info = {
            'game_id': game['id'],
            'date': game['date'],
            'home_team': teams_map[game['homeTeam']['id']],
            'away_team': teams_map[game['awayTeam']['id']],
            'home_team_players': [],
            'away_team_players': []
        }

        # Process home team players
        for player in game['homeTeam']['players']:
            player_data = players_map[player['id']]
            player_stats = {
                'id': player_data['id'],  # Include player ID
                'name': player_data['name'],  # Player name
                'isStarter': player['isStarter'],
                'minutes': player['minutes'],
                'points': player['points'],
                'assists': player['assists'],
                'offensiveRebounds': player['offensiveRebounds'],
                'defensiveRebounds': player['defensiveRebounds'],
                'steals': player['steals'],
                'blocks': player['blocks'],
                'turnovers': player['turnovers'],
                'defensiveFouls': player['defensiveFouls'],
                'offensiveFouls': player['offensiveFouls'],
                'freeThrowsMade': player['freeThrowsMade'],
                'freeThrowsAttempted': player['freeThrowsAttempted'],
                'twoPointersMade': player['twoPointersMade'],
                'twoPointersAttempted': player['twoPointersAttempted'],
                'threePointersMade': player['threePointersMade'],
                'threePointersAttempted': player['threePointersAttempted'],
                'shots': []  # Shot details go here
            }

            # Add shot details, classify shot based on location
            for shot in player.get('shots', []):
                locationX = shot.get('locationX', 0.0)
                locationY = shot.get('locationY', 0.0)
                shot_type = classify_shot_type(locationX, locationY)  # Classify shot based on distance

                shot_info = {
                    'isMake': shot['isMake'],
                    'locationX': locationX,
                    'locationY': locationY,
                    'shot_type': shot_type  # Two Pointer or Three Pointer based on location
                }
                player_stats['shots'].append(shot_info)

            game_info['home_team_players'].append(player_stats)

        # Process away team players
        for player in game['awayTeam']['players']:
            player_data = players_map[player['id']]
            player_stats = {
                'id': player_data['id'],  # Include player ID
                'name': player_data['name'],  # Player name
                'isStarter': player['isStarter'],
                'minutes': player['minutes'],
                'points': player['points'],
                'assists': player['assists'],
                'offensiveRebounds': player['offensiveRebounds'],
                'defensiveRebounds': player['defensiveRebounds'],
                'steals': player['steals'],
                'blocks': player['blocks'],
                'turnovers': player['turnovers'],
                'defensiveFouls': player['defensiveFouls'],
                'offensiveFouls': player['offensiveFouls'],
                'freeThrowsMade': player['freeThrowsMade'],
                'freeThrowsAttempted': player['freeThrowsAttempted'],
                'twoPointersMade': player['twoPointersMade'],
                'twoPointersAttempted': player['twoPointersAttempted'],
                'threePointersMade': player['threePointersMade'],
                'threePointersAttempted': player['threePointersAttempted'],
                'shots': []  # Shot details go here
            }

            # Add shot details, classify shot based on location
            for shot in player.get('shots', []):
                locationX = shot.get('locationX', 0.0)
                locationY = shot.get('locationY', 0.0)
                shot_type = classify_shot_type(locationX, locationY)  # Classify shot based on distance

                shot_info = {
                    'isMake': shot['isMake'],
                    'locationX': locationX,
                    'locationY': locationY,
                    'shot_type': shot_type  # Two Pointer or Three Pointer based on location
                }
                player_stats['shots'].append(shot_info)

            game_info['away_team_players'].append(player_stats)

        processed_games.append(game_info)

    # Save to a new JSON file
    with open('processed_data_with_ids.json', 'w') as processed_file:
        json.dump(processed_games, processed_file, indent=4)

    print("Data pre-processing complete. Saved as 'processed_data_with_ids.json'.")

if __name__ == '__main__':
    preprocess_data()