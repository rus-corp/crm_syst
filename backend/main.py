from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os

from apps.client_app.app_router import router as client_router
from apps.program_app.app_router import router as program_router
from apps.payments_app.router import router as payment_router
from apps.hotels_app.hotels.routers import router as hotel_routers
from apps.hotels_app.hotel_rooms.routers import router as room_routers
from apps.commands.router import router as command_router
from apps.staff.main_router import router as staff_router
from apps.partner_app.router import router as partner_router
from apps.program_rooms_app.routers import router as program_room_router
from apps.users.router import router as user_router
from apps.auth.routers import router as auth_router


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

# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     print(f"Request: {request.method} {request.url} - {request.client}")
#     print(request.body)
#     response = await call_next(request)
#     return response
  

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
app.include_router(staff_router)
app.include_router(partner_router)
app.include_router(program_room_router)
app.include_router(user_router)
app.include_router(auth_router)