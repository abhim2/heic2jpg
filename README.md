# HEIC to JPG Converter

A Windows application that converts HEIC image files to JPEG format with right-click context menu integration.

## Features

- Convert HEIC files to JPG format
- Right-click context menu integration
- High-quality conversion (95% JPEG quality)
- Simple and easy to use

## Requirements

- Windows 10 or later
- Python 3.7 or later
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the setup script as administrator to register the context menu:
   ```
   python setup_context_menu.py
   ```

## Usage

### Using Context Menu
1. Right-click on any HEIC file
2. Select "Convert to JPG" from the context menu
3. The converted JPG file will be created in the same directory as the original file

### Using Command Line
You can also convert files directly using the command line:
```
python heic2jpg.py path/to/your/image.heic
```

## Uninstallation

To remove the context menu integration, you'll need to manually delete the registry keys:
1. Open Registry Editor (regedit)
2. Navigate to `HKEY_CLASSES_ROOT\*\shell\ConvertToJPG`
3. Delete the `ConvertToJPG` key

## License

This project is open source and available under the MIT License. 