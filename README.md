# Python Backup Script

A Python script for creating backups of websites. This script reads a CSV file or backups all files in the current directory (excluding specified files) and compresses them into a ZIP archive.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `wpbackup.py` file.
3. Prepare a CSV file named `toBackup.csv` (if you want to backup specific websites) or place the script in the directory where you want to backup all files.
4. Run the script using the following command:

   ```bash
   python wpbackup.py
   ```

## Features

- Backs up websites specified in a CSV file or all files in the current directory.
- Creates a timestamped backup in ZIP format.
- Moves the backup file to the specified destination directory.

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `wpbackup.py` file.
2. Ensure you have Python 3.x installed on your system.

## Configuration

The script supports the following configuration options:

- `DONTBACKUP`: A list of files or directories to exclude from the backup process.
- `Backup()` class options:
  - `sitename`: Name of the website or file to backup.
  - `dest_path`: Destination directory to store the backup files (default: "BACKUPS").
  - `format`: Backup file format (default: "zip").

## Examples

1. Backup specific websites listed in `toBackup.csv`:

   ```python
   python wpbackup.py
   ```

2. Backup all files in the current directory (excluding specified files):

   ```python
   python wpbackup.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## Acknowledgements

- [Python](https://www.python.org/) - Programming language used.
- [OpenAI](https://www.openai.com/) - GPT-3.5 language model used to generate this README.

🚀 Happy backing up! 🌟
