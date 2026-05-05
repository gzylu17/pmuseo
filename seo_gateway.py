from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI(title="Render 301 Redirect Gateway")

@app.get("/{path:path}")
async def redirect_to_seohost(path: str, request: Request):
    """
    Krytyczny wektor SEO: Przechwytuje KAŻDY ruch wchodzący na stary adres chmury Render
    i wymusza twarde przekierowanie (HTTP 301 Moved Permanently) na docelową domenę.
    Dzięki temu Google przeniesie pozycję z wyników wyszukiwania na nowy adres.
    """
    target_url = "https://mpmwojcicka.pl/"
    return RedirectResponse(url=target_url, status_code=301)