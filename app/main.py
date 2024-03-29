from http import HTTPStatus
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.param_functions import Header
from starlette.middleware.cors import CORSMiddleware
from app.views import view_propertie
from app.core.core import cur

app = FastAPI(title="Habi Application",
    description="Habi Application",
    version="1.0.0",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("shutdown")
async def shutdown():
    await cur.close()

app.include_router(view_propertie.router)

