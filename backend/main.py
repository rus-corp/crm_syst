from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from apps.client_app.client.routers import router as client_router
from apps.program_app.routers import router as program_router
from apps.payments_app.router import router as payment_router
from apps.hotels_app.hotels.routers import router as hotel_routers
from apps.hotels_app.hotel_rooms.routers import router as room_routers
from apps.commands.router import router as command_router


app = FastAPI(
  title='Astro',
  root_path='/api'
)

origins = [
    "*",
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:57172",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:57172",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



base_dir = os.path.dirname(os.path.abspath(__file__))
static_root = os.path.join(base_dir, 'static')

if not os.path.exists(static_root):
  os.makedirs(static_root)


@app.get("/")
def root():
  return {"message": "Hello World"}

# app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(client_router)
app.include_router(program_router)
app.include_router(payment_router)
app.include_router(hotel_routers)
app.include_router(room_routers)
app.include_router(command_router)