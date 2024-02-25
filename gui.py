import sys
import requests
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QSizePolicy, QInputDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Online Voting System")
        self.resize(800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.admin_password = ""

        self.create_intro_ui()

    def create_intro_ui(self):
        intro_layout = QVBoxLayout()

        intro_label = QLabel()
        pixmap = QPixmap("intro_image.jpg")
        pixmap = pixmap.scaled(400, 300, Qt.KeepAspectRatio)
        intro_label.setPixmap(pixmap)
        intro_label.setAlignment(Qt.AlignCenter)

        quote_label = QLabel("Here are some inspirational quotes:")
        quote_label.setStyleSheet("font-size: 16pt; font-family: Arial; font-style: italic;")
        quote_text = QTextEdit()
        quote_text.setReadOnly(True)
        quote_text.setStyleSheet("font-size: 12pt; font-family: Times New Roman;")
        quote_text.setPlainText("Your vote is your voice.\n\nDemocracy is not a spectator sport\n\nThe ballot is stronger than the bullet.")

        intro_layout.addWidget(intro_label)
        intro_layout.addWidget(quote_label)
        intro_layout.addWidget(quote_text)

        self.layout.addLayout(intro_layout)

        continue_button = QPushButton("Continue")
        continue_button.clicked.connect(self.show_login_ui)
        self.layout.addWidget(continue_button)

    def show_login_ui(self):
        self.clear_layout()
        self.create_login_ui()

    def create_login_ui(self):
        login_layout = QVBoxLayout()
        login_label = QLabel("Enter Admin Password:")
        self.password_input = QLineEdit()
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        login_layout.addWidget(login_label)
        login_layout.addWidget(self.password_input)
        login_layout.addWidget(login_button)

        self.layout.addLayout(login_layout)

    def login(self):
        self.admin_password = self.password_input.text()
        if self.admin_password == ADMIN_PASSWORD:
            self.clear_layout()
            self.create_main_ui()
        else:
            QMessageBox.warning(self, "Login Failed", "Incorrect password. Access denied.")

    def create_main_ui(self):
        main_layout = QVBoxLayout()

        # Create buttons for each option
        options_layout = QHBoxLayout()
        button_texts = ["Voter Insert", "Admin View Voter Details", "Remove Voter", "Count Vote", "Vote Now", "Close"]
        buttons = []
        for text in button_texts:
            button = QPushButton(text)
            button.clicked.connect(self.process_option)
            buttons.append(button)

        options_layout.addStretch(1)  # Add stretch to push buttons to the sides
        for button in buttons:
            options_layout.addWidget(button)
        options_layout.addStretch(1)  # Add stretch to push buttons to the sides

        main_layout.addLayout(options_layout)

        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        main_layout.addWidget(self.output_display)

        self.layout.addLayout(main_layout)

    def process_option(self):
        button_text = self.sender().text()
        if button_text == "Voter Insert":
            self.voter_insert()
        elif button_text == "Admin View Voter Details":
            self.admin_view_voter_details()
        elif button_text == "Remove Voter":
            self.remove_voter()
        elif button_text == "Count Vote":
            self.count_vote()
        elif button_text == "Vote Now":
            self.vote_now()
        elif button_text == "Close":
            self.close()
        else:
            self.output_display.append("Invalid option! Please try again.")

    def voter_insert(self):
        self.insert_window = VoterInsertWindow()
        self.insert_window.show()

    def remove_voter(self):
        self.remove_window = RemoveVoterWindow()
        self.remove_window.show()

    def send_voter_data_to_php(self, voter):
        post_fields = {
            "aadhar": voter.aadhar,
            "name": voter.name,
            "birth_date": voter.birth_date,
            "admin_password": self.admin_password
        }
        response = requests.post(SAVE_VOTER_DATA_URL, data=post_fields)
        if response.status_code == 200:
            self.output_display.append("Voter information sent successfully.")
        else:
            self.output_display.append("Failed to send voter data.")

    def admin_view_voter_details(self):
        response = requests.get(GET_VOTER_DETAILS_URL)
        if response.status_code == 200:
            self.output_display.append("\n===== Voter Details =====\n")
            self.output_display.append(response.text)
        else:
            self.output_display.append("Failed to fetch voter details.")

    def count_vote(self):
        webbrowser.open_new_tab(COUNT_VOTE_URL)

    def vote_now(self):
        webbrowser.open_new_tab(VOTE_NOW_URL)

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

class VoterInsertWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voter Insert")
        self.resize(400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.aadhar_input = QLineEdit()
        self.name_input = QLineEdit()
        self.birth_date_input = QLineEdit()

        layout.addWidget(QLabel("AADHAR ID:"))
        layout.addWidget(self.aadhar_input)
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Birth Date (dd-mm-yyyy):"))
        layout.addWidget(self.birth_date_input)

        insert_button = QPushButton("Insert Voter")
        insert_button.clicked.connect(self.insert_voter)
        layout.addWidget(insert_button)

    def insert_voter(self):
        aadhar = self.aadhar_input.text()
        name = self.name_input.text()
        birth_date = self.birth_date_input.text()

        temp_voter = VoterInfo(aadhar, name, birth_date)
        post_fields = {
            "aadhar": temp_voter.aadhar,
            "name": temp_voter.name,
            "birth_date": temp_voter.birth_date,
            "admin_password": ADMIN_PASSWORD
        }
        response = requests.post(SAVE_VOTER_DATA_URL, data=post_fields)
        if response.status_code == 200:
            QMessageBox.information(self, "Success", "Voter information sent successfully.")
        else:
            QMessageBox.warning(self, "Error", "Failed to send voter data.")

class RemoveVoterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remove Voter")
        self.resize(300, 150)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.aadhar_input = QLineEdit()

        layout.addWidget(QLabel("Enter AADHAR ID of voter to remove:"))
        layout.addWidget(self.aadhar_input)

        remove_button = QPushButton("Remove Voter")
        remove_button.clicked.connect(self.remove_voter)
        layout.addWidget(remove_button)

    def remove_voter(self):
        aadhar = self.aadhar_input.text()
        post_fields = {"aadhar": aadhar}
        response = requests.post(REMOVE_VOTER_URL, data=post_fields)
        if response.status_code == 200:
            QMessageBox.information(self, "Success", f"Voter with AADHAR ID {aadhar} removed successfully.")
        else:
            QMessageBox.warning(self, "Error", "Failed to remove voter.")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
