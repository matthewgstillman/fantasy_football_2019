from django.shortcuts import render, redirect
import requests, json
# from ff_espn_api import League
from dicts import ids
from quickstart import *

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
        print("\nPlayer Full Name: {}".format(player_full_name))
        player_injured = player['injured']
        player_default_position_id = player['defaultPositionId']
        ratings = player_pool_entry['ratings']
        print("Ratings: {}".format(ratings))
        player_pro_team_id = player['proTeamId']
        print("Player Pro Team ID: {}".format(player_pro_team_id))
        player_id = player['id']
        print("Player ID: {}".format(player_id))
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
        percent_started = player_ownership['percentStarted']
        print("Percent Started: {}".format(percent_started))
        auction_value_average_change = player_ownership['auctionValueAverageChange']
        print("Auction Value Average Change: {}".format(auction_value_average_change))
        average_draft_position_percent_change = player_ownership['averageDraftPositionPercentChange']
        print("Average Draft Position Percent Change: {}".format(average_draft_position_percent_change))
        percent_owned = player_ownership['percentOwned']
        print("Percentage Owned: {}".format(percent_owned))
        ownership_date = player_ownership['date']
        print("Ownership Date: {}".format(ownership_date))
        ownership_league_type = player_ownership['leagueType']
        print("Ownership League Type: {}".format(ownership_league_type))
        ownership_percent_change = player_ownership['percentChange']
        print("Ownership Percentage Change: {}".format(ownership_percent_change))
        ownership_auction_value_average = player_ownership['auctionValueAverage']
        average_draft_position = player_ownership['averageDraftPosition']
        print("Average Draft Position: {}".format(average_draft_position))
        player_rankings = player['rankings']
        print("Player Rankings: {}".format(player_rankings))
        first_player_ranking_item = player_rankings['1']
        print("First Player Ranking Item: {}".format(first_player_ranking_item))
        for i in range(0, len(first_player_ranking_item)):
            first_player_ranking_rank_type = first_player_ranking_item[i]['rankType']
            print("First Player Ranking Rank Type: {}".format(first_player_ranking_rank_type))
            first_player_ranking_rank_source_id = first_player_ranking_item[i]['rankSourceId']
            print("First Player Ranking: {}".format(first_player_ranking_rank_source_id))
            first_player_ranking_auction_value = first_player_ranking_item[i]['auctionValue']
            print("First Player Auction Value: {}".format(first_player_ranking_auction_value))
            first_player_ranking_slot_id = first_player_ranking_item[i]['slotId']
            print("First Player Ranking Slot ID: {}".format(first_player_ranking_slot_id))
            first_player_ranking = first_player_ranking_item[i]['rank']
            print("First Player Ranking: {}".format(first_player_ranking))
        player_stats = player['stats']
        print("Player Stats: {}".format(player_stats))
        for i in range(0, len(player_stats)):
            print("Player Stat Item: {}".format(player_stats[i]))
            player_stats_season_id = player_stats[i]['seasonId']
            print("Player Stats Season ID: {}".format(player_stats_season_id))
            # player_stats_season_stats = player_stats_season['stats']
    context = {
        'data': data
    }
    return render(request, 'fantasy_football_19/player_info.html', context)

