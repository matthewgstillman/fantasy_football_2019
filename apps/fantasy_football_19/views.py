from django.shortcuts import render, redirect
import requests, json

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
