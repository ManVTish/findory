# from redis_om import HashModel

# class VideoTranscript(HashModel):
#     t_user_video_id: str
#     t_transcript_list: list

    
    
#     class Meta:
#         database = redis


# @app.get('/video/{video_id}')
# def get_video_transcript(video_id: str):
#     print("This is the given video ID: ", video_id)
#     video_data = Video.video_transcript(video_id)
#     return video_data

# @app.get('/keyword/{keyword}')
# def get_keyword_record(keyword: str):
#     transcript = video.user_video_transcript
#     return video.search_keyword(keyword, transcript)