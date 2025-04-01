# Video Processing Software

A comprehensive tool for downloading YouTube videos and converting presentation videos into detailed Markdown summaries.

## Features

### Video Downloader
- Download YouTube videos with a simple command
- Choose video quality (highest, lowest, audio only)
- View video information before downloading
- Progress bar display during download
- Support for different output directories
- Dual engine support: pytube and yt-dlp (more reliable)

### Video Processing (Coming Soon)
- Process presentation videos from YouTube or local files
- Extract and transcribe audio with speaker diarization
- Detect and capture unique slides from the video
- Perform OCR on slides to extract text
- Generate a structured Markdown file with all extracted content

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/bfm92485/YouTube-Downloader-Tool.git
   cd YouTube-Downloader-Tool
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Video Downloader

Download a video with default settings (highest quality):

```
python main.py download https://youtu.be/SUiWfhAhgQw
```

Download with specific quality:

```
python main.py download https://youtu.be/SUiWfhAhgQw --quality lowest
```

Download to a specific directory:

```
python main.py download https://youtu.be/SUiWfhAhgQw --output /path/to/directory
```

Get video information without downloading:

```
python main.py download info https://youtu.be/SUiWfhAhgQw
```

Using the alternative downloader (yt-dlp - more reliable):

```
python main.py download https://youtu.be/SUiWfhAhgQw --use-alt
```

### Video Processing (Coming Soon)

Process a YouTube video into a Markdown summary:

```
python main.py process https://youtu.be/SUiWfhAhgQw /path/to/output
```

Process a local video file:

```
python main.py process /path/to/video.mp4 /path/to/output
```

## Configuration

You can create a `.env` file in the project root to set default configuration values:

```
# Video Downloader Settings
DOWNLOAD_PATH=/path/to/downloads
DEFAULT_QUALITY=highest  # Options: highest, lowest, audio_only

# Video Processing Settings
TEMP_DIR=/path/to/temp   # Temporary directory for processing files
```

## Project Structure

This project follows Vertical Slice Architecture (VSA) principles:

```
project_root/
├── features/                     # Container for all features
│   ├── feature_name/             # Individual feature slice
│   │   ├── __init__.py
│   │   ├── feature_module.py     # Feature implementation
│   │   ├── tests/                # Co-located tests
│   │   └── docs/                 # Feature-specific documentation
├── docs/                         # Project-wide documentation
├── tests/                        # Cross-feature test utilities
├── main.py                       # Application entry point
└── ... (configuration files)
```

Each feature is self-contained within its own directory, including both code and documentation. This isolation enables:
- Better maintainability as features evolve independently
- Clearer code organization by business capability
- Easier onboarding as developers can focus on one slice at a time

## Testing

Tests in this project are organized following the VSA pattern:

- **Feature-specific tests** are located within each feature's `tests/` directory
- **Cross-feature tests** are in the root `tests/` directory

To run all tests:

```
python tests/run_tests.py
```

To run tests for a specific feature:

```
python -m unittest discover features/feature_name/tests
```

## Troubleshooting

If you encounter errors with the downloader, try:

1. Use the alternative downloader with `--use-alt` flag
2. Update pytube: `pip install --upgrade pytube`
3. Try a different URL format (remove tracking parameters)

## License

MIT