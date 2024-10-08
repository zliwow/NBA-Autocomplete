import os
import json
from rest_framework.views import APIView
from django.http import JsonResponse
from django.conf import settings
import logging

LOGGER = logging.getLogger('django')

# API to return player summary data by player ID
class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        """Return player data dynamically based on playerID"""

        # Path to processed_data.json
        file_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'processed_data.json')

        try:
            with open(file_path, 'r') as data_file:
                data = json.load(data_file)

            # Search for the player with matching playerID
            player_data = None
            for game in data:
                for player in game['home_team_players'] + game['away_team_players']:
                    LOGGER.info(f"Checking player with ID: {player['id']}")
                    if str(player['id']) == str(playerID):
                        player_data = player
                        break
                if player_data:
                    break

            if player_data:
                # Format the response to match the structure in sample_response.json
                player_summary = {
                    "name": player_data["name"],
                    "isStarter": player_data["isStarter"],
                    "minutes": player_data["minutes"],
                    "points": player_data["points"],
                    "assists": player_data["assists"],
                    "offensiveRebounds": player_data["offensiveRebounds"],
                    "defensiveRebounds": player_data["defensiveRebounds"],
                    "steals": player_data["steals"],
                    "blocks": player_data["blocks"],
                    "turnovers": player_data["turnovers"],
                    "defensiveFouls": player_data["defensiveFouls"],
                    "offensiveFouls": player_data["offensiveFouls"],
                    "freeThrowsMade": player_data["freeThrowsMade"],
                    "freeThrowsAttempted": player_data["freeThrowsAttempted"],
                    "twoPointersMade": player_data["twoPointersMade"],
                    "twoPointersAttempted": player_data["twoPointersAttempted"],
                    "threePointersMade": player_data["threePointersMade"],
                    "threePointersAttempted": player_data["threePointersAttempted"],
                    "shots": player_data["shots"]
                }
                return JsonResponse(player_summary)

            return JsonResponse({'error': 'Player not found'}, status=404)

        except FileNotFoundError:
            LOGGER.error("Data file not found")
            return JsonResponse({'error': 'Data file not found'}, status=500)

        except Exception as e:
            LOGGER.error(f"Error fetching player data: {str(e)}")
            return JsonResponse({'error': 'Internal server error'}, status=500)


# API to return autocomplete suggestions for players and teams
class SearchAutocomplete(APIView):
    def get(self, request):
        """Return autocomplete suggestions for players and teams"""
        query = request.GET.get('query', '')

        # Path to processed_data.json
        file_path = os.path.join(os.path.dirname(settings.BASE_DIR), 'processed_data.json')

        try:
            with open(file_path, 'r') as data_file:
                data = json.load(data_file)

            # Search for matching players and teams
            players = set()
            teams = set()

            for game in data:
                # Players
                for player in game['home_team_players'] + game['away_team_players']:
                    if query.lower() in player['name'].lower():
                        players.add((player['id'], player['name']))

                # Teams
                if query.lower() in game['home_team'].lower():
                    teams.add(game['home_team'])
                if query.lower() in game['away_team'].lower():
                    teams.add(game['away_team'])

            results = {
                'players': [{'id': p[0], 'name': p[1]} for p in players],
                'teams': [{'name': t} for t in teams],
            }

            return JsonResponse(results)

        except FileNotFoundError:
            LOGGER.error("Data file not found")
            return JsonResponse({'error': 'Data file not found'}, status=500)

        except Exception as e:
            LOGGER.error(f"Error fetching autocomplete data: {str(e)}")
            return JsonResponse({'error': 'Internal server error'}, status=500)
