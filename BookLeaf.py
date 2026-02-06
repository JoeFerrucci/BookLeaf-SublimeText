import sublime
import sublime_plugin
import os
from datetime import datetime


def get_settings():
    """Load BookLeaf settings."""
    return sublime.load_settings("BookLeaf.sublime-settings")


def get_storage_path():
    """Get the BookLeaf storage folder path, creating it if needed."""
    packages_path = sublime.packages_path()
    storage_path = os.path.join(packages_path, "User", "BookLeaf")

    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    return storage_path


def get_all_files():
    """Get all files in the BookLeaf storage folder, sorted by modification time (newest first)."""
    storage_path = get_storage_path()
    files = []

    for filename in os.listdir(storage_path):
        filepath = os.path.join(storage_path, filename)
        if os.path.isfile(filepath):
            mtime = os.path.getmtime(filepath)
            files.append((filename, filepath, mtime))

    # Sort by modification time, newest first
    files.sort(key=lambda x: x[2], reverse=True)
    return files


def get_file_preview(filepath, max_lines=3):
    """Get the first few lines of a file for preview."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = []
            for i, line in enumerate(f):
                if i >= max_lines:
                    break
                lines.append(line.rstrip())
            return " | ".join(lines) if lines else "(empty file)"
    except Exception:
        return "(unable to read)"


class BookLeafCommand(sublime_plugin.WindowCommand):
    """Main BookLeaf command - shows Quick Panel with all files and option to create new."""

    def run(self):
        self.files = get_all_files()
        settings = get_settings()
        show_preview = settings.get("show_file_preview", True)
        preview_lines = settings.get("preview_max_lines", 3)

        # Build Quick Panel items
        self.items = []

        # First item: create new file
        self.items.append(sublime.QuickPanelItem(
            trigger="+ New File",
            details="Create a new scratch file",
            kind=(sublime.KIND_ID_COLOR_GREENISH, "+", "")
        ))

        # Add existing files
        for filename, filepath, mtime in self.files:
            if show_preview:
                preview = get_file_preview(filepath, preview_lines)
            else:
                preview = ""

            # Format modification time
            mod_time = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")

            self.items.append(sublime.QuickPanelItem(
                trigger=filename,
                details=preview,
                annotation=mod_time,
                kind=(sublime.KIND_ID_COLOR_LIGHT, "B", "")
            ))

        self.window.show_quick_panel(
            self.items,
            self.on_done,
            sublime.KEEP_OPEN_ON_FOCUS_LOST,
            placeholder="Search files or create new..."
        )

    def on_done(self, index):
        if index == -1:
            return

        if index == 0:
            # Create new file
            self.window.run_command("book_leaf_new")
        else:
            # Open selected file
            _, filepath, _ = self.files[index - 1]
            self.window.open_file(filepath)


class BookLeafNewCommand(sublime_plugin.WindowCommand):
    """Create a new BookLeaf scratch file."""

    def run(self):
        settings = get_settings()
        date_format = settings.get("date_format", "%Y-%m-%d_%H%M%S")

        # Generate default name with timestamp
        default_name = datetime.now().strftime(date_format)

        self.window.show_input_panel(
            "File name:",
            default_name,
            self.on_done,
            None,
            None
        )

    def on_done(self, name):
        if not name:
            return

        settings = get_settings()
        extension = settings.get("default_extension", ".md")

        # Add extension if not present
        if not os.path.splitext(name)[1]:
            name = name + extension

        storage_path = get_storage_path()
        filepath = os.path.join(storage_path, name)

        # Create the file if it doesn't exist
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("")

        self.window.open_file(filepath)


class BookLeafSearchCommand(sublime_plugin.WindowCommand):
    """Search BookLeaf files by content."""

    def run(self):
        self.files = get_all_files()
        self.matches = []

        # Index all files with their content
        for filename, filepath, mtime in self.files:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Get first line as preview
                    first_line = content.split("\n")[0][:100] if content else "(empty)"
                    self.matches.append({
                        "filename": filename,
                        "filepath": filepath,
                        "content": content,
                        "preview": first_line,
                        "mtime": mtime
                    })
            except Exception:
                continue

        # Build Quick Panel items
        self.items = []
        for match in self.matches:
            mod_time = datetime.fromtimestamp(match["mtime"]).strftime("%Y-%m-%d %H:%M")
            self.items.append(sublime.QuickPanelItem(
                trigger=match["filename"],
                details=match["preview"],
                annotation=mod_time,
                kind=(sublime.KIND_ID_COLOR_LIGHT, "B", "")
            ))

        if not self.items:
            sublime.status_message("BookLeaf: No files found")
            return

        self.window.show_quick_panel(
            self.items,
            self.on_done,
            sublime.KEEP_OPEN_ON_FOCUS_LOST,
            placeholder="Search file contents..."
        )

    def on_done(self, index):
        if index == -1:
            return

        filepath = self.matches[index]["filepath"]
        self.window.open_file(filepath)


class BookLeafDeleteCommand(sublime_plugin.WindowCommand):
    """Delete a BookLeaf file (with confirmation)."""

    def run(self):
        self.files = get_all_files()

        if not self.files:
            sublime.status_message("BookLeaf: No files to delete")
            return

        # Build Quick Panel items
        self.items = []
        for filename, filepath, mtime in self.files:
            mod_time = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
            self.items.append(sublime.QuickPanelItem(
                trigger=filename,
                details="Select to delete",
                annotation=mod_time,
                kind=(sublime.KIND_ID_COLOR_REDISH, "X", "")
            ))

        self.window.show_quick_panel(
            self.items,
            self.on_select,
            sublime.KEEP_OPEN_ON_FOCUS_LOST,
            placeholder="Select file to delete..."
        )

    def on_select(self, index):
        if index == -1:
            return

        filename, filepath, _ = self.files[index]
        self.filepath_to_delete = filepath
        self.filename_to_delete = filename

        # Show confirmation
        self.window.show_quick_panel(
            [
                sublime.QuickPanelItem(
                    trigger="Yes, delete",
                    details="Permanently delete " + filename,
                    kind=(sublime.KIND_ID_COLOR_REDISH, "!", "")
                ),
                sublime.QuickPanelItem(
                    trigger="Cancel",
                    details="Keep the file",
                    kind=(sublime.KIND_ID_COLOR_LIGHT, "-", "")
                )
            ],
            self.on_confirm
        )

    def on_confirm(self, index):
        if index == 0:
            try:
                os.remove(self.filepath_to_delete)
                sublime.status_message("BookLeaf: Deleted " + self.filename_to_delete)
            except Exception as e:
                sublime.error_message("Failed to delete file: " + str(e))


class BookLeafOpenFolderCommand(sublime_plugin.WindowCommand):
    """Open the BookLeaf storage folder in Finder."""

    def run(self):
        storage_path = get_storage_path()
        self.window.run_command("open_dir", {"dir": storage_path})
