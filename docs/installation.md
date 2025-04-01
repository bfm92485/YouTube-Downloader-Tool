# Installation Guide

This guide will help you set up the YouTube Downloader Tool on your system.

## Prerequisites

Before installation, ensure you have the following prerequisites:

1. **Python 3.7+**: The application requires Python 3.7 or higher.
2. **pip**: Python package manager (usually included with Python).
3. **External dependencies**:
   - **FFmpeg**: Required for audio extraction and video processing
   - **Tesseract OCR**: Required for text extraction from slides (optional)

## Installing Python Dependencies

1. Clone the repository:
   ```
   git clone https://github.com/bfm92485/YouTube-Downloader-Tool.git
   cd YouTube-Downloader-Tool
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Installing External Dependencies

### FFmpeg

FFmpeg is required for audio extraction and video processing.

#### Windows

1. **Using a package manager (recommended)**:
   ```
   # Using Chocolatey
   choco install ffmpeg
   
   # Using Scoop
   scoop install ffmpeg
   ```

2. **Manual installation**:
   - Download from https://www.gyan.dev/ffmpeg/builds/
   - Extract the ZIP file
   - Add the `bin` folder to your system PATH

#### macOS

```
# Using Homebrew
brew install ffmpeg
```

#### Linux

```
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

### Tesseract OCR (Optional)

Tesseract is required for OCR text extraction from slides.

#### Windows

1. Download the installer from https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer and follow the instructions
3. Add the Tesseract installation directory to your system PATH

#### macOS

```
# Using Homebrew
brew install tesseract
```

#### Linux

```
# Ubuntu/Debian
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

# Fedora
sudo dnf install tesseract
sudo dnf install tesseract-devel

# Arch Linux
sudo pacman -S tesseract
sudo pacman -S tesseract-data-eng
```

## Configuration

1. Create a `.env` file based on the provided `.env.sample`:
   ```
   cp .env.sample .env
   ```

2. Edit the `.env` file with your preferred settings:
   - Set download paths
   - Configure quality preferences
   - Set transcription settings

## Verifying Installation

Run the following command to verify that your installation is working correctly:

```
python main.py --version
```

You should see the version information displayed.

## Next Steps

- For usage instructions, refer to the [README.md](../README.md)
- For detailed feature documentation, check the documentation for each feature in their respective directories