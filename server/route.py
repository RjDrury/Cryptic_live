from app import app
from flask import jsonify, request
from helpers.combineMixerTwitchGames import combine_twitch_mix_games
from helpers.combineMixerTwitchStreams import combine_twitch_mix_streams
import requests
# twitch api: https://dev.twitch.tv/docs/api/reference#get-top-games
# mixer api: https://dev.mixer.com/rest/index.html#

## Return a json of top streamers by viewers
@app.route('/topstreamers', methods=['get'])
def get_streamers():
    response_twitch=requests.get("https://api.twitch.tv/helix/streams?first=100", headers={"client-id":"dms7sh0fza9rao1zenqkrertn8q9gy"})
    response_mixer=requests.get("https://mixer.com/api/v1/channels?order=viewersCurrent:DESC", headers={"client-id":"c50ddb4fe3623dad063d858e32f2d841c59de32526624dff"})
    
    full_stream_list = combine_twitch_mix_streams(response_twitch.json(),response_mixer.json())
    return jsonify(stream_list=full_stream_list)

## return a json of top games by viewers
@app.route('/games', methods=['get'])
def get_top_games(): # uses v5 instead of helix - helix doesn't show viewer count per game??????
    response_twitch=requests.get("https://api.twitch.tv/kraken/games/top?limit=51", headers={"Accept": "application/vnd.twitchtv.v5+json","client-id":"dms7sh0fza9rao1zenqkrertn8q9gy"})
    response_mixer=requests.get("https://mixer.com/api/v1/types?order=viewersCurrent:DESC", headers={"client-id":"c50ddb4fe3623dad063d858e32f2d841c59de32526624dff"})
    
    full_game_list = combine_twitch_mix_games(response_twitch.json(), response_mixer.json())
    return jsonify(game_list=full_game_list)

## return a json of top streamers for a game
@app.route('/game/<twitch_id>/<mixer_id>', methods=['get'])
def get_top_streamers_for_game(twitch_id,mixer_id):
    #twitch test game id = 493057
    #mixer test game id = 70323
    response_twitch = None
    response_mixer = None

    if twitch_id == "1" and mixer_id == "1":
        twitch_id = "493057"
        mixer_id = "70323"
        
    if  twitch_id != "0":
        response_twitch = requests.get("https://api.twitch.tv/helix/streams/?game_id="+str(twitch_id), headers={"client-id":"dms7sh0fza9rao1zenqkrertn8q9gy"}).json()
    if  mixer_id != "0":
        response_mixer = requests.get("https://mixer.com/api/v1/types/"+str(mixer_id)+"/channels?order=viewersCurrent:DESC", headers={"client-id":"c50ddb4fe3623dad063d858e32f2d841c59de32526624dff"}).json()

    full_stream_list = combine_twitch_mix_streams(response_twitch,response_mixer)
    return jsonify(stream_list=full_stream_list)

## Return a json of top streamers by viewers
@app.route('/gamename/<twitch_id>/<mixer_id>', methods=['get'])
def get_top_games_name(twitch_id,mixer_id):
    response_twitch = None
    response_mixer = None
    game_name = {}
    if twitch_id != 1:
        response_twitch = requests.get("https://api.twitch.tv/helix/games?id="+twitch_id, headers={"client-id":"dms7sh0fza9rao1zenqkrertn8q9gy"}).json()
        game_name["name"] = response_twitch["data"][0]['name']  
    elif mixer_id != 1:
        response_mixer = requests.get("https://mixer.com/api/v1/types/"+mixer_id, headers={"client-id":"c50ddb4fe3623dad063d858e32f2d841c59de32526624dff"}).json()
        game_name["name"] = response_mixer["name"]
    else:
        game_name["name"] = "Game"
    return jsonify(game_name)
