# Video Processing Software Project Plan

## Goals
- Create a comprehensive video processing tool that:
  - Downloads videos from YouTube or uses local video files
  - Extracts and transcribes audio with speaker diarization
  - Detects and captures unique slides from presentations
  - Performs OCR on slides to extract text
  - Generates structured Markdown documents with all processed content
- Implement a clean vertical slice architecture for maintainability

## Architecture
- **Vertical Slice Architecture (VSA)** with isolated features
- Each feature will have its own directory with code and documentation

### Directory Structure
```
project_root/
├── features/
│   ├── video_input_handling/
│   │   ├── __init__.py
│   │   ├── video_input.py
│   │   ├── tests/
│   │   │   └── test_video_input.py
│   │   └── docs/
│   │       └── video_input_notes.md
│   ├── audio_extraction/
│   │   ├── __init__.py
│   │   ├── audio_extraction.py
│   │   ├── tests/
│   │   │   └── test_audio_extraction.py
│   │   └── docs/
│   │       └── audio_extraction_notes.md
│   ├── transcription_diarization/
│   │   ├── __init__.py
│   │   ├── transcription.py
│   │   ├── diarization.py
│   │   ├── tests/
│   │   │   └── test_transcription_diarization.py
│   │   └── docs/
│   │       └── transcription_diarization_notes.md
│   ├── slide_detection_capture/
│   │   ├── __init__.py
│   │   ├── slide_detection.py
│   │   ├── tests/
│   │   │   └── test_slide_detection.py
│   │   └── docs/
│   │       └── slide_detection_notes.md
│   ├── ocr_processing/
│   │   ├── __init__.py
│   │   ├── ocr.py
│   │   ├── tests/
│   │   │   └── test_ocr.py
│   │   └── docs/
│   │       └── ocr_notes.md
│   ├── markdown_generation/
│   │   ├── __init__.py
│   │   ├── markdown_generator.py
│   │   ├── tests/
│   │   │   └── test_markdown_generation.py
│   │   └── docs/
│   │       └── markdown_generation_notes.md
│   ├── video_downloader/           # Original downloader feature
│   │   ├── cli.py
│   │   ├── downloader.py
│   │   ├── alt_downloader.py
│   │   ├── validation.py
│   │   ├── tests/
│   │   └── docs/
│   └── playlist_downloader/        # New feature for playlist support
│       ├── __init__.py
│       ├── playlist_downloader.py
│       ├── playlist_validation.py
│       ├── tests/
│       └── docs/
├── docs/
│   ├── project_architecture.md
│   ├── testing_report.md            # New document for test results
│   └── contribution_guidelines.md
├── main.py
├── requirements.txt
├── .env
├── .env.sample
├── .gitignore
└── README.md
```

## Dependencies
- pytube - For YouTube video downloading
- python-dotenv - For environment variable management
- click - For command line interface
- yt-dlp - Alternative YouTube downloader (optional, installed on demand)
- moviepy - For audio extraction
- whisper - For transcription
- pyannote.audio - For speaker diarization
- pyscenedetect - For slide detection
- opencv-python - For image capture and processing
- pytesseract - For OCR
- ffmpeg - External dependency for audio/video processing

## TODOs

### Completed
- [DONE] Create basic project structure
- [DONE] Set up virtual environment and dependencies
- [DONE] Create entry point (main.py)
- [DONE] Implement URL validation
- [DONE] Implement core video download functionality
- [DONE] Create command-line interface
- [DONE] Add support for quality selection
- [DONE] Add progress reporting
- [DONE] Implement alternative downloader using yt-dlp
- [DONE] Document usage in feature documentation
- [DONE] Document API limitations and alternatives
- [DONE] Create basic video processing pipeline structure
- [DONE] Implement video input handling module
- [DONE] Implement audio extraction module
- [DONE] Implement transcription and diarization modules
- [DONE] Implement slide detection and capture module
- [DONE] Implement OCR processing module
- [DONE] Implement markdown generation module
- [DONE] Add support for subtitles/captions download
- [DONE] Implement download resume capability

### 1. Performance Test Results and Dependencies
- [DONE] Document test results in `docs/testing_report.md`
- [DONE] Install FFmpeg in development environment for proper testing
- [DONE] Test audio extraction performance on sample videos
- [DONE] Test transcript accuracy against known content
- [DONE] Evaluate slide detection efficiency and quality
- [TODO] Test OCR accuracy on different presentation styles

### 2. Documentation and Research
- [ ] Research and document Whisper usage details in `features/transcription_diarization/docs/`
- [ ] Research and document pyannote.audio setup in `features/transcription_diarization/docs/`
- [ ] Research and document PySceneDetect parameters in `features/slide_detection_capture/docs/`
- [TODO] Research and document Tesseract OCR setup in `features/ocr_processing/docs/`
- [DONE] Document Markdown format in `features/markdown_generation/docs/`
- [TODO] Research playlist API limitations in `features/playlist_downloader/docs/`

### 3. Testing
- [DONE] Implement tests for video input handling in `features/video_input_handling/tests/`
- [DONE] Implement tests for audio extraction in `features/audio_extraction/tests/`
- [DONE] Implement tests for transcription in `features/transcription_diarization/tests/`
- [ ] Implement tests for diarization in `features/transcription_diarization/tests/`
- [DONE] Implement tests for slide detection in `features/slide_detection_capture/tests/`
- [TODO] Implement tests for OCR processing in `features/ocr_processing/tests/`
- [DONE] Implement tests for markdown generation in `features/markdown_generation/tests/`
- [DONE] Implement tests for playlist downloader in `features/playlist_downloader/tests/`

