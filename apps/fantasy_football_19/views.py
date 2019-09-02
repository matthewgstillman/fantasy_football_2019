from django.shortcuts import render, redirect
import requests, json
# from ff_espn_api import League
from dicts import ids

# Create your views here.
def index(request):
    response = requests.get('https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/446679',
    # params={'leagueId': 446679, 'seasonId': 2019},
    cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"})
    # response = requests.get(url)
    data = response.json()
    print(data)
    context = {
        'data': data
    }
    return render(request, 'fantasy_football_19/index.html', context)

# def league(request):
#     league_id = 446679
#     # year = 2019
#     # swid = "1001E5E2-2AE2-4AE8-A464-5B8D985F962D"
#     # espn_s2 = "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"
#     # league = League(league_id, year, espn_s2, swid)
#     # print(league)
#     context = {

#     }
#     return render(request, 'fantasy_footbal_19/league.html', context)

def matchups(request):
    url = 'https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/446679?2019?mMatchup'
    response = requests.get(url, params={"view": "mMatchup"}, cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"} )
    data = response.json()
    print(data)
    context = {
        'data': data
    }
    return render(request, 'fantasy_football_19/matchups.html', context)


def teams(request):
    url = 'https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/446679?2019?mTeam'
    response = requests.get(url, cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"} )
    data = response.json()
    print(data)
    context = {
        'data': data
    }
    return render(request, 'fantasy_football_19/teams.html', context)


def rosters(request):
    ids_list = []
    url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/446679?view=mRoster'
    # url = 'https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/446679?2019?mSchedule'
    response = requests.get(url, cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"} )
    data = response.json()
    print(data)
    season = data['seasonId']
    season_status = data['status']
    game_id = data['gameId']
    segment_id = data['segmentId']
    league_id = data['id']
    print("League ID: {}".format(league_id))
    print("Season: {}".format(season))
    print("IDs: {}".format(ids))
    # applied_stat_total = data['roster']['appliedStatTotal']
    teams = data['teams']
    print("Teams: {}".format(teams))
    for i in range(0, len(teams)):
        print(teams[i])
        team_id = teams[i]['id']
        print("Team ID: {}".format(team_id))
        roster = teams[i]['roster']
        print("Roster: {}".format(roster))
        applied_stat_total = roster['appliedStatTotal']
        acquisition_type = roster['entries'][i]['acquisitionType']
        print("Acquisition Type: {}".format(acquisition_type))
        acquisition_date = roster['entries'][i]['acquisitionDate']
        print("Acquisition Date: {}".format(acquisition_date))
        player_id = roster['entries'][i]['playerId']
        print("Player ID: {}".format(player_id))
        pending_transactions = roster['entries'][i]['pendingTransactionIds']
        status = roster['entries'][i]['status']
        player_pool_entry = roster['entries'][i]['playerPoolEntry']
        ratings = player_pool_entry['ratings']
        # total_ranking = ratings[i]['totalRanking']
        player = player_pool_entry['player']
        print("Player: {}".format(player))
        player_first_name = player['firstName']
        player_last_name = player['lastName']
        print("Name: {} {}".format(player_first_name, player_last_name))
        player_full_name = player['fullName']
        # player_first_name = player['first_name']
        # applied_stat_total = teams['roster']['appliedStatTotal']
        # status = teams['roster']['entries'][i]['status']
        # print("Status: {}".format(status))
        # acquisition_type = teams[i]['acquisitionType']
        # acquisition_date = teams[i]['acquisitionDate']
        # player_id = teams['roster']['entries'][i]['playerId']
        # print("Player ID: {}".format(player_id))
        # status = teams['roster']['entries'][i]['status']
        # print("Status: {}".format(status))
    context = {
        'teams': teams,
        'data': data,
        'ids': ids
    }
    return render(request, 'fantasy_football_19/rosters.html', context)
