import graphene


class SuccessDelete(graphene.ObjectType):
    success = graphene.Boolean(required=True, description="Indicate success on the operation")