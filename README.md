# Onlinevotingsytem-PHP-PY

```markdown
# Online Voting System

This is a simple online voting system implemented using Python for the GUI, PHP for server-side processing, and MySQL for database management.

## Features

- Admin authentication
- Voter registration
- Viewing voter details
- Removing voters
- Vote counting
- Voting interface for users

## Prerequisites

- Python 3
- PHP
- MySQL

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/adhimiw/online-voting-system.git
   ```

2. Import the MySQL database:
   - Execute the SQL script provided in `database.sql` to create the necessary tables.

3. Configure PHP files:
   - Modify the PHP files (`save_voter_data.php`, `get_voter_details.php`, `remove_voter_data_from.php`, `count_vote.php`, `votr.php`) to connect to your MySQL database and adjust any other settings if necessary.

4. Start the server:
   - Ensure that your PHP server is running.

5. Run the Python GUI:
   ```bash
   cd online-voting-system
   python main.py
   ```

## Usage

- Upon running the Python GUI (`main.py`), follow the on-screen instructions to navigate through the system.
- Admin login is required to access administrative features.
- Voters can register themselves using the provided interface.

## Screenshots

![image](https://github.com/adhimiw/Onlinevotingsytem-PHP-PY/assets/121428949/b0a21be1-f5ed-4233-b57a-3525adeba238)
![image](https://github.com/adhimiw/Onlinevotingsytem-PHP-PY/assets/121428949/10e50d3f-169f-4a45-8f2f-1d56bcfc0b50)


## License

GPL-3.0 license



```

**SQL Files:**
- `database.sql`: This file contains SQL commands to create the necessary tables in your MySQL database. Users should execute this script in their MySQL environment to set up the database for the online voting system.

**PHP Files:**
- `save_voter_data.php`: PHP script to handle saving voter data to the database.
- `get_voter_details.php`: PHP script to fetch voter details from the database.
- `remove_voter_data_from.php`: PHP script to remove voter data from the database.
- `count_vote.php`: PHP script to count votes from the database.
- `votr.php`: PHP script to handle the voting interface for users.

You can include these files in your GitHub repository with appropriate modifications as per your system setup.
