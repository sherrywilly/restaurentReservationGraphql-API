from graphene_django.filter import DjangoFilterConnectionField
import graphene
import graphql
from graphql.error.base import GraphQLError
from .type import CategoryNode, ItemNode, LocationNode, RestaurantNode
from .models import Location, Restaurant


class Query(graphene.ObjectType):
    all_location = DjangoFilterConnectionField(LocationNode)
    get_restaurants_by_location = graphene.Field(
        LocationNode, location_id=graphene.Int())
    get_items_by_restaurant = graphene.Field(
        RestaurantNode, restaurant_id=graphene.Int())

    def resolve_get_items_by_restaurant(self, info, restaurant_id):
        try:
            __x = Restaurant.objects.get(pk=restaurant_id)
        except Exception as e:
            print(e)
            raise GraphQLError(e)
        return __x

    def resolve_get_restaurants_by_location(self, info, location_id):
        try:
            __x = Location.objects.get(id=location_id)
        except Exception as e:
            print(e)
            raise GraphQLError(e)
        return __x




schema = graphene.Schema(query=Query)
