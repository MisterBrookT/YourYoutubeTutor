from youtube_transcript_api import YouTubeTranscriptApi
from typing import List, Dict
class YoutubeExtractor:
    @staticmethod
    # example as https://www.youtube.com/watch?v=lXUZvyajciY&t=7028s
    def get_transcript(url: str) -> List[Dict]:
        """
        Get the transcript of a YouTube video.
        """
        youtube_id = YoutubeExtractor._extract_youtube_id(url)
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(youtube_id).to_raw_data()
        return transcript

    @staticmethod
    def _extract_youtube_id(url: str) -> str:
        """
        Extract the YouTube ID from a URL.
        """
        part = url.split("v=")[1] 
        if "&" in part:
            part = part.split("&")[0]
        return part