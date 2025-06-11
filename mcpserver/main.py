from mcp.server.fastmcp import FastMCP

import os

# create an MCP server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = "notes.txt"

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")


@mcp.tool()

def add_note(message: str) -> str:

    """
    Append a new note to the sticky note file.

    Args: 
        message (str): The note content to be added.

    Returns:
        str: confirmation message indicating the note is saved.
    """

    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Note saved!"

@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from the sticky note file.

    Returns:
           str: All notes as a single string separated by line breaks.
           if no notes exists, a default message is returned.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    return content or "No notes yet."

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet."

@mcp.prompt()
def note_summary_prompt() -> str:
     
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        content = f.read().strip()
    if not content:
        return "There are no notes yet."
    return f"Summaize the current notes: {content}"
    