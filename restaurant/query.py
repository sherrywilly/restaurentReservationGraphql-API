from graphene_django.filter import DjangoFilterConnectionField
import graphene
import graphql
from graphql.error.base import GraphQLError
from .type import CategoryNode,ItemNode,LocationNode,RestaurantNode
from .models import Location

class Query(graphene.ObjectType):
    all_location = DjangoFilterConnectionField(LocationNode)
    get_restaurants_by_location = graphene.Field(LocationNode,location_id=graphene.Int())


    def resolve_get_restaurants_by_location(self,info,location_id):
        try:
           x = Location.objects.get(id = location_id)
        except Exception as e:
            print(e)
            raise GraphQLError(e)
        return x

schema = graphene.Schema(query=Query)