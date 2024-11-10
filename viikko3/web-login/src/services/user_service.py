from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import string


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user


    def check_for_valid_password(self,password):
        if len(password) < 8:
            return "Too Short Password"
        only_letters = True
        numbers = "0123456789"
        for char in password:
            if char in numbers:
                only_letters = False
        if only_letters == False:
            return "Valid Password"
        return "Invalid Password"
        
    def check_for_valid_username(self,username):
        if len(username) < 3:
            return "Too Short Username"
        accepted_chars = string.ascii_lowercase
        contains_only_accepted_chars = True
        for char in username:
            if char not in accepted_chars:
                contains_only_accepted_chars = False
        if contains_only_accepted_chars == True:
            return "Valid Username"
        return "Invalid Username"

        
        
    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        user = self._user_repository.find_by_username(username)
        username_message = self.check_for_valid_username(username)
        password_message = self.check_for_valid_password(password)
        
        if username_message == "Too Short Username" and password_message == "Valid Password":
            raise UserInputError("Too short username!")
        if username_message == "Valid Username" and password_message == "Too Short Password":
            raise UserInputError("Too short password!")

        if username_message == "Valid Username" and password_message == "Invalid Password":
            raise UserInputError("Invalid password!")
        if username_message == "Valid Username" and password != password_confirmation:
            raise UserInputError("Nonmatching passwords!")
        
        if user:
            raise UserInputError("User already exists!")
        
            


user_service = UserService()
