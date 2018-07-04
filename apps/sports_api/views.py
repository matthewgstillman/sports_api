from django.shortcuts import render, redirect
import sports_py
# Create your views here.
def alllive(request):
    all_matches = sports_py.get_all_matches()
    for sport in all_matches:
        for match in sport:
            print('{} vs {}: {}-{}'.format(match.home_team, match.away_team,
         match.home_score, match.away_score))
    context = {
        'match': match,
        'all_matches': all_matches,
    }
    return render(request, 'sports_api/alllive.html', context)

def index(request):
    return render(request, 'sports_api/index.html')

def baseball(request):
    matches = sports_py.get_sport_scores('baseball')
    for match in matches:
        print(' {} vs {}: {}-{}'.format(match.home_team, match.away_team,
        match.home_score, match.away_score))
    context = {
        'match': match,
        'matches': matches,
    }
    return render(request, 'sports_api/baseball.html', context)


def basketball(request):
    matches = sports_py.get_sport_scores('basketball')
    for match in matches:
        print(' {} vs {}: {}-{}'.format(match.home_team, match.away_team,
        match.home_score, match.away_score))
    context = {
        'match': match,
        'matches': matches,
    }
    return render(request, 'sports_api/basketball.html', context)

def get_match_score(sport, team1, team2):
    match = sports_py.get_match_score('')
    return redirect('/')

def soccer(request):
    matches = sports_py.get_sport_scores('soccer')
    for match in matches:
        print(' {} vs {}: {}-{}'.format(match.home_team, match.away_team,
        match.home_score, match.away_score))
    context = {
        'match': match,
        'matches': matches,
    }
    return render(request, 'sports_api/soccer.html', context)

def tennis(request):
    matches = sports_py.get_sport_scores('tennis')
    for match in matches:
        print(' {} vs {}: {}-{}'.format(match.home_team, match.away_team,
        match.home_score, match.away_score))
    context = {
        'match': match,
        'matches': matches,
    }
    return render(request, 'sports_api/tennis.html', context)