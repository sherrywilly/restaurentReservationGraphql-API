import graphene
from graphene import Node
from graphene.types import interface
from graphene_django import DjangoObjectType
from .models import Booking,BookingItem

class BookingNode(DjangoObjectType):
    class Meta:
        model = Booking
        interfaces = ('Node',)
        filter_fields = ('restaurant','user','date',)

class BookingItemNode(DjangoObjectType):
    class Meta:
        model = BookingItem
        interfaces =(Node,)
        filter_fields = ('order',)


