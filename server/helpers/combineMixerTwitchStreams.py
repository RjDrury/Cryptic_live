from operator import itemgetter
def combine_twitch_mix_streams(twitch, mixer):
    stream_info = []
    for stream in twitch["data"]:
        stream_info.append({"name":stream["user_name"], "viewers":stream["viewer_count"]
        ,"thumbnail":stream["thumbnail_url"],"game_id":stream["game_id"],
         "title":stream["title"], "user_id":stream["user_id"], "twitch":True, "mixer":False})
         
    for stream in mixer:
        stream_info.append({"name":stream["token"], "viewers":stream["viewersCurrent"]
        ,"thumbnail":stream["bannerUrl"],"game_id":stream["typeId"], "title":stream["name"], 
        "platform":"mixer","twitch":False, "mixer":True})

    return sorted(stream_info, key=itemgetter("viewers"), reverse=True)

