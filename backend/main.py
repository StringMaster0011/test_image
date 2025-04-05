import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.routes.item_routes import router as item_router
from app.postgres import database


@asynccontextmanager
async def lifespan(app:FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

# Allow requests from your frontend (React, for example)
origins = [
    "http://localhost:5173",  # React dev server
    "http://localhost:3000"  # another common port
    # "https://your-frontend-domain.com",  # in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # You can also use ["*"] for all origins (less secure)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# API routes
app.include_router(item_router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port="8000")