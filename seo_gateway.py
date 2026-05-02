from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Manufaktura Piekna SEO Gateway v1.2 Premium")

# ==========================================
# KONFIGURACJA BIZNESOWA & LINKI
# ==========================================
PAGE_TITLE = "Makijaż Permanentny i Fine Line Tattoo Giżycko | Manufaktura Piękna"
META_DESCRIPTION = "Profesjonalny makijaż permanentny brwi, ust i kresek oraz subtelne tatuaże Fine Line w Giżycku. Ekskluzywne usługi w Manufakturze Piękna."
KEYWORDS = "makijaż permanentny Giżycko, makijaż permanentny brwi Giżycko, makijaż permanentny ust, kreski permanentne, fine line tattoo Giżycko, najlepszy makijaż permanentny, studio makijażu, Manufaktura Piękna, Marta Wójcicka, PMU Giżycko"

FACEBOOK_URL = "https://www.facebook.com/manufakturapieknamartawojcicka/" 
INSTAGRAM_URL = "https://www.instagram.com/manufakturapieknamartawojcicka" 

# Zmienna przechowująca Logo. Obecnie zawiera wygenerowany matematycznie elegancki złoty monogram MP.
LOGO_URL = "data:image/svg+xml;charset=UTF-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'%3E%3Ccircle cx='60' cy='60' r='58' fill='none' stroke='%23d4af37' stroke-width='2'/%3E%3Ctext x='60' y='75' font-family='serif' font-size='45' fill='%23d4af37' text-anchor='middle'%3EMP%3C/text%3E%3C/svg%3E"

# Paleta kolorów Premium Beauty
BG_COLOR = "#0a0a0a" 
ACCENT_COLOR = "#d4af37" 

# ==========================================
# SILNIK GENEROWANIA HTML5 & CSS3 (PREMIUM)
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
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400&family=Playfair+Display:wght@400;600&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --bg-color: {BG_COLOR};
            --accent-color: {ACCENT_COLOR};
        }}
        body {{
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, var(--bg-color) 0%, #1c1917 100%);
            color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
            overflow-x: hidden;
        }}
        
        /* Animacja wejścia */
        @keyframes fadeInDown {{
            from {{ opacity: 0; transform: translateY(-30px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .container {{
            text-align: center;
            /* Efekt matowego szkła (Glassmorphism) */
            background: rgba(30, 30, 30, 0.6);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            padding: 4rem 3rem;
            border-radius: 12px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
            max-width: 650px;
            width: 100%;
            border: 1px solid rgba(212, 175, 55, 0.15);
            animation: fadeInDown 1.2s cubic-bezier(0.2, 0.8, 0.2, 1);
        }}
        .logo {{
            width: 110px;
            height: auto;
            margin-bottom: 25px;
            border-radius: 50%;
            box-shadow: 0 0 25px rgba(212, 175, 55, 0.1);
        }}
        h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 2.2rem;
            margin-bottom: 0.5rem;
            color: var(--accent-color);
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}
        h2 {{
            font-size: 1.1rem;
            color: #a8a29e;
            font-weight: 300;
            margin-bottom: 2.5rem;
            letter-spacing: 3px;
            text-transform: uppercase;
        }}
        p {{
            font-size: 1.05rem;
            line-height: 1.8;
            margin-bottom: 3rem;
            color: #d6d3d1;
            font-weight: 300;
        }}
        .button-group {{
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin-bottom: 2rem;
        }}
        .cta-button {{
            display: inline-block;
            background-color: transparent;
            color: var(--accent-color);
            text-decoration: none;
            padding: 1.2rem 2rem;
            font-size: 0.95rem;
            font-weight: 400;
            border-radius: 4px;
            border: 1px solid var(--accent-color);
            transition: all 0.4s ease;
            text-transform: uppercase;
            letter-spacing: 2px;
            width: 100%;
            box-sizing: border-box;
            position: relative;
            overflow: hidden;
        }}
        .cta-button:hover {{
            background-color: var(--accent-color);
            color: var(--bg-color);
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
        }}
        .footer-note {{
            margin-top: 3rem;
            font-size: 0.75rem;
            color: #57534e;
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
    </style>
</head>
<body>
    <div class="container">
        <img src="{LOGO_URL}" alt="Manufaktura Piękna Logo" class="logo">
        
        <h1>Manufaktura Piękna</h1>
        <h2>Permanent Makeup & Fine Line</h2>
        <p>{META_DESCRIPTION}</p>
        
        <div class="button-group">
            <a href="{FACEBOOK_URL}" class="cta-button" rel="noopener noreferrer">
                Odwiedź Profil na Facebooku
            </a>
            <a href="{INSTAGRAM_URL}" class="cta-button" rel="noopener noreferrer">
                Obejrzyj Portfolio Instagram
            </a>
        </div>
        
        <div class="footer-note">
            Bezpieczny węzeł przekierowujący zoptymalizowany dla algorytmów wyszukiwania.
        </div>
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def serve_landing_page():
    return HTML_TEMPLATE