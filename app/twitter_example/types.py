import graphene

from app.documents import TwitterMessage as TwitterMessageDocument
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType


class TwitterMessage(MongoengineObjectType):
    class Meta:
        model = TwitterMessageDocument
        interfaces = (Node,)


class SuccessDelete(graphene.ObjectType):
    success = graphene.Boolean(
        required=True, description="Indicate success on the operation"
    )
