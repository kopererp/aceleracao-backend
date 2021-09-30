import graphene


class Hello(graphene.ObjectType):
    message = graphene.String(required=True, description="Welcome message")


class SayHello(graphene.Mutation):
    class Arguments:
        your_name = graphene.String(required=True, description="Your name")

    Output = Hello

    def mutate(self, info, your_name: str) -> Hello:
        return Hello(message=f"Hello {your_name}")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello")


class Mutation(graphene.ObjectType):
    say_hello = SayHello.Field()
