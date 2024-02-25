import requests
import webbrowser
from datetime import datetime

ADMIN_PASSWORD = "admin123"
SAVE_VOTER_DATA_URL = "http://localhost:8080/voting_system/save_voter_data.php"
GET_VOTER_DETAILS_URL = "http://localhost:8080/voting_system/get_voter_details.php"
REMOVE_VOTER_URL = "http://localhost:8080/voting_system/remove_voter_data_from.php"
COUNT_VOTE_URL = "http://localhost:8080/voting_system/count_vote.php"
VOTE_NOW_URL = "http://localhost:8080/voting_system/votr.php"

class VoterInfo:
    def __init__(self, aadhar, name, birth_date):
        self.aadhar = aadhar
        self.name = name
        self.birth_date = birth_date

def open_url_in_browser(url):
    webbrowser.open_new(url)

def send_voter_data_to_php(voter, admin_password):
    post_fields = {
        "aadhar": voter.aadhar,
        "name": voter.name,
        "birth_date": voter.birth_date,
        "admin_password": admin_password
    }
    response = requests.post(SAVE_VOTER_DATA_URL, data=post_fields)
    if response.status_code != 200:
        print("Failed to send voter data.")

def parse_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj
    except ValueError:
        return None

def voter_insert(admin_password):
    print("\nEnter AADHAR ID: ")
    aadhar = input()
    print("Enter Name: ")
    name = input()
    print("Enter Birth Date (dd-mm-yyyy): ")
    birth_date_str = input()

    birth_date = parse_date(birth_date_str)
    if birth_date is None:
        print("Invalid birth date format.")
        return

    age = (datetime.now() - birth_date).days // 365
    if age < 18:
        print("Voter must be at least 18 years old.")
        return

    temp_voter = VoterInfo(aadhar, name, birth_date_str)
    send_voter_data_to_php(temp_voter, admin_password)

def admin_view_voter_details():
    password = input("\nEnter Admin Password: ")
    if password != ADMIN_PASSWORD:
        print("\nIncorrect password. Access denied.")
        return

    response = requests.get(GET_VOTER_DETAILS_URL)
    if response.status_code == 200:
        print("\n===== Voter Details =====")
        print(response.text)
    else:
        print("Failed to fetch voter details.")

def remove_voter():
    password = input("\nEnter Admin Password: ")
    if password != ADMIN_PASSWORD:
        print("\nIncorrect password. Access denied.")
        return

    aadhar = input("Enter AADHAR ID of voter to remove: ")
    post_fields = {"aadhar": aadhar}
    response = requests.post(REMOVE_VOTER_URL, data=post_fields)
    if response.status_code == 200:
        print(f"Voter with AADHAR ID {aadhar} removed successfully.")
    else:
        print("Failed to remove voter.")

def count_vote(candidate):
    open_url_in_browser(COUNT_VOTE_URL)

def vote_now():
    open_url_in_browser(VOTE_NOW_URL)

def main():
    admin_password = input("Enter Admin Password: ")
    while True:
        print("\n\n===== Online Voting System =====")
        print("1. Voter Insertion")
        print("2. Admin View Voter Details")
        print("3. Remove Voter")
        print("4. Count Vote")
        print("5. Vote Now")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            voter_insert(admin_password)
        elif choice == "2":
            admin_view_voter_details()
        elif choice == "3":
            remove_voter()
        elif choice == "4":
            count_vote("vote")
        elif choice == "5":
            vote_now()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
