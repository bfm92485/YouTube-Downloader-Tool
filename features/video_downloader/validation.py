"""URL validation for YouTube downloader."""
import re
from typing import Tuple, Optional


def validate_youtube_url(url: str) -> Tuple[bool, Optional[str]]:
    """
    Validate if a URL is a valid YouTube URL.
    
    Args:
        url: The URL to validate
        
    Returns:
        Tuple containing:
            - Boolean indicating if URL is valid
            - Error message if invalid, None otherwise
    """
    # Check if URL is empty
    if not url:
        return False, "URL cannot be empty"
    
    # Regular expressions for YouTube URLs
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)'
        r'([a-zA-Z0-9_-]{11})(\S*)'
    )
    
    match = re.match(youtube_regex, url)
    if not match:
        return False, "Invalid YouTube URL format"
    
    video_id = match.group(4)
    if not video_id or len(video_id) != 11:
        return False, "Invalid YouTube video ID"
    
    return True, None


def extract_video_id(url: str) -> Optional[str]:
    """
    Extract video ID from a YouTube URL.
    
    Args:
        url: The YouTube URL
        
    Returns:
        The video ID if found, None otherwise
    """
    # Skip validation if already validated
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)'
        r'([a-zA-Z0-9_-]{11})(\S*)'
    )
    
    match = re.match(youtube_regex, url)
    if match:
        return match.group(4)
    return None