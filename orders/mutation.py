from typing_extensions import Required
from restaurant.models import Restaurant
import graphene
from .type import BookingNode,BookingItemNode
from .models import Item,BookingItem

class BookingItemType(graphene.InputObjectType):
    pass

class OrderMutation(graphene.Mutation):
    class Arguments:
        restaurant = graphene.String(required=True)
        guest = graphene.Int(required=True)
        date = graphene.Date(required=True)
        time = graphene.Time(required=True)
    
    @classmethod
    def mutate(cls,self,info,restaurant,guest,date,time):
        pass