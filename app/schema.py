from graphene_django import DjangoObjectType
import graphene
from .models import Info

class Movie(DjangoObjectType):
    class Meta:
        model = Info

class Query(graphene.ObjectType):
    allmovies = graphene.List(Movie)

    @graphene.resolve_only_args
    def resolve_allmovies(self):
        return Info.objects.all()

schema = graphene.Schema(query=Query)