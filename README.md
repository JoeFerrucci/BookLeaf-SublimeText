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
2. Clone this repository: `git clone https://github.com/JoeFerrucci/BookLeaf-SublimeText.git BookLeaf`

## Usage

All commands are available via the Command Palette (`Cmd+Shift+P`):

| Command | Description |
|---------|-------------|
| BookLeaf: Open | Open Quick Panel to search/create files |
| BookLeaf: New File | Create a new scratch file |
| BookLeaf: Search Contents | Search file contents |
| BookLeaf: Delete File | Delete a scratch file |
| BookLeaf: Open Storage Folder | Open storage folder in Finder |

## Key Bindings

No key bindings are enabled by default. To add one, open your user key bindings (`Preferences > Key Bindings`) and add:

```json
// If CMD+SHIFT+B is already tied to 'build' or something else use a chord (see below)
{ "keys": ["super+shift+b"], "command": "book_leaf" }
// Chord: Hold CMD+SHIFT and press B then L.
{ "keys": ["super+shift+b", "super+shift+l"], "command": "book_leaf" }
```

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

## License

MIT License
