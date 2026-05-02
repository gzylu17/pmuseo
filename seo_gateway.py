from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Manufaktura Piekna SEO Gateway")

# ==========================================
# KONFIGURACJA BIZNESOWA (ZOPTYMALIZOWANA DLA BRANŻY BEAUTY)
# ==========================================
PAGE_TITLE = "Makijaż Permanentny i Fine Line Tattoo Giżycko | Manufaktura Piękna"
META_DESCRIPTION = "Profesjonalny makijaż permanentny brwi, ust i kresek oraz subtelne tatuaże Fine Line w Giżycku. Manufaktura Piękna Marta Wójcicka. Odwiedź nasz profil i umów się na wizytę!"
KEYWORDS = "makijaż permanentny Giżycko, makijaż permanentny brwi Giżycko, makijaż permanentny ust, kreski permanentne, fine line tattoo Giżycko, najlepszy makijaż permanentny, studio makijażu, Manufaktura Piękna, Marta Wójcicka, PMU Giżycko, delikatny tatuaż"
FACEBOOK_URL = "https://www.facebook.com/manufakturapieknamartawojcicka/" 

# Paleta kolorów Premium Beauty (Grafit i Złoto)
BG_COLOR = "#1c1917" 
ACCENT_COLOR = "#d4af37" 

# ==========================================
# SILNIK GENEROWANIA HTML5
# ==========================================
HTML_TEMPLATE = f"""
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{META_DESCRIPTION}">
    <meta name="keywords" content="{KEYWORDS}">
    <meta name="author" content="Marta Wójcicka">
    <title>{PAGE_TITLE}</title>
    
    <meta property="og:title" content="{PAGE_TITLE}">
    <meta property="og:description" content="{META_DESCRIPTION}">
    <meta property="og:type" content="business.business">
    <meta property="og:url" content="{FACEBOOK_URL}">
    
    <style>
        :root {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background-color: {BG_COLOR};
            color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }}
        .container {{
            text-align: center;
            background: #292524;
            padding: 3.5rem;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
            max-width: 650px;
            width: 90%;
            border: 1px solid #44403c;
        }}
        h1 {{
            font-size: 2.2rem;
            margin-bottom: 1rem;
            color: {ACCENT_COLOR};
            font-weight: 300;
            letter-spacing: 1px;
        }}
        p {{
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 2.5rem;
            color: #d6d3d1;
            font-weight: 300;
        }}
        .cta-button {{
            display: inline-block;
            background-color: transparent;
            color: {ACCENT_COLOR};
            text-decoration: none;
            padding: 1rem 2.5rem;
            font-size: 1.1rem;
            font-weight: bold;
            border-radius: 4px;
            border: 2px solid {ACCENT_COLOR};
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .cta-button:hover {{
            background-color: {ACCENT_COLOR};
            color: {BG_COLOR};
            transform: translateY(-2px);
        }}
        .footer-note {{
            margin-top: 2rem;
            font-size: 0.8rem;
            color: #78716c;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{PAGE_TITLE.split(' | ')[1]}</h1>
        <h2>Makijaż Permanentny & Fine Line Tattoo</h2>
        <p>{META_DESCRIPTION}</p>
        
        <a href="{FACEBOOK_URL}" class="cta-button" rel="noopener noreferrer">
            Przejdź do Portfolio na Facebooku
        </a>
        
        <div class="footer-note">
            Nastąpi bezpieczne przekierowanie na oficjalny profil.
        </div>
    </div>
</body>
</html>
"""

# ==========================================
# ENDPOINTY API
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def serve_landing_page():
    return HTML_TEMPLATE