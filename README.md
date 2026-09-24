# Latch public repair fixture

This deliberately small public repository provides honest Git and CI evidence for a Latch repair bounty on GenLayer Studionet 61999. The base parser loses embedded LF and CRLF characters by splitting input into lines before CSV parsing. Its regression tests intentionally fail. The repair must preserve `parse_csv(text: str) -> list[list[str]]`, retain the failing fixtures, and preserve quoted newlines exactly.

Run: `python -m unittest discover -s demo-target -v`.
