from fastapi import FastAPI
from .routers import users, state, locations

app = FastAPI()


app.include_router(users.router)
app.include_router(state.router)
app.include_router(locations.router)
