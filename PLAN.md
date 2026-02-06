# BookLeaf - Sublime Text Scratch Notes Manager

## Overview
A Sublime Text 4 package for managing scratch notes/snippets as individual files with Quick Panel search and easy creation.

## User Requirements
- **Storage**: `~/Library/Application Support/Sublime Text/Packages/User/BookLeaf/`
- **Interface**: Quick Panel (fuzzy search)
- **Naming**: Prompt with pre-selected timestamp default (fully highlighted for easy replacement)
- **Format**: Configurable extension, default `.md`, support `.json`

---

## File Structure

```
BookLeaf/
├── BookLeaf.py                    # Main plugin with all commands
├── BookLeaf.sublime-commands      # Command palette entries
├── BookLeaf.sublime-settings      # Default settings
├── Default (OSX).sublime-keymap   # macOS key bindings
└── messages/
    └── install.txt                # Post-install instructions
```

---

## Implementation Plan

### 1. BookLeaf.py - Core Plugin

**Commands to implement:**

| Command | Description |
|---------|-------------|
| `book_leaf` | Main entry: Quick Panel listing all files + "New File" option |
| `book_leaf_new` | Create new file with input panel (pre-selected default name) |
| `book_leaf_search` | Search file contents via Quick Panel |

**Key Implementation Details:**

```python
# Main command - shows Quick Panel with files
class BookLeafCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get all files from storage folder
        # Build Quick Panel items: ["+ New File", file1, file2, ...]
        # Show preview of selected file content
        # On select: open file or trigger new file creation
```

```python
# New file command - input panel with pre-selected default
class BookLeafNewCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Generate default name: "2026-02-06_143022"
        # Show input_panel with default text
        # Input panel auto-selects all text (ST4 default behavior)
        # On done: create file with extension from settings
```

```python
# Search command - search file contents
class BookLeafSearchCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Index all files and their content
        # Show Quick Panel with file:snippet format
        # Fuzzy search matches filename and content
```

**Helper Functions:**
- `get_storage_path()` - Returns/creates storage folder
- `get_all_files()` - Lists all files in storage
- `get_settings()` - Load plugin settings

### 2. BookLeaf.sublime-settings

```json
{
    "default_extension": ".md",
    "date_format": "%Y-%m-%d_%H%M%S",
    "show_file_preview": true,
    "preview_max_lines": 3
}
```

### 3. BookLeaf.sublime-commands

```json
[
    { "caption": "BookLeaf: Open", "command": "book_leaf" },
    { "caption": "BookLeaf: New File", "command": "book_leaf_new" },
    { "caption": "BookLeaf: Search Contents", "command": "book_leaf_search" }
]
```

### 4. Default (OSX).sublime-keymap

```json
[
    { "keys": ["super+shift+b"], "command": "book_leaf" }
]
```

---

## Key UX Details

1. **Quick Panel Preview**: When navigating files in Quick Panel, show first few lines of content as preview (using `on_highlight` callback)

2. **Pre-selected Default Name**: ST4's `show_input_panel` automatically selects all text, so the timestamp default will be fully highlighted

3. **Storage Auto-creation**: If BookLeaf folder doesn't exist, create it on first use

4. **File Sorting**: Show most recently modified files first

5. **Content Search**: Show snippets of matching content in Quick Panel's detail line

---

## Verification

1. Install package by symlinking to ST4 Packages folder
2. Open Command Palette, run "BookLeaf: Open"
3. Create a new file, verify name input has default selected
4. Create multiple files, verify they appear in Quick Panel
5. Test content search finds text inside files
6. Verify settings (extension, date format) work correctly
