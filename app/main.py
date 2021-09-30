from fastapi import FastAPI
from graphene import Schema
from starlette.graphql import GraphQLApp

from .events import on_application_shutdown, on_application_startup
from .routers import playground
from .schema import Mutation, Query

app = FastAPI()

app.add_event_handler("startup", on_application_startup)
app.add_event_handler("shutdown", on_application_shutdown)

app.include_router(playground.router, prefix="/playground", tags=["playground"])


schema = Schema(query=Query, mutation=Mutation)
app.add_route("/", GraphQLApp(schema=schema, graphiql=False))
