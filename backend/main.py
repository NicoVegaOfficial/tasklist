from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import task

app = FastAPI()

#Configuraciones
origins = [
   "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Routers
app.include_router(task.app)
