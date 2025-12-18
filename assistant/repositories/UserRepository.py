from django.contrib.auth.models import User

class UserRepository:
    @staticmethod
    def get_by_id(user_id):
        return User.objects.filter(id=user_id).first()
    
    @staticmethod
    def create_user(**data):
        return User.objects.create(**data)