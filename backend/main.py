from fastapi import FastAPI
import task

app = FastAPI()

#Routers
app.include_router(task.app)
