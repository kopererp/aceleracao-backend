from fastapi import FastAPI
from graphene import Schema
from starlette.graphql import GraphQLApp

from .events import on_application_shutdown, on_application_startup
from .schema import Mutation, Query

app = FastAPI()

app.add_event_handler("startup", on_application_startup)
app.add_event_handler("shutdown", on_application_shutdown)

schema = Schema(query=Query, mutation=Mutation)
app.add_route("/", GraphQLApp(schema=schema, graphiql=False))
