from assistant.repositories.UserRepository import UserRepository

class UserService:
    @staticmethod
    def register_user(data):
        return UserRepository.create_user(data=data)