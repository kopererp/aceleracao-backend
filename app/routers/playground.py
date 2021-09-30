from app.settings import templates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def playground(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("playground.html", {"request": request})
