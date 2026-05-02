from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Manufaktura Piekna Marta Wojcicka SEO v1.7 GSC-Verified")

# ==========================================
# KONFIGURACJA BIZNESOWA & LINKI
# ==========================================
PAGE_TITLE = "Makijaż Permanentny i Fine Line Tattoo Giżycko | Manufaktura Piękna Marta Wójcicka"
META_DESCRIPTION = "Profesjonalny makijaż permanentny brwi, ust i kresek oraz subtelne tatuaże Fine Line w Giżycku. Zapraszam do Manufaktury Piękna Marty Wójcickiej - najwyższa jakość i precyzja."
KEYWORDS = "makijaż permanentny Giżycko, Marta Wójcicka, makijaż permanentny brwi, makijaż permanentny ust, fine line tattoo Giżycko, Manufaktura Piękna, tatuaż Giżycko"

FACEBOOK_URL = "https://www.facebook.com/manufakturapieknamartawojcicka/" 
INSTAGRAM_URL = "https://www.instagram.com/manufakturapieknamartawojcicka" 
LOGO_URL = "https://i.postimg.cc/0y9L49dN/znak-wodny-zloty.png"

# ==========================================
# TELEMETRIA & AUTORYZACJA GOOGLE (ZAKTUALIZOWANE)
# ==========================================
GOOGLE_ANALYTICS_ID = "G-XXXXXXXXXX" 
# TWOJA WERYFIKACJA GOOGLE:
GOOGLE_VERIFICATION_ID = "A8-zrO-QuWPykQu2KzEvQrOpbAjcjRjbNSzBZNNldt0"

BG_COLOR = "#0a0a0a" 
ACCENT_COLOR = "#d4af37" 

# ==========================================
# SILNIK GENEROWANIA HTML5 & CSS3
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
    
    <meta name="google-site-verification" content="{GOOGLE_VERIFICATION_ID}" />
    
    <meta property="og:title" content="{PAGE_TITLE}">
    <meta property="og:description" content="{META_DESCRIPTION}">
    <meta property="og:type" content="website">
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400&family=Playfair+Display:wght@400;600&display=swap" rel="stylesheet">
    
    <script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GOOGLE_ANALYTICS_ID}');
    </script>
    
    <style>
        :root {{
            --bg: {BG_COLOR};
            --gold: {ACCENT_COLOR};
        }}
        
        body {{
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, var(--bg) 0%, #1c1917 100%);
            color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
        }}
        
        .container {{
            text-align: center;
            background: rgba(28, 25, 23, 0.7);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            padding: 4rem 2rem;
            border-radius: 15px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.6);
            max-width: 600px;
            width: 100%;
            border: 1px solid rgba(212, 175, 55, 0.2);
        }}

        .logo {{
            width: auto;
            max-width: 320px;
            height: auto;
            margin-bottom: 30px;
            filter: drop-shadow(0 0 10px rgba(212, 175, 55, 0.4));
        }}

        h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 2.2rem;
            margin-bottom: 0.5rem;
            color: var(--gold);
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            line-height: 1.2;
        }}
        
        h2 {{
            font-size: 1rem;
            color: #a8a29e;
            font-weight: 300;
            margin-bottom: 2.5rem;
            letter-spacing: 3px;
            text-transform: uppercase;
        }}

        p {{
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 3rem;
            color: #d6d3d1;
            font-weight: 300;
        }}
        
        .button-group {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        
        .cta-button {{
            display: inline-block;
            background-color: transparent;
            color: var(--gold);
            text-decoration: none;
            padding: 1.2rem;
            font-size: 0.95rem;
            border-radius: 5px;
            border: 1px solid var(--gold);
            transition: all 0.4s ease;
            text-transform: uppercase;
            letter-spacing: 2px;
            font-weight: 400;
        }}
        
        .cta-button:hover {{
            background-color: var(--gold);
            color: var(--bg);
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
        }}

        .footer-note {{
            margin-top: 3rem;
            font-size: 0.75rem;
            color: #57534e;
            letter-spacing: 1px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <img src="{LOGO_URL}" alt="Manufaktura Piękna Marta Wójcicka" class="logo">
        
        <h1>Manufaktura Piękna<br>Marta Wójcicka</h1>
        <h2>Makijaż Permanentny & Fine Line Tattoo</h2>
        
        <p>{META_DESCRIPTION}</p>
        
        <div class="button-group">
            <a href="{FACEBOOK_URL}" class="cta-button" target="_blank" rel="noopener">Odwiedź Facebook</a>
            <a href="{INSTAGRAM_URL}" class="cta-button" target="_blank" rel="noopener">Obejrzyj Instagram</a>
        </div>
        
        <div class="footer-note">
            Oficjalny profil biznesowy • Giżycko
        </div>
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def serve_landing_page():
    return HTML_TEMPLATE