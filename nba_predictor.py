import random
from nba_api.stats.endpoints import leaguestandings

# Fetch real NBA standings
print("Fetching real NBA data...\n")
standings = leaguestandings.LeagueStandings()
data = standings.get_data_frames()[0]

# Build teams list with real win rates
teams_data = {}
for _, row in data.iterrows():
    team = row["TeamName"]
    wins = row["WINS"]
    losses = row["LOSSES"]
    total = wins + losses
    win_rate = wins / total if total > 0 else 0.5
    teams_data[team] = win_rate

# Display teams
teams = list(teams_data.keys())
print("Here are all the NBA teams:\n")
for i, team in enumerate(teams, 1):
    print(f"{i}. {team}")

# Pick teams
home = int(input("\nEnter the number for the HOME team: ")) - 1
away = int(input("Enter the number for the AWAY team: ")) - 1

home_team = teams[home]
away_team = teams[away]

print(f"\nMatchup: {away_team} vs {home_team}")

# Predict winner based on real win rates
home_rate = teams_data[home_team] + 0.05  # home court advantage
away_rate = teams_data[away_team]

prediction = home_team if home_rate > away_rate else away_team
print(f"\nPrediction: {prediction} will win!")
print(f"  {home_team} win rate: {teams_data[home_team]:.0%}")
print(f"  {away_team} win rate: {teams_data[away_team]:.0%}")

# Ask user for their prediction
print(f"\nWho do you think will win?")
print(f"1. {home_team}")
print(f"2. {away_team}")

guess = input("\nEnter 1 or 2: ")

if guess == "1":
    user_pick = home_team
elif guess == "2":
    user_pick = away_team
else:
    print("Invalid choice!")
    exit()

# Compare user guess to prediction
print(f"\nYour pick: {user_pick}")
print(f"Prediction: {prediction}")

if user_pick == prediction:
    print("\n✅ You agree with the prediction!")
else:
    print("\n❌ You disagree with the prediction!")
