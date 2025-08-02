# BookBot 📚

A Python command-line tool that analyzes text files and generates detailed reports on word counts and character frequency statistics.

## Features

- **Word Count Analysis**: Counts total words in any text file
- **Character Frequency Analysis**: Tracks how often each letter appears
- **Smart Sorting**: Displays characters from most to least frequent
- **Clean Output**: Generates formatted reports with clear sections
- **Command-Line Interface**: Easy to use with any text file

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/AndyGuffey/bookbot.git
   cd bookbot
   ```

2. Ensure you have Python 3.x installed

## Usage

Run BookBot with any text file:

```bash
python main.py books/frankenstein.txt
```

### Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77536 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
...
============= END ===============
```

## Project Structure

```
bookbot/
├── main.py          # Main application entry point
├── stats.py         # Statistical analysis functions
├── books/           # Directory for text files
│   └── frankenstein.txt
└── README.md
```

## About

BookBot is my first project from [Boot.dev](https://www.boot.dev) - a hands-on introduction to Python programming, file handling, and data analysis!

## What I Learned

- File I/O operations in Python
- Dictionary manipulation and sorting
- Command-line argument handling with `sys.argv`
- Function organization and imports
- String processing and character analysis
