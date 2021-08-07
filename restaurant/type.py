from graphene.types import interface
from graphene_django import DjangoObjectType
from graphene import Node
from .models import Category, Location, Restaurant, RestaurantCategory, Item


class LocationNode(DjangoObjectType):
    class Meta:
        model = Location
        interfaces = (Node,)
        filter_fields = ['name', ]


class RestaurantCategoryNode(DjangoObjectType):
    class Meta:
        model = RestaurantCategory
        interfaces = (Node,)


class RestaurantNode(DjangoObjectType):
    class Meta:
        model = Restaurant
        interfaces = (Node,)
        filter_fields = ['name', 'status', ]


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        interfaces = (Node,)
        filter_fields = ['name', 'shop', ]


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        interfaces = (Node,)
        filter_fields = ['name', 'category']
