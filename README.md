# BookLeaf

A Sublime Text 4 package for managing scratch notes and snippets as individual files with fuzzy search.

## Features

- **Quick Panel Search** - Fuzzy search across filenames AND file contents
- **Easy File Creation** - Create new scratch files with auto-generated timestamps
- **File Management** - Delete files, open storage folder
- **Configurable** - Custom file extensions, date formats, preview settings

## Installation

### Package Control (Recommended)

1. Open Command Palette (`Cmd+Shift+P` on macOS)
2. Select "Package Control: Install Package"
3. Search for "BookLeaf"

### Manual Installation

1. Open Sublime Text's Packages folder (`Preferences > Browse Packages...`)
2. Clone this repository: `git clone https://github.com/YOUR_USERNAME/BookLeaf-SublimeText.git BookLeaf`

## Usage

| Command | Shortcut | Description |
|---------|----------|-------------|
| BookLeaf: Open | `Cmd+Shift+B` | Open Quick Panel to search/create files |
| BookLeaf: New File | - | Create a new scratch file |
| BookLeaf: Search Contents | - | Search file contents |
| BookLeaf: Delete File | - | Delete a scratch file |
| BookLeaf: Open Storage Folder | - | Open storage folder in Finder |

## Settings

`Preferences > Package Settings > BookLeaf > Settings`

```json
{
    // Default file extension: ".md", ".txt", ".json"
    "default_extension": ".md",

    // Date format for auto-generated filenames
    "date_format": "%Y-%m-%d_%H%M%S",

    // Show file content preview in Quick Panel
    "show_file_preview": true,

    // Number of lines to show in preview
    "preview_max_lines": 3
}
```

## Storage Location

Files are stored in: `~/Library/Application Support/Sublime Text/Packages/User/BookLeaf/`

## Requirements

- Sublime Text 4 (Build 4074+)
- Python 3.8 (included with ST4)

## License

MIT License
