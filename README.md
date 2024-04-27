# Country Data Management System

This project is a Python-based system for managing country data, including information such as country names, codes, populations, and regions. It includes functionality to create and populate a database with country data from an external source, as well as to perform various operations on the data.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Country Data Management System provides a set of Python scripts to manage country data stored in a SQLite database. It allows users to create and populate the database with country data retrieved from an external JSON file, perform various operations on the data, and generate statistics about regions and countries.

## Requirements

To run this project, you need:

- Python 3.x
- SQLite (if not already installed)
- Requests library (for fetching data from the external source)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Noman1555/DCR-python-test.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DCR-python-test
   ```

3. (Optional) Set up a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate  # For Unix/Linux
   # OR
   .\env\Scripts\activate   # For Windows
   ```

4. Install dependencies from requirements.txt:

   ```bash
   pip3 install -r requirements.txt
   ```

## Usage

### Populating the Database

To create and populate the database with country data from an external JSON file, run the following command:

```bash
cd src
```

```bash
python3 load_data.py
```

### Running Operations

To perform operations on the country data, such as listing all countries or generating statistics for regions, you can run the respective scripts:

```bash
python3 list_countries.py
python3 stats.py
```

### Project Structure

- `data/`: Contains external data files (`countries.json`, `countries.db`)
- `src/`: Contains Python scripts for database management and data operations
  - `create_db.py`: Script to create the database schema
  - `db.py`: Contains database connection and management classes
  - `list_countries.py`: Script to list all countries in the database
  - `load_data.py`: Script to populate the database with country data
  - `stats.py`: Script to generate statistics for regions
- `README.md`: This README file
---