def player_week_one(request):
    url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/446679?view=mBoxscore'
    response = requests.get(url, cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"} )
    data = response.json()
    print(data)
    player_week_one_season = data['seasonId']
    print("Season: {}".format(player_week_one_season))
    context = {
        'data': data,
    }
    return render(request, 'fantasy_football_19/player_week_one.html', context)


def team(request):
    url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/446679?view=mTeam'
    response = requests.get(url, cookies={'swid': "1001E5E2-2AE2-4AE8-A464-5B8D985F962D",
    "espn_s2": "AEBokNq4aPr8liLBu9WPHgD0pqWtp1fiArO46aRrX%2F3139jBoyjjCjpygBuVIOwd3ITU3cJZ9qCmkJS5H%2FIYCq8gm4thQ1ehhUBEKXR7ZJSw47wsVoNmoCIkEvs6llNQKawmn%2FWnw%2Fawy%2B%2BUg1%2FygO8nCzReY5ro5AJXXRFM4t%2FInsIetIJocb1FFEoPW8OFU%2B4mxLcrxAT7jBzNsricQ%2FZbGbcI82nO4NNt8I4GuudLq1hb8xXnjNshQbBE9H79HxnmsMJxxpBytM3%2B9B74ZUGn"} )
    data = response.json()
    print(data)
    team_season = data['seasonId']
    print("Season: {}".format(team_season))
    team_status = data['status']
    print("Team Status: {}".format(team_status))
    team_transaction_scoring_period = team_status['transactionScoringPeriod']
    print("Team Transaction Scoring Period: {}".format(team_transaction_scoring_period))
    team_current_matchup_period = team_status['currentMatchupPeriod']
    print("Team Current Matchup Period: {}".format(team_current_matchup_period))
    team_waiver_process_status = team_status['waiverProcessStatus']
    print("Team Waiver Process Status: {}".format(team_waiver_process_status))
    team_previous_seasons = team_status['previousSeasons']
    print("Team Previous Seasons: {}".format(team_previous_seasons))
    is_playoff_matchup_edited = team_status['isPlayoffMatchupEdited']
    print("Is Playoff Matchup Edited: {}".format(is_playoff_matchup_edited))
    team_final_scoring_period = team_status['finalScoringPeriod']
    print("Team Final Scoring Period: {}".format(team_final_scoring_period))
    team_current_league_type = team_status['currentLeagueType']
    print("Team current league type: {}".format(team_current_league_type))
    team_waiver_last_execution_date = team_status['waiverLastExecutionDate']
    print("Team waiver last execution date: {}".format(team_waiver_last_execution_date))
    is_waiver_order_edited = team_status['isWaiverOrderEdited']
    print("Is waiver order edited: {}".format(is_waiver_order_edited))
    team_standings_update_date = team_status['standingsUpdateDate']
    print("Team Standings update: {}".format(team_standings_update_date))
    team_latest_scoring_period = team_status['latestScoringPeriod']
    teams_joined = team_status['teamsJoined']
    print("Teams joined: {}".format(teams_joined))
    teams_activated_date = team_status['activatedDate']
    print("Teams Activated Date: {}".format(teams_activated_date))
    is_to_be_deleted = team_status['isToBeDeleted']
    print("Is to be deleted?: {}".format(is_to_be_deleted))
    is_full = team_status['isFull']
    print("Is full?: {}".format(is_full))
    teams_first_scoring_period = team_status['firstScoringPeriod']
    teams_is_viewable = team_status['isViewable']
    print("Is viewable: {}".format(teams_is_viewable))
    teams_is_expired = team_status['isExpired']
    print("Teams is expired: {}".format(teams_is_expired))
    teams_created_as_league_type = team_status['createdAsLeagueType']
    print("Teams created as a league type: {}".format(teams_created_as_league_type))
    teams_is_active = team_status['isActive']
    print("Teams is active?: {}".format(teams_is_active))
    teams_game_id = data['gameId']
    print("Team Game ID: {}".format(teams_game_id))
    team_segment_id = data['segmentId']
    print("Team Segment ID: {}".format(team_segment_id))
    team_league_id = data['id']
    print("Team League ID: {}".format(team_league_id))
    team_league_members = data['members']
    print("\nLeague Members: {}".format(team_league_members))
    for i in range(0, len(team_league_members)):
        team_first_name = team_league_members[i]['firstName']
        print("Team First Name: {}".format(team_first_name))
        team_last_name = team_league_members[i]['lastName']
        print("Team Last Name: {}".format(team_last_name))
        team_display_name = team_league_members[i]['displayName']
        print(team_league_members[i])
        team_notification_settings = team_league_members[i]['notificationSettings']
        print("Team Notification Settings: {}".format(team_notification_settings))
        for j in range(0, len(team_notification_settings)):
            print("Team Notification Settings Expanded: {}".format(team_notification_settings[j]))
            team_notification_settings_type = team_notification_settings[j]['type']
            print("Team Notification Settings Type: {}".format(team_notification_settings_type))
            team_notification_type_enabled = team_notification_settings[j]['enabled']
            print("Team Notification Settings Enabled: {}".format(team_notification_type_enabled))
            team_notification_type_id = team_notification_settings[j]['id']
            print("Team Notification Type ID: {}".format(team_notification_type_id))
    teams = data['teams']
    print("Teams: {}".format(teams))
    for i in range(0, len(teams)):
        print("\nNew Team: {}".format(teams[i]))
        team_projected_draft_day_rank = teams[i]['draftDayProjectedRank']
        print("Team Projected Draft Day Rank: {}".format(team_projected_draft_day_rank))
        team_owners = teams[i]['owners']
        print("Team Owners: {}".format(team_owners))
        team_trade_block = teams[i]['tradeBlock']
        print("Team Trade Block: {}".format(team_trade_block))
        team_points_adjusted = teams[i]['pointsAdjusted']
        print("Team points adjusted: {}".format(team_points_adjusted))
        team_points_delta = teams[i]['pointsDelta']
        print("Team points delta: {}".format(team_points_delta))
        team_values_by_stat = teams[i]['valuesByStat']
        print("Team Values By Stat: {}".format(team_values_by_stat))
        team_waiver_rank = teams[i]['waiverRank']
        print("Team Waiver Rank: {}".format(team_waiver_rank))
        team_record = teams[i]['record']
        print("Team Record: {}".format(team_record))
        team_division_record = team_record['division']
        print("Team Division Record: {}".format(team_division_record))
        team_division_points_for = team_division_record['pointsFor']
        print("Team Division Points For: {}".format(team_division_points_for))
        team_division_points_against = team_division_record['pointsAgainst']
        print("Team Division Points Against: {}".format(team_division_points_against))
        team_division_wins = team_division_record['wins']
        print("Wins: {}".format(team_division_wins))
        team_division_losses = team_division_record['losses']
        print("Losses: {}".format(team_division_losses))
        team_division_ties = team_division_record['ties']
        print("Team Division Ties: {}".format(team_division_ties))
        team_division_percentage = team_division_record['percentage']
        print("Team Division Percentage: {}".format(team_division_percentage))
        team_division_streak_type = team_division_record['streakType']
        print("Team Division Streak Type: {}".format(team_division_streak_type))
        team_division_games_back = team_division_record['gamesBack']
        print("Division Games Back: {}".format(team_division_games_back))
        team_overall_record = team_record['overall']
        print("Team Overall Record: {}".format(team_overall_record))
        team_overall_points_for = team_overall_record['pointsFor']
        print("Team Overall Points For: {}".format(team_overall_points_for))
        team_overall_points_against = team_overall_record['pointsAgainst']
        print("Team Overall Points Against: {}".format(team_overall_points_against))
        team_overall_wins = team_overall_record['wins']
        print("Team Overall Wins: {}".format(team_overall_wins))
        team_overall_losses = team_overall_record['losses']
        print("Team Overall Losses: {}".format(team_overall_losses))
        team_overall_ties = team_overall_record['ties']
        print("Team Overall Ties: {}".format(team_overall_ties))
        team_overall_percentage = team_overall_record['percentage']
        print("Team Overall Percentage: {}".format(team_overall_percentage))
        team_overall_streak_type = team_overall_record['streakType']
        print("Team Overall Streak Type: {}".format(team_overall_streak_type))
        team_home_record = team_record['home']
        print("Team Home Record: {}".format(team_home_record))
        team_home_points_for = team_home_record['pointsFor']
        print("Team Home Points For: {}".format(team_home_points_for))
        team_home_points_against = team_home_record['pointsAgainst']
        print("Team Home Points Against: {}".format(team_home_points_against))
        team_home_wins = team_home_record['wins']
        print("Team Home Wins: {}".format(team_home_wins))
        team_home_losses = team_home_record['losses']
        print("Team Home Losses: {}".format(team_home_losses))
        team_home_ties = team_home_record['ties']
        print("Team Home Ties: {}".format(team_home_ties))
        team_home_percentage = team_home_record['percentage']
        print("Team Overall Percentage: {}".format(team_home_percentage))
        team_home_streak_type = team_overall_record['streakType']
        print("Team Home Streak Type: {}".format(team_home_streak_type))
        team_away_record = team_record['away']
        print("Team Away Record: {}".format(team_away_record))
        team_away_points_for = team_away_record['pointsFor']
        print("Team Away Points For: {}".format(team_away_points_for))
        team_away_points_against = team_away_record['pointsAgainst']
        print("Team Away Points Against: {}".format(team_away_points_against))
        team_away_wins = team_away_record['wins']
        print("Team Away Wins: {}".format(team_away_wins))
        team_away_losses = team_away_record['losses']
        print("Team Away Losses: {}".format(team_away_losses))
        team_away_ties = team_away_record['ties']
        print("Team Away Ties: {}".format(team_away_ties))
        team_away_percentage = team_away_record['percentage']
        print("Team Away Percentage: {}".format(team_away_percentage))
        team_away_streak_type = team_away_record['streakType']
        print("Team Away Streak Type: {}".format(team_away_streak_type))
    context = {
        "data" : data,
    }
    return render(request, 'fantasy_football_19/team.html', context)
