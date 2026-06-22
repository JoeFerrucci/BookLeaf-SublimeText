# BookLeaf

A Sublime Text 4 package for managing scratch notes and snippets as individual files with fuzzy search.

## Features

- **Quick Panel Search** - Fuzzy search across filenames AND file contents
- **Easy File Creation** - Create new scratch files with auto-generated timestamps, or save an unsaved tab directly into BookLeaf
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

All commands are available via the Command Palette (`Cmd+Shift+P`) or keyboard shortcuts:

| Command | Shortcut | Description |
|---------|----------|-------------|
| BookLeaf: Open | `Cmd+Shift+B`, `Cmd+Shift+L` | Browse and open scratch files |
| BookLeaf: New File | `Cmd+Shift+B`, `Cmd+Shift+N` | Create a new scratch file, or save the current unsaved tab to BookLeaf |
| BookLeaf: Search Contents | `Cmd+Shift+B`, `Cmd+Shift+S` | Search file contents |
| BookLeaf: Delete File | `Cmd+Shift+B`, `Cmd+Shift+D` | Delete a scratch file |
| BookLeaf: Open Storage Folder | | Open storage folder in Finder |

## Key Bindings

Default chord bindings are included but commented out. To enable them, go to `Preferences > Package Settings > BookLeaf > Key Bindings` and uncomment the bindings you want.

To customize or add your own, open your user key bindings (`Preferences > Key Bindings`):

```json
{ "keys": ["super+shift+b", "super+shift+l"], "command": "book_leaf" },
{ "keys": ["super+shift+b", "super+shift+n"], "command": "book_leaf_new" },
{ "keys": ["super+shift+b", "super+shift+s"], "command": "book_leaf_search" },
{ "keys": ["super+shift+b", "super+shift+d"], "command": "book_leaf_delete" }
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
