from orders.models import Booking
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .type import BookingNode, BookingItemNode


class Query(graphene.ObjectType):
    all_order_by_user = graphene.List(BookingNode, id=graphene.Int())

    def resolve_all_order_by_user(self, info, id):
        user = info.context.user
        __orders = Booking.objects.filter(user_id=id)
        return __orders
