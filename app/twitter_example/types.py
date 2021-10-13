from graphene.relay import Node
from graphene_mongo import MongoengineObjectType

from app.documents import TwitterMessage as TwitterMessageDocument


class TwitterMessage(MongoengineObjectType):
    class Meta:
        model = TwitterMessageDocument
        interfaces = (Node,)
