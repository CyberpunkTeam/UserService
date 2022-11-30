# ENV VARS, CONSTANTS
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "server.example.com")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "test")
USER_COLLECTION = "users"