### 4. Playlist Downloader Implementation
- [DONE] Create playlist downloader feature directory structure
- [DONE] Implement playlist URL validation in `features/playlist_downloader/playlist_validation.py`
- [DONE] Implement playlist metadata extraction (title, author, video count)
- [DONE] Implement playlist download functionality in `features/playlist_downloader/playlist_downloader.py`
- [DONE] Add CLI commands for playlist operations in `features/playlist_downloader/cli.py`
- [DONE] Integrate with existing video downloader feature (maintain isolation)
- [DONE] Add progress tracking for playlist downloads
- [DONE] Add support for partial playlist downloads (ranges)
- [DONE] Add support for excluding specific videos from playlist

### 5. Integration and Enhancements
- [DONE] Test end-to-end pipeline with sample videos
- [ ] Add support for configuration file to customize processing
- [DONE] Add progress reporting during processing
- [DONE] Enhance error handling and recovery
- [ ] Add support for batch processing multiple videos
- [ ] Add support for video chapter detection

### 6. Installation and Setup Requirements
- [DONE] FFmpeg installation for audio extraction
- [TODO] Tesseract OCR installation for text extraction from slides
- [TODO] pyannote.audio setup with HuggingFace API token for speaker diarization

### 7. UI/UX
- [DONE] Create a simple CLI interface for the video processing pipeline
- [ ] Add interactive mode for configuring processing options
- [ ] Add a web interface for processing videos

## Success Metrics
- **Transcription**: Word Error Rate (WER) < 20%
- **Diarization**: >80% accuracy in speaker identification
- **Slide Detection**: >90% of unique slides captured
- **OCR**: >85% text accuracy on clear slides
- **Usability**: Positive feedback on setup and output readability
- **Playlist Downloading**: >95% of videos successfully downloaded from playlists

## Security Considerations
- Never store API keys or credentials in the codebase
- Validate all user inputs
- Use secure and relative paths for downloads
- Store any required API keys (YouTube, transcription services) in `.env`

## Future Enhancements
- [TODO] Add a graphical user interface (GUI)
- [TODO] Support for batch downloading from a list of URLs
- [DONE] Add support for playlist downloading 

## Current Implementation Status
- Video downloading (YouTube): ✅ Working with both pytube and yt-dlp
- Video input handling (local files): ✅ Working
- Audio extraction: ✅ Working with FFmpeg (requires installation)
- Transcription: ✅ Working with Whisper
- Speaker diarization: ⚠️ Partially working (needs pyannote.audio installation)
- Slide detection: ✅ Working
- OCR text extraction: ⚠️ Implemented but requires Tesseract OCR installation
- Markdown generation: ✅ Working
- End-to-end pipeline: ✅ Basic functionality working

## Test Videos
- [Rick Astley - Never Gonna Give You Up](https://www.youtube.com/watch?v=dQw4w9WgXcQ) - Music video with lyrics
- [The Net Ninja - Python OOP Tutorial](https://youtu.be/SUiWfhAhgQw) - Education video with slides
- [Alex Hormozi - Outworking Everyone](https://youtu.be/gD0X-PLax5I?si=IbVQh8BvMBG6nthu) - Motivational video about work ethic
- [Jimmy Bogard - Vertical Slice Architecture](https://youtu.be/SUiWfhAhgQw?si=tsh-1uDqWXeC5GuK) - Architecture presentation about moving from layered architecture to vertical slice architecture, covering patterns, tools, and techniques
- Local video files in downloads/ directory

## Test Results

### Test Case: The Net Ninja - Python OOP Tutorial
- **Video Type**: Educational/presentation
- **Duration**: ~60 minutes
- **Download Performance**: Successfully downloaded using yt-dlp
- **Audio Extraction**: Completed successfully with FFmpeg
- **Transcription**: 
  - Whisper model performed well on technical content
  - Generated approximately 2,000 lines of transcribed text
  - Word accuracy appears high for technical terms
  - Speaker identification missing due to lack of pyannote.audio setup
- **Slide Detection**:
  - Successfully detected multiple slides from the presentation
  - Educational content with code examples was properly captured
  - Detected approximately 30+ unique slides
- **OCR**: 
  - Failed due to missing Tesseract installation
  - Placeholder text added to output markdown
- **Markdown Generation**:
  - Successfully generated comprehensive markdown document
  - Well-structured with table of contents
  - Transcription organized with timestamps
  - Slides properly linked and displayed
  - Estimated file size: ~100KB for markdown, plus slide images

### Test Case: Rick Astley - Never Gonna Give You Up
- **Video Type**: Music video
- **Duration**: 3:33
- **Download Performance**: Fast download with yt-dlp
- **Audio Extraction**: Successfully extracted audio with FFmpeg
- **Transcription**: 
  - Accurately transcribed lyrics
  - Proper segmentation of vocals vs. instrumental sections
- **Slide Detection**:
  - Detected 14 scene changes/key frames
  - Primarily detected changes in camera angles and scenes
- **OCR**: 
  - Not applicable for this content type
  - Failed due to missing Tesseract installation
- **Markdown Generation**: 
  - Successfully generated markdown with transcribed lyrics
  - Scene screenshots properly included

## Installation Notes
- FFmpeg can be installed via:
  - Windows: Using ffmpeg-downloader or manual installation from https://www.gyan.dev/ffmpeg/builds/
  - Linux: `sudo apt install ffmpeg` or `sudo yum install ffmpeg`
  - macOS: `brew install ffmpeg`
- Tesseract OCR can be installed from: https://github.com/UB-Mannheim/tesseract/wiki