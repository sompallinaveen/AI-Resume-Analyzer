from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.ats import router as ats_router
from app.api.auth import router as auth_router
from app.api.home import router as home_router
from app.api.job import router as job_router
from app.api.resume import router as resume_router
from app.api.matching import router as matching_router
from app.api.ai import router as ai_router

from app.core.config import settings
from app.database.database import Base, engine

# Import models so SQLAlchemy registers them
from app.models import job, resume, user


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend API for AI Resume Analyzer",
    lifespan=lifespan,
)

# Routers
app.include_router(home_router)
app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(job_router)
app.include_router(matching_router)
app.include_router(ai_router)