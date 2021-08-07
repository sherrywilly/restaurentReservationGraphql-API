from users.type import UserType
import graphene
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistrationMutation(graphene.Mutation):
    class Arguments:
        phone = graphene.String()
        email = graphene.String()
        password = graphene.String()
    ok = graphene.Boolean()
    user = graphene.Field(UserType)

    
    @staticmethod
    def mutate(root, info, phone, email, password):
        user = User.objects.create_user(phone, email, password)
        return UserRegistrationMutation(ok=True, user=user)




