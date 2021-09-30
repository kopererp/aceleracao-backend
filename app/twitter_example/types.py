from app.documents import TwitterMessage as TwitterMessageDocument
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType


class TwitterMessage(MongoengineObjectType):
    class Meta:
        model = TwitterMessageDocument
        interfaces = (Node,)
