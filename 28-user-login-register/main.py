import sys
import sqlite3
import os
from PyQt5 import QtWidgets


class LoginWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.create_connection()
        self.init_ui()

    def create_connection(self):
        # Database path relative to this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "login.db")

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        # Create users table if it does not exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        self.connection.commit()

        print("Database path:", db_path)

    def init_ui(self):
        # Widgets
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_button = QtWidgets.QPushButton("Login")
        self.register_button = QtWidgets.QPushButton("Register")

        # Layouts
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username_input)
        v_box.addWidget(self.password_input)
        v_box.addWidget(self.login_button)
        v_box.addWidget(self.register_button)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        # Window settings
        self.setWindowTitle("User Login & Registration")
        self.setFixedSize(300, 180)

        # Signals
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

        self.show()

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QtWidgets.QMessageBox.warning(
                self,
                "Input Error",
                "Please enter both username and password."
            )
            return

        self.cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        )

        if self.cursor.fetchone() is None:
            QtWidgets.QMessageBox.warning(
                self,
                "Login Failed",
                "User not found.\nPlease try again."
            )
        else:
            QtWidgets.QMessageBox.information(
                self,
                "Login Successful",
                f"Welcome, {username}!"
            )
            self.username_input.clear()
            self.password_input.clear()

    def register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QtWidgets.QMessageBox.warning(
                self,
                "Input Error",
                "Please enter both username and password."
            )
            return

        try:
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            self.connection.commit()
            QtWidgets.QMessageBox.information(
                self,
                "Registration Successful",
                f"User '{username}' has been registered!"
            )
            self.username_input.clear()
            self.password_input.clear()
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(
                self,
                "Registration Failed",
                "Username already exists. Choose another."
            )


# Run application
app = QtWidgets.QApplication(sys.argv)
window = LoginWindow()
sys.exit(app.exec_())
