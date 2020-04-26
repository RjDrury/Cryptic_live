import re
import unidecode
from operator import itemgetter
def combine_twitch_mix_games(twitch_games, mixer_games):
    game_info = []
     # Different services use different puntuation for games - must compare without punctuation
    for game in twitch_games['top']:
        comparable_name = get_comparable_game_name(game["game"]["name"])
        game_info.append({"name":game["game"]["name"], "viewers":game["viewers"], "twitch_viewers":game["viewers"],
        "twitch_id" : game["game"]["_id"], "box_img":game["game"]["box"]["large"],"cpr_name":comparable_name , "mixer_id":"1"})

    for game in mixer_games:
        comparable_name = get_comparable_game_name(game["name"])
        idx = get_index_of_game(game_info, comparable_name)
        if idx!= -1:
            game_info[idx]["viewers"] = game_info[idx]["viewers"] + game["viewersCurrent"]
            game_info[idx]["mixer_id"] = game["id"]
            game_info[idx]["mixer_viewers"] = game["viewersCurrent"]
        else:
            game_info.append({"name":game["name"],"viewers": game["viewersCurrent"],
             "mixer_viewers":game["viewersCurrent"],
            "box_img":game["coverUrl"],"mixer_id": game["id"],"cpr_name":comparable_name, "twitch_id":"1"})
    game_info = sorted(game_info, key=itemgetter("viewers"), reverse=True)
    for game in game_info:
        game["viewers"] = format_viewers_to_k(game["viewers"])
        if "twitch_viewers" in game:
            game["twitch_viewers"] = format_viewers_to_k(game["twitch_viewers"])
        if "mixer_viewers" in game:
            game["mixer_viewers"] = format_viewers_to_k(game["mixer_viewers"])
    return game_info

def get_comparable_game_name(game_name):
    
     return unidecode.unidecode(re.sub(r'[^a-zA-Z0-9 ]', '', game_name).replace(" ", ""))

def get_index_of_game(game_list,comparable_name):

    for idx, game in enumerate(game_list):
        if game["cpr_name"] == comparable_name:
            return idx
    return -1
def format_viewers_to_k(viewers):
    viewers = str(round(viewers/1000,1))+"k"
    return viewers