# Project Architecture

This project is built using **Vertical Slice Architecture** (VSA) principles, which organize code around features or "slices" rather than technical layers.

## Vertical Slice Architecture

In contrast to traditional layered architecture (where code is organized by technical function like controllers, services, repositories), Vertical Slice Architecture organizes code by feature or business capability.

### Key Principles

1. **Feature Isolation**: Each feature is self-contained with minimal dependencies on other features.
2. **Co-location**: All code related to a feature (including controllers, services, models) is located in the same directory.
3. **Duplication over Coupling**: Some controlled code duplication is acceptable to maintain feature isolation.
4. **Explicit Dependencies**: Dependencies between features are explicit and minimized.

## Directory Structure

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

## Features Implementation

Each feature in the `features/` directory represents a vertical slice of functionality:

### Video Downloader
- Handles downloading videos from YouTube URLs
- Provides options for quality selection and output location

### Audio Extraction
- Extracts audio from video files
- Supports multiple formats and quality settings

### Transcription and Diarization
- Transcribes audio to text
- Identifies different speakers in the audio

### Slide Detection and Capture
- Detects changes in presentation slides
- Captures unique slides as images

### OCR Processing
- Extracts text from slide images
- Processes text for inclusion in documentation

### Markdown Generation
- Compiles all processed data into a structured Markdown document
- Includes transcriptions, slides, and extracted text

## Data Flow

1. User provides a YouTube URL or local video file
2. Video is downloaded (if URL) or loaded (if local)
3. Audio is extracted from the video
4. Audio is transcribed and speakers are identified
5. Video is analyzed for slide transitions
6. Unique slides are captured as images
7. OCR is performed on slide images
8. A Markdown document is generated with all processed content

## Benefits of VSA in This Project

- **Maintainability**: Features can be modified independently
- **Testability**: Features can be tested in isolation
- **Onboarding**: New developers can focus on understanding one slice at a time
- **Evolvability**: New features can be added with minimal impact on existing code