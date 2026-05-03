from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Manufaktura Piekna Marta Wojcicka SEO v1.11 + Ikony")

# ==========================================
# KONFIGURACJA BIZNESOWA & LINKI
# ==========================================
PAGE_TITLE = "Makijaż Permanentny i Fine Line Tattoo Giżycko | Manufaktura Piękna Marta Wójcicka"
META_DESCRIPTION = "Profesjonalny makijaż permanentny brwi, ust i kresek oraz subtelne tatuaże Fine Line w Giżycku. Zapraszam do Manufaktury Piękna Marty Wójcickiej - najwyższa jakość i precyzja."
KEYWORDS = "makijaż permanentny Giżycko, Marta Wójcicka, makijaż permanentny brwi, makijaż permanentny ust, fine line tattoo Giżycko, Manufaktura Piękna, tatuaż Giżycko"

FACEBOOK_URL = "https://www.facebook.com/manufakturapieknamartawojcicka/" 
INSTAGRAM_URL = "https://www.instagram.com/manufakturapieknamartawojcicka/" 
LOGO_URL = "https://i.postimg.cc/0y9L49dN/znak-wodny-zloty.png"

# DOCELOWY LINK DO KALENDARZA NA SUBDOMENIE:
ADMIN_URL = "https://rezerwacje.mpmwojcicka.pl" 

# ==========================================
# TELEMETRIA & AUTORYZACJA GOOGLE
# ==========================================
GOOGLE_ANALYTICS_ID = "G-HC1LYB5Y7Z" # Pamiętaj o podmianie na swój kod GA4
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
            position: relative;
        }}

        /* STYL PRZYCISKU ADMIN */
        .admin-link {{
            position: absolute;
            top: 20px;
            right: 20px;
            color: rgba(214, 211, 209, 0.3);
            text-decoration: none;
            font-size: 0.75rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            transition: color 0.3s ease;
            z-index: 100;
        }}
        
        .admin-link:hover {{
            color: var(--gold);
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
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
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
        
        .cta-button svg {{
            width: 22px;
            height: 22px;
            fill: currentColor;
            transition: transform 0.4s ease;
        }}

        .cta-button:hover {{
            background-color: var(--gold);
            color: var(--bg);
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(212, 175, 55, 0.2);
        }}
        
        .cta-button:hover svg {{
            transform: scale(1.1);
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
    <a href="{ADMIN_URL}" class="admin-link">Admin</a>
    
    <div class="container">
        <img src="{LOGO_URL}" alt="Manufaktura Piękna Marta Wójcicka" class="logo">
        
        <h1>Manufaktura Piękna<br>Marta Wójcicka</h1>
        <h2>Makijaż Permanentny & Fine Line Tattoo</h2>
        
        <p>{META_DESCRIPTION}</p>
        
        <div class="button-group">
            <a href="{FACEBOOK_URL}" class="cta-button" target="_blank" rel="noopener">
                <svg viewBox="0 0 320 512" xmlns="http://www.w3.org/2000/svg"><path d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z"/></svg>
                Odwiedź Facebook
            </a>
            <a href="{INSTAGRAM_URL}" class="cta-button" target="_blank" rel="noopener">
                <svg viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg"><path d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"/></svg>
                Obejrzyj Instagram
            </a>
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