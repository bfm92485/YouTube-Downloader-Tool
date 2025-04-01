"""Module for extracting audio from video files."""
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

# Debug info for troubleshooting
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

# Simplified MoviePy import approach with better error handling
try:
    import moviepy
    import moviepy.editor
    from moviepy.editor import VideoFileClip
    print(f"MoviePy version: {moviepy.__version__}")
    USING_MOVIEPY = True
except ImportError as e:
    print(f"MoviePy import error: {e}")
    USING_MOVIEPY = False

# Define constants
DEFAULT_AUDIO_FORMAT = "wav"  # Best for transcription
DEFAULT_AUDIO_CODEC = "pcm_s16le"  # 16-bit PCM, good for speech recognition
DEFAULT_AUDIO_CHANNELS = 1  # Mono, best for transcription
DEFAULT_AUDIO_SAMPLE_RATE = 16000  # 16kHz, common for speech recognition


def check_ffmpeg() -> bool:
    """
    Check if ffmpeg is installed.
    
    Returns:
        True if ffmpeg is installed, False otherwise
    """
    try:
        result = subprocess.run(
            ["ffmpeg", "-version"], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            check=False
        )
        print(f"FFmpeg found: {result.stdout.decode()[:50]}...")
        return True
    except FileNotFoundError:
        print("FFmpeg not found in PATH")
        return False


def extract_audio_ffmpeg(
    video_path: str,
    output_dir: Optional[str] = None,
    audio_format: str = DEFAULT_AUDIO_FORMAT,
    audio_codec: str = DEFAULT_AUDIO_CODEC,
    channels: int = DEFAULT_AUDIO_CHANNELS,
    sample_rate: int = DEFAULT_AUDIO_SAMPLE_RATE,
) -> str:
    """
    Extract audio from a video file using ffmpeg.
    
    Args:
        video_path: Path to the video file
        output_dir: Directory to save the audio file (defaults to same directory as video)
        audio_format: Audio format (e.g., wav, mp3)
        audio_codec: Audio codec (e.g., pcm_s16le for WAV)
        channels: Number of audio channels (1 for mono, 2 for stereo)
        sample_rate: Audio sample rate in Hz
        
    Returns:
        Path to the extracted audio file
    """
    video_path = Path(video_path)
    
    if output_dir is None:
        output_dir = video_path.parent
    else:
        output_dir = Path(output_dir)
        os.makedirs(output_dir, exist_ok=True)
    
    # Generate output filename
    output_filename = f"{video_path.stem}.{audio_format}"
    output_path = output_dir / output_filename
    
    # Build ffmpeg command
    cmd = [
        "ffmpeg",
        "-i", str(video_path),
        "-vn",  # No video
        "-acodec", audio_codec,
        "-ac", str(channels),
        "-ar", str(sample_rate),
        "-y",  # Overwrite output files
        str(output_path)
    ]
    
    print(f"Running FFmpeg command: {' '.join(cmd)}")
    
    # Run ffmpeg
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"FFmpeg extraction successful. Output: {output_path}")
        return str(output_path)
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        print(f"FFmpeg failed with error: {error_msg}")
        raise RuntimeError(f"FFmpeg failed: {error_msg}")


def extract_audio_moviepy(
    video_path: str, 
    output_dir: Optional[str] = None,
    audio_format: str = DEFAULT_AUDIO_FORMAT
) -> str:
    """
    Extract audio from a video file using moviepy.
    
    Args:
        video_path: Path to the video file
        output_dir: Directory to save the audio file (defaults to same directory as video)
        audio_format: Audio format (e.g., wav, mp3)
        
    Returns:
        Path to the extracted audio file
    """
    global USING_MOVIEPY
    
    if not USING_MOVIEPY:
        print("MoviePy was not successfully imported during module initialization")
        raise ImportError("MoviePy is not available. Install with: pip install moviepy")
    
    video_path = Path(video_path)
    
    if output_dir is None:
        output_dir = video_path.parent
    else:
        output_dir = Path(output_dir)
        os.makedirs(output_dir, exist_ok=True)
    
    # Generate output filename
    output_filename = f"{video_path.stem}.{audio_format}"
    output_path = output_dir / output_filename
    
    print(f"Starting MoviePy audio extraction for {video_path}")
    
    # Extract audio
    try:
        video = VideoFileClip(str(video_path))
        if video.audio is None:
            raise ValueError("Video has no audio track")
            
        audio = video.audio
        
        # Save audio
        if audio_format.lower() == "wav":
            print(f"Writing WAV audio file to {output_path}")
            audio.write_audiofile(
                str(output_path), 
                codec=DEFAULT_AUDIO_CODEC,
                fps=DEFAULT_AUDIO_SAMPLE_RATE,
                nbytes=2,  # 16-bit
                ffmpeg_params=["-ac", str(DEFAULT_AUDIO_CHANNELS)]
            )
        else:
            print(f"Writing {audio_format} audio file to {output_path}")
            audio.write_audiofile(str(output_path))
        
        # Close resources
        audio.close()
        video.close()
        
        print(f"MoviePy extraction successful. Output: {output_path}")
        return str(output_path)
    except Exception as e:
        print(f"MoviePy audio extraction failed: {str(e)}")
        raise RuntimeError(f"MoviePy audio extraction failed: {str(e)}")


def extract_audio(
    video_path: str,
    output_dir: Optional[str] = None,
    audio_format: str = DEFAULT_AUDIO_FORMAT,
    force_ffmpeg: bool = False
) -> str:
    """
    Extract audio from a video file.
    
    This function first tries to use ffmpeg directly if available.
    If ffmpeg is not available or fails, it falls back to moviepy if installed.
    
    Args:
        video_path: Path to the video file
        output_dir: Directory to save the audio file (defaults to same directory as video)
        audio_format: Audio format (e.g., wav, mp3)
        force_ffmpeg: If True, only use ffmpeg, don't fall back to moviepy
        
    Returns:
        Path to the extracted audio file
    """
    # Check if video file exists
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    print(f"Extracting audio from video: {video_path}")
    print(f"Output directory: {output_dir or 'same as video'}")
    print(f"Audio format: {audio_format}")
    
    # Try ffmpeg first
    has_ffmpeg = check_ffmpeg()
    if has_ffmpeg:
        try:
            return extract_audio_ffmpeg(
                video_path=video_path,
                output_dir=output_dir,
                audio_format=audio_format
            )
        except Exception as e:
            if force_ffmpeg:
                raise
            print(f"FFmpeg extraction failed: {e}. Trying MoviePy...")
    elif force_ffmpeg:
        raise RuntimeError("FFmpeg is not installed but force_ffmpeg=True")
    elif not USING_MOVIEPY:
        raise RuntimeError("Neither FFmpeg nor MoviePy are available. Please install one of them.")
    
    # Fall back to moviepy
    return extract_audio_moviepy(
        video_path=video_path,
        output_dir=output_dir,
        audio_format=audio_format
    )