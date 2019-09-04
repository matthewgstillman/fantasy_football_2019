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

def league(request):
    url = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/446679"
    response = requests.get(url, cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"} )
    data = response.json()
    print(data)
    season_id = data['seasonId']
    print("Season ID: {}".format(season_id))
    status = data['status']
    print("Status: {}".format(status))
    latest_scoring_period = status['latestScoringPeriod']
    print("Latest Scoring Period: {}".format(latest_scoring_period))
    current_matchup_period = status['currentMatchupPeriod']
    print("Current Matchup Period: {}".format(current_matchup_period))
    is_active = status['isActive']
    print("Is Active: {}".format(is_active))
    game_id = data['gameId']
    print("Game ID: {}".format(game_id))
    segment_id = data['segmentId']
    print("Segment ID: {}".format(segment_id))
    settings = data['settings']
    print("League Settings: {}".format(settings))
    league_name = settings['name']
    print("League Name: {}".format(league_name))
    teams = data['teams']
    print("Teams: {}".format(teams))
    for i in range(0, len(teams)):
        print("Team: {}".format(teams[i]))
        print(teams[i]['abbrev'])
        owners = teams[i]['owners']
        team_db_id = owners[0]
        print("Team DB ID: {}".format(team_db_id))
        team_nickname = teams[i]['nickname']
        print("Team Nickname: {}".format(team_nickname))
        team_id = teams[i]['id']
        print("Team ID: {}".format(team_id))
        team_location = teams[i]['location']
        print("Team Location: {}".format(team_location))
        team_name = str(team_location) + " " + str(team_nickname)
        print("Team Name: {}".format(team_name))
    members = data['members']
    print("Members: {}".format(members))
    for i in range(0, len(members)):
        print("Members: {}".format(members[i]))
        display_name = members[i]['displayName']
        print("Display Name: {}".format(display_name))
        member_id = members[i]['id']
        print("Member Berries! - Member ID: {}".format(member_id))
    context = {
        'data': data
    }
    return render(request, 'fantasy_football_19/league.html', context)

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
        print(int(team_id))
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
        player = player_pool_entry['player']
        print("Player: {}".format(player))
        player_first_name = player['firstName']
        player_last_name = player['lastName']
        print("Name: {} {}".format(player_first_name, player_last_name))
        player_full_name = player['fullName']
        player_injured = player['injured']
        player_default_position_id = player['defaultPositionId']
        ratings = player_pool_entry['ratings']
        print("Ratings: {}".format(ratings))
        # i_minus_one = i - 1
        # print("i - 1 = {}".format(i_minus_one))
        # ratings_item = ratings[1]['totalRanking']
        # print("Ratings Item: {}".format(ratings_item))
        # rankings = player['rankings']
        # print(rankings)
        # rank = rankings[1][0]
        # print("Player: {}".format(player))
    context = {
        'teams': teams,
        'data': data,
        'ids': ids
    }
    return render(request, 'fantasy_football_19/rosters.html', context)



def settings(request):
    url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/446679?view=mSettings'
    response = requests.get(url, cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"} )
    data = response.json()
    print(data)
    season_id = data['seasonId']
    # print("Season ID: {}".format(season_id))
    status = data['status']
    # print("Status: {}".format(status))
    transaction_scoring_period = status['transactionScoringPeriod']
    # print("Transaction Scoring Period: {}".format(transaction_scoring_period))
    current_matchup_period = status['currentMatchupPeriod']
    # print("Current Matchup Period: {}".format(current_matchup_period))
    waiver_process_status = status['waiverProcessStatus']
    # print("Waiver Process Status: {}".format(waiver_process_status))
    previous_seasons = status['previousSeasons']
    # print("Previous Seasons: {}".format(previous_seasons))
    is_playoff_matchup_edited = status['isPlayoffMatchupEdited']
    # print("Is Playoff Matchup Edited: {}".format(is_playoff_matchup_edited))
    final_scoring_period = status['finalScoringPeriod']
    # print("Final Scoring Period: {}".format(final_scoring_period))
    current_league_type = status['currentLeagueType']
    # print("Current League Type: {}".format(current_league_type))
    waiver_last_execution_date = status['waiverLastExecutionDate']
    # print("Waiver Last Execution Date: {}".format(waiver_last_execution_date))
    is_waiver_order_edited = status['isWaiverOrderEdited']
    # print("Is Waiver Order Edited: {}".format(is_waiver_order_edited))
    standings_update_date = status['standingsUpdateDate']
    # print("Standings Update: {}".format(standings_update_date))
    latest_scoring_period = status['latestScoringPeriod']
    # print("Latest Scoring Period: {}".format(latest_scoring_period))
    teams_joined = status['teamsJoined']
    # print("Teams Joined: {}".format(teams_joined))
    activated_date = status['activatedDate']
    # print("Activated Date: {}".format(activated_date))
    is_to_be_deleted = status['isToBeDeleted']
    # print("Is to be deleted: {}".format(is_to_be_deleted))
    is_full = status['isFull']
    # print("Is Full?: {}".format(is_full))
    first_scoring_period = status['firstScoringPeriod']
    # print("First Scoring Period: {}".format(first_scoring_period))
    is_viewable = status['isViewable']
    # print("Is Viewable?: {}".format(is_viewable))
    is_expired = status['isExpired']
    # print("Is Expired: {}".format(is_expired))
    created_as_league_type = status['createdAsLeagueType']
    # print("Created as league type: {}".format(created_as_league_type)
    # )
    is_active = status['isActive']
    # print("Is Active?: {}".format(is_active))
    context = {
        'data': data
    }
    return render(request, 'fantasy_football_19/settings.html', context)


def player_info(request):
    url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/446679?view=kona_player_info'
    response = requests.get(url, cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"} )
    data = response.json()
    print(data)
    players = data['players']
    print("Players: {}".format(players))
    for i in range(0, len(players)):
        status = players[0]
        print("Status: {}".format(status))
        player_status = status['status']
        print("Player Status: {}".format(player_status))
        player_ratings = status['ratings']
        print("Player Ratings: {}".format(player_ratings))
        # player_rating_and_ranking = player_ratings[0]
        # print("Player Rating and Ranking: {}".format(player_rating_and_ranking))
        # player = players['player']
        # print("Player: {}".format(player))
        # player_first_name = player_status['player']
        # print("Player First Name: {}".format(player_first_name))
        lineup_locked = status['lineupLocked']
        print("Lineup Locked: {}".format(lineup_locked))
        draft_auction_value = status['draftAuctionValue']
        print("Draft Auction Value: {}".format(draft_auction_value))
        keeper_value_future = status['keeperValueFuture']
        print("Keeper Value Future: {}".format(keeper_value_future))
        player = status['player']
        print("Player: {}".format(player))
        player_injured = player['injured']
        print("Player Injured: {}".format(player_injured))
        player_default_position_id = player['defaultPositionId']
        print("Player Default Position ID: {}".format(player_default_position_id))
        player_season_outlook = player['seasonOutlook']
        print("Player Season Outlook: {}".format(player_season_outlook))
        player_first_name = player['firstName']
        print("Player First Name: {}".format(player_first_name))
        player_last_name = player['lastName']
        print("Player Last Name: {}".format(player_last_name))
        player_eligible_slots = player['eligibleSlots']
        print("Player Eligible Slots: {}".format(player_eligible_slots))
        player_droppable = player['droppable']
        print("Player Droppable: {}".format(player_droppable))
        player_outlooks = player['outlooks']
        print("Player Outlooks: {}".format(player_outlooks))
        player_outlooks_by_week = player_outlooks['outlooksByWeek']
        print("Player Outlooks By Week: {}".format(player_outlooks_by_week))
        # player_week_one_outlook = player_outlooks_by_week[1]
        # print("Week 1 Outlook: {}".format(player_week_one_outlook))
        player_ownership = player['ownership']
        print("Player Ownership: {}".format(player_ownership))
        percent_stared = player_ownership['percentStarted']
        print("Percent Started: {}".format(percent_stared))
    context = {
        'data': data
    }
    return render(request, 'fantasy_football_19/player_info.html', context)
