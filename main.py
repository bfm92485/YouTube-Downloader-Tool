#!/usr/bin/env python3
"""
Video Processing Software
A tool that converts presentation videos into detailed Markdown summaries.
"""
import os
import sys
import argparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def download_mode():
    """Run the video downloader feature."""
    from features.video_downloader.cli import cli
    cli()

def playlist_mode():
    """Run the playlist downloader feature."""
    from features.playlist_downloader.cli import cli
    cli()

def process_mode(input_source: str, output_dir: str):
    """
    Process a video file into a Markdown summary.
    
    Args:
        input_source: YouTube URL or local video file path
        output_dir: Output directory for the Markdown file
    """
    try:
        from features.video_input_handling.video_input import get_video
        from features.audio_extraction.audio_extraction import extract_audio
        from features.transcription_diarization.transcription import transcribe
        from features.transcription_diarization.diarization import diarize
        from features.slide_detection_capture.slide_detection import detect_slides
        from features.ocr_processing.ocr import perform_ocr
        from features.markdown_generation.markdown_generator import generate_markdown
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"Processing video from: {input_source}")
        
        # Step 1: Get the video file
        print("Step 1: Obtaining video file...")
        video_path = get_video(input_source)
        print(f"Video file located at: {video_path}")
        
        # Step 2: Extract audio
        print("Step 2: Extracting audio...")
        audio_path = extract_audio(video_path)
        print(f"Audio extracted to: {audio_path}")
        
        # Step 3: Transcribe audio
        print("Step 3: Transcribing audio...")
        transcription = transcribe(audio_path)
        print("Transcription complete")
        
        # Step 4: Diarize speakers
        print("Step 4: Identifying speakers...")
        speaker_labels = diarize(audio_path, transcription)
        print("Speaker identification complete")
        
        # Step 5: Detect and capture slides
        print("Step 5: Detecting and capturing slides...")
        slide_images = detect_slides(video_path)
        print(f"Detected {len(slide_images)} slides")
        
        # Step 6: Perform OCR on slides
        print("Step 6: Extracting text from slides...")
        ocr_texts = perform_ocr(slide_images)
        print("Text extraction complete")
        
        # Step 7: Generate Markdown
        print("Step 7: Generating Markdown file...")
        markdown_file = generate_markdown(transcription, speaker_labels, slide_images, ocr_texts, output_dir)
        print(f"Markdown file generated at: {markdown_file}")
        
        print("Processing complete!")
        return markdown_file
        
    except ImportError as e:
        print(f"Error: Feature not yet implemented - {str(e)}")
        print("Please check the Project_Plan.md file for implementation status.")
        return None
    except Exception as e:
        print(f"Error during processing: {str(e)}")
        return None

def main():
    """Entry point for the application."""
    parser = argparse.ArgumentParser(description="Video Processing Software")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Download command (original functionality)
    download_parser = subparsers.add_parser("download", help="Download a YouTube video")
    
    # Playlist command (new functionality)
    playlist_parser = subparsers.add_parser("playlist", help="Download YouTube playlists")
    
    # Process command
    process_parser = subparsers.add_parser("process", help="Process a video into Markdown")
    process_parser.add_argument("input", help="YouTube URL or local video file path")
    process_parser.add_argument("output_dir", help="Output directory for processed files")
    
    args = parser.parse_args()
    
    if args.command == "download":
        download_mode()
    elif args.command == "playlist":
        playlist_mode()
    elif args.command == "process":
        process_mode(args.input, args.output_dir)
    else:
        # Default to showing help if no command specified
        parser.print_help()

if __name__ == "__main__":
    main()