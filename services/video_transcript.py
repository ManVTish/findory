# from typing import List
from models.common_lib import List
from youtube_transcript_api import YouTubeTranscriptApi

class VideoTranscript:
    def find_video_transcript(video_id: str):
        user_video_transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return user_video_transcript


    def search_keyword(keyword: str, transcript_data: List):
        mylist=[]
        trans = transcript_data

        for i in trans:

            if keyword in i['text']:
                start_point = i['start']
                start_end = {"start_time": start_point, "end_time": start_point + i['duration']}
                mylist.append(start_end)

        return mylist

