import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

BASE_DIR = r"C:\Users\bruno\.gemini\antigravity\scratch\postres-navidenos"
BRAIN_DIR = r"C:\Users\bruno\.gemini\antigravity\brain\4625a942-b87a-400c-9c2c-b7f293274965"

# Fonts
font_bold_path = "C:\\Windows\\Fonts\\arialbd.ttf"
font_impact = "C:\\Windows\\Fonts\\impact.ttf"

def get_font(path, size):
    return ImageFont.truetype(path, size)

# ═══════════════════════════════════════════════════════════
# CRIATIVO 1: A MATEMÁTICA DO LUCRO
# ═══════════════════════════════════════════════════════════

def create_criativo_1():
    """CRIATIVO 1: A Matemática do Lucro (Feed 1080x1080)"""
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (10, 15, 22, 255))
    
    hero_path = os.path.join(BASE_DIR, "cheesecake_frutos_rojos.jpg")
    bg = Image.open(hero_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    bg = ImageEnhance.Color(bg).enhance(1.15)
    canvas.paste(bg, (0, 0))
    
    # Overlays
    top_overlay = Image.new("RGBA", (w, 220), (5, 10, 18, 220))
    bot_overlay = Image.new("RGBA", (w, 380), (5, 10, 18, 240))
    canvas.paste(top_overlay, (0, 0), top_overlay)
    canvas.paste(bot_overlay, (0, h - 380), bot_overlay)
    
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(font_bold_path, 26)
    f_title = get_font(font_impact, 62)
    
    # 1. Top Ribbon Banner
    draw.rounded_rectangle([60, 25, w - 60, 75], radius=25, fill=(196, 30, 58, 250), outline=(255, 215, 0, 220), width=2)
    kicker_txt = "EL NEGOCIO MAS RENTABLE DE ESTA NAVIDAD"
    bbox_k = f_kicker.getbbox(kicker_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 36), kicker_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    title_txt = "CUANTO GANAS POR CADA VASITO?"
    bbox_t = f_title.getbbox(title_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2 + 2, 95 + 2), title_txt, fill=(0, 0, 0, 240), font=f_title)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 95), title_txt, fill=(255, 223, 94, 255), font=f_title)
    
    # 2. Central Math Card
    c_x1, c_y1, c_x2, c_y2 = 70, 720, w - 70, 960
    draw.rounded_rectangle([c_x1 - 4, c_y1 - 4, c_x2 + 4, c_y2 + 4], radius=24, fill=(0, 0, 0, 200))
    draw.rounded_rectangle([c_x1, c_y1, c_x2, c_y2], radius=20, fill=(18, 24, 38, 245), outline=(255, 215, 0, 230), width=3)
    
    f_item = get_font(font_bold_path, 30)
    f_badge = get_font(font_bold_path, 34)
    
    # Row 1: Costo
    draw.text((c_x1 + 40, c_y1 + 25), "Costo de Preparacion:", fill=(210, 220, 230, 255), font=f_item)
    draw.text((c_x2 - 230, c_y1 + 25), "$0.60 USD", fill=(255, 100, 100, 255), font=f_item)
    
    # Row 2: Venta
    draw.text((c_x1 + 40, c_y1 + 80), "Precio Promedio Venta:", fill=(210, 220, 230, 255), font=f_item)
    draw.text((c_x2 - 230, c_y1 + 80), "$2.50 USD", fill=(100, 255, 150, 255), font=f_item)
    
    # Row 3: Ganancia Highlight
    draw.rounded_rectangle([c_x1 + 20, c_y1 + 135, c_x2 - 20, c_y1 + 215], radius=14, fill=(0, 168, 77, 245), outline=(255, 255, 255, 200), width=2)
    profit_txt = "GANANCIA: MAS DEL 300% POR VASITO"
    bbox_p = f_badge.getbbox(profit_txt)
    draw.text(((w - (bbox_p[2] - bbox_p[0])) // 2, c_y1 + 152), profit_txt, fill=(255, 255, 255, 255), font=f_badge)
    
    # 3. Bottom CTA Bar
    f_cta = get_font(font_bold_path, 25)
    cta_bar_y = 980
    cta_txt = "30 Recetas en Vasito + Calculadora Excel - Solo $9.90 USD"
    bbox_c = f_cta.getbbox(cta_txt)
    draw.rounded_rectangle([60, cta_bar_y, w - 60, cta_bar_y + 65], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    draw.text(((w - (bbox_c[2] - bbox_c[0])) // 2, cta_bar_y + 18), cta_txt, fill=(255, 255, 255, 255), font=f_cta)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "criativo_1_lucro_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "criativo_1_lucro_feed.jpg"), quality=95)
    print("Criativo 1 Feed created!")

def create_criativo_1_story():
    """CRIATIVO 1: A Matemática do Lucro (Story / Reels 1080x1920)"""
    w, h = 1080, 1920
    canvas = Image.new("RGBA", (w, h), (10, 15, 22, 255))
    
    hero_path = os.path.join(BASE_DIR, "cheesecake_frutos_rojos.jpg")
    bg = Image.open(hero_path).convert("RGBA")
    bg_w, bg_h = bg.size
    scale = max(w / bg_w, h / bg_h)
    new_w, new_h = int(bg_w * scale), int(bg_h * scale)
    bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    bg_cropped = bg.crop((left, top, left + w, top + h))
    canvas.paste(ImageEnhance.Color(bg_cropped).enhance(1.1), (0, 0))
    
    top_overlay = Image.new("RGBA", (w, 420), (5, 10, 18, 225))
    bot_overlay = Image.new("RGBA", (w, 650), (5, 10, 18, 240))
    canvas.paste(top_overlay, (0, 0), top_overlay)
    canvas.paste(bot_overlay, (0, h - 650), bot_overlay)
    
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(font_bold_path, 28)
    f_title = get_font(font_impact, 66)
    f_sub = get_font(font_bold_path, 34)
    
    draw.rounded_rectangle([60, 90, w - 60, 155], radius=28, fill=(196, 30, 58, 250), outline=(255, 215, 0, 220), width=2)
    kicker_txt = "NEGOCIO NAVIDEÑO RENTABLE 2024"
    bbox_k = f_kicker.getbbox(kicker_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 106), kicker_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    title_txt = "CUANTO GANAS POR VASITO?"
    bbox_t = f_title.getbbox(title_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2 + 2, 180 + 2), title_txt, fill=(0, 0, 0, 240), font=f_title)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 180), title_txt, fill=(255, 223, 94, 255), font=f_title)
    
    sub_txt = "Aprende las 30 Recetas Mas Vendidas sin Horno"
    bbox_s = f_sub.getbbox(sub_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 265), sub_txt, fill=(255, 255, 255, 255), font=f_sub)
    
    c_x1, c_y1, c_x2, c_y2 = 70, 1340, w - 70, 1680
    draw.rounded_rectangle([c_x1 - 4, c_y1 - 4, c_x2 + 4, c_y2 + 4], radius=24, fill=(0, 0, 0, 200))
    draw.rounded_rectangle([c_x1, c_y1, c_x2, c_y2], radius=20, fill=(18, 24, 38, 245), outline=(255, 215, 0, 230), width=3)
    
    f_item = get_font(font_bold_path, 34)
    f_badge = get_font(font_bold_path, 38)
    
    draw.text((c_x1 + 45, c_y1 + 35), "Costo de Preparacion:", fill=(210, 220, 230, 255), font=f_item)
    draw.text((c_x2 - 270, c_y1 + 35), "$0.60 USD", fill=(255, 100, 100, 255), font=f_item)
    
    draw.text((c_x1 + 45, c_y1 + 105), "Precio Promedio Venta:", fill=(210, 220, 230, 255), font=f_item)
    draw.text((c_x2 - 270, c_y1 + 105), "$2.50 USD", fill=(100, 255, 150, 255), font=f_item)
    
    draw.rounded_rectangle([c_x1 + 25, c_y1 + 180, c_x2 - 25, c_y1 + 285], radius=16, fill=(0, 168, 77, 245), outline=(255, 255, 255, 200), width=2)
    profit_txt = "GANANCIA: MAS DEL 300% POR VASITO"
    bbox_p = f_badge.getbbox(profit_txt)
    draw.text(((w - (bbox_p[2] - bbox_p[0])) // 2, c_y1 + 205), profit_txt, fill=(255, 255, 255, 255), font=f_badge)
    
    f_cta = get_font(font_bold_path, 32)
    cta_bar_y = 1730
    cta_txt = "TOCA AQUI PARA DESCARGAR ($9.90 USD)"
    bbox_c = f_cta.getbbox(cta_txt)
    draw.rounded_rectangle([60, cta_bar_y, w - 60, cta_bar_y + 90], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 230), width=3)
    draw.text(((w - (bbox_c[2] - bbox_c[0])) // 2, cta_bar_y + 26), cta_txt, fill=(255, 255, 255, 255), font=f_cta)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "criativo_1_lucro_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "criativo_1_lucro_story.jpg"), quality=95)
    print("Criativo 1 Story created!")

# ═══════════════════════════════════════════════════════════
# CRIATIVO 2: QUEBRA DE OBJEÇÃO (100% SEM FORNO)
# ═══════════════════════════════════════════════════════════

def create_criativo_2():
    """CRIATIVO 2: Quebra de Objeção / 100% Sem Forno (Feed 1080x1080)"""
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (15, 20, 30, 255))
    
    grid_imgs = [
        os.path.join(BASE_DIR, "mousse_chocolate.jpg"),
        os.path.join(BASE_DIR, "carlota_fresa.jpg"),
        os.path.join(BASE_DIR, "mousse_maracuya.jpg"),
        os.path.join(BASE_DIR, "chocoflan_navideno.jpg")
    ]
    
    gw, gh = 525, 340
    positions = [(10, 160), (545, 160), (10, 510), (545, 510)]
    
    for i, path in enumerate(grid_imgs):
        if os.path.exists(path):
            img_item = Image.open(path).convert("RGBA").resize((gw, gh), Image.Resampling.LANCZOS)
            mask = Image.new("L", (gw, gh), 0)
            ImageDraw.Draw(mask).rounded_rectangle([0, 0, gw, gh], radius=16, fill=255)
            canvas.paste(img_item, positions[i], mask)
            
    draw = ImageDraw.Draw(canvas)
    for pos in positions:
        draw.rounded_rectangle([pos[0], pos[1], pos[0] + gw, pos[1] + gh], radius=16, outline=(255, 215, 0, 180), width=2)
        
    f_kicker = get_font(font_bold_path, 25)
    f_title = get_font(font_impact, 58)
    
    draw.rounded_rectangle([60, 20, w - 60, 68], radius=24, fill=(196, 30, 58, 250), outline=(255, 215, 0, 220), width=2)
    kicker_txt = "APRENDE DESDE CERO - SIN EXPERIENCIA"
    bbox_k = f_kicker.getbbox(kicker_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 31), kicker_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    title_txt = "NO TIENES HORNO? NO LO NECESITAS!"
    bbox_t = f_title.getbbox(title_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2 + 2, 85 + 2), title_txt, fill=(0, 0, 0, 240), font=f_title)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 85), title_txt, fill=(255, 223, 94, 255), font=f_title)
    
    f_center = get_font(font_bold_path, 34)
    badge_y = 480
    badge_h = 75
    draw.rounded_rectangle([90, badge_y, w - 90, badge_y + badge_h], radius=20, fill=(0, 168, 77, 255), outline=(255, 255, 255, 230), width=3)
    badge_txt = "100% SIN HORNO - LISTOS EN 15 MIN"
    bbox_b = f_center.getbbox(badge_txt)
    draw.text(((w - (bbox_b[2] - bbox_b[0])) // 2, badge_y + 18), badge_txt, fill=(255, 255, 255, 255), font=f_center)
    
    f_bullet = get_font(font_bold_path, 25)
    f_offer = get_font(font_bold_path, 28)
    
    bot_y = 865
    draw.rounded_rectangle([40, bot_y, w - 40, 1045], radius=20, fill=(10, 15, 25, 245), outline=(255, 215, 0, 200), width=2)
    
    bullets = "Sin hornos costosos    |    Sin batidoras    |    Recetas Paso a Paso"
    bbox_bul = f_bullet.getbbox(bullets)
    draw.text(((w - (bbox_bul[2] - bbox_bul[0])) // 2, bot_y + 22), bullets, fill=(230, 235, 245, 255), font=f_bullet)
    
    draw.rounded_rectangle([120, bot_y + 70, w - 120, bot_y + 140], radius=16, fill=(196, 30, 58, 250), outline=(255, 255, 255, 200), width=2)
    promo_txt = "Descarga el Manual + 3 Bonos por solo $9.90 USD"
    bbox_pr = f_offer.getbbox(promo_txt)
    draw.text(((w - (bbox_pr[2] - bbox_pr[0])) // 2, bot_y + 86), promo_txt, fill=(255, 255, 255, 255), font=f_offer)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "criativo_2_sem_forno_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "criativo_2_sem_forno_feed.jpg"), quality=95)
    print("Criativo 2 Feed created!")

def create_criativo_2_story():
    """CRIATIVO 2: Quebra de Objeção / Sem Forno (Story 1080x1920)"""
    w, h = 1080, 1920
    canvas = Image.new("RGBA", (w, h), (12, 17, 26, 255))
    draw = ImageDraw.Draw(canvas)
    
    grid_imgs = [
        os.path.join(BASE_DIR, "mousse_chocolate.jpg"),
        os.path.join(BASE_DIR, "carlota_fresa.jpg"),
        os.path.join(BASE_DIR, "mousse_maracuya.jpg"),
        os.path.join(BASE_DIR, "chocoflan_navideno.jpg")
    ]
    
    gw, gh = 515, 480
    positions = [(15, 340), (550, 340), (15, 840), (550, 840)]
    
    for i, path in enumerate(grid_imgs):
        if os.path.exists(path):
            img_item = Image.open(path).convert("RGBA").resize((gw, gh), Image.Resampling.LANCZOS)
            mask = Image.new("L", (gw, gh), 0)
            ImageDraw.Draw(mask).rounded_rectangle([0, 0, gw, gh], radius=20, fill=255)
            canvas.paste(img_item, positions[i], mask)
            draw.rounded_rectangle([positions[i][0], positions[i][1], positions[i][0] + gw, positions[i][1] + gh], radius=20, outline=(255, 215, 0, 180), width=3)
            
    f_kicker = get_font(font_bold_path, 28)
    f_title = get_font(font_impact, 64)
    f_sub = get_font(font_bold_path, 34)
    
    draw.rounded_rectangle([60, 80, w - 60, 145], radius=28, fill=(196, 30, 58, 250), outline=(255, 215, 0, 220), width=2)
    kicker_txt = "APRENDE DESDE CERO - SIN EXPERIENCIA"
    bbox_k = f_kicker.getbbox(kicker_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 96), kicker_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    title_txt = "NO TIENES HORNO? NO LO NECESITAS!"
    bbox_t = f_title.getbbox(title_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2 + 2, 170 + 2), title_txt, fill=(0, 0, 0, 240), font=f_title)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 170), title_txt, fill=(255, 223, 94, 255), font=f_title)
    
    sub_txt = "30 Postres en Vasito que se Preparan en 15 Minutos"
    bbox_s = f_sub.getbbox(sub_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 250), sub_txt, fill=(255, 255, 255, 255), font=f_sub)
    
    f_center = get_font(font_bold_path, 36)
    badge_y = 800
    draw.rounded_rectangle([80, badge_y, w - 80, badge_y + 85], radius=22, fill=(0, 168, 77, 255), outline=(255, 255, 255, 240), width=3)
    badge_txt = "100% SIN HORNO - LISTOS EN 15 MIN"
    bbox_b = f_center.getbbox(badge_txt)
    draw.text(((w - (bbox_b[2] - bbox_b[0])) // 2, badge_y + 22), badge_txt, fill=(255, 255, 255, 255), font=f_center)
    
    f_bullet = get_font(font_bold_path, 30)
    f_cta = get_font(font_bold_path, 32)
    
    bot_y = 1360
    draw.rounded_rectangle([50, bot_y, w - 50, 1680], radius=24, fill=(18, 24, 38, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((90, bot_y + 40), "> Sin hornos ni tecnicas complicadas", fill=(255, 140, 140, 255), font=f_bullet)
    draw.text((90, bot_y + 105), "> Sin gastar en batidoras caras", fill=(255, 140, 140, 255), font=f_bullet)
    draw.text((90, bot_y + 170), "+ 30 Recetas Paso a Paso + 3 Bonos Gratis", fill=(100, 255, 150, 255), font=f_bullet)
    draw.text((90, bot_y + 235), "+ Precio Especial de Temporada: $9.90 USD", fill=(255, 223, 94, 255), font=f_bullet)
    
    cta_bar_y = 1730
    cta_txt = "TOCA AQUI PARA DESCARGAR ($9.90 USD)"
    bbox_c = f_cta.getbbox(cta_txt)
    draw.rounded_rectangle([60, cta_bar_y, w - 60, cta_bar_y + 90], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 230), width=3)
    draw.text(((w - (bbox_c[2] - bbox_c[0])) // 2, cta_bar_y + 26), cta_txt, fill=(255, 255, 255, 255), font=f_cta)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "criativo_2_sem_forno_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "criativo_2_sem_forno_story.jpg"), quality=95)
    print("Criativo 2 Story created!")

# ═══════════════════════════════════════════════════════════
# CRIATIVO 3: OPORTUNIDADE DE RENDA EXTRA DE NATAL
# ═══════════════════════════════════════════════════════════

def create_criativo_3():
    """CRIATIVO 3: Oportunidade de Renda Extra de Natal (Feed 1080x1080)"""
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (12, 17, 26, 255))
    
    caja_path = os.path.join(BASE_DIR, "caja_regalo.jpg")
    bg = Image.open(caja_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    canvas.paste(bg, (0, 0))
    
    overlay_top = Image.new("RGBA", (w, 230), (8, 12, 20, 225))
    overlay_bot = Image.new("RGBA", (w, 360), (8, 12, 20, 240))
    canvas.paste(overlay_top, (0, 0), overlay_top)
    canvas.paste(overlay_bot, (0, h - 360), overlay_bot)
    
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(font_bold_path, 25)
    f_title = get_font(font_impact, 58)
    f_sub = get_font(font_bold_path, 32)
    f_bonus = get_font(font_bold_path, 26)
    f_price = get_font(font_impact, 48)
    
    draw.rounded_rectangle([70, 25, w - 70, 75], radius=25, fill=(196, 30, 58, 250), outline=(255, 215, 0, 220), width=2)
    kicker_txt = "TEMPORADA NAVIDEÑA 2024 - CUPOS LIMITADOS"
    bbox_k = f_kicker.getbbox(kicker_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 36), kicker_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    title_txt = "GANA DE $300 A $800 USD ESTA NAVIDAD"
    bbox_t = f_title.getbbox(title_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2 + 2, 95 + 2), title_txt, fill=(0, 0, 0, 240), font=f_title)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 95), title_txt, fill=(255, 223, 94, 255), font=f_title)
    
    sub_txt = "Vendiendo Postres Gourmet en Vasitos desde Casa"
    bbox_s = f_sub.getbbox(sub_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 165), sub_txt, fill=(255, 255, 255, 255), font=f_sub)
    
    card_y = 740
    draw.rounded_rectangle([50, card_y, w - 50, 1030], radius=24, fill=(18, 24, 38, 250), outline=(255, 215, 0, 230), width=3)
    
    draw.text((85, card_y + 28), "+ Manual Completo: 30 Recetas en Vasito", fill=(255, 255, 255, 255), font=f_bonus)
    draw.text((85, card_y + 75), "+ Bono 1: Calculadora Excel de Costos (GRATIS)", fill=(255, 223, 94, 255), font=f_bonus)
    draw.text((85, card_y + 122), "+ Bono 2: Guia de Empaques y Fotos (GRATIS)", fill=(255, 223, 94, 255), font=f_bonus)
    draw.text((85, card_y + 169), "+ Bono 3: Estrategia de Ventas WhatsApp (GRATIS)", fill=(255, 223, 94, 255), font=f_bonus)
    draw.text((85, card_y + 216), "+ Acceso Inmediato de por Vida - Garantia 7 Dias", fill=(100, 255, 150, 255), font=f_bonus)
    
    price_box_x1 = w - 340
    price_box_y1 = card_y + 40
    price_box_x2 = w - 75
    price_box_y2 = card_y + 225
    
    draw.rounded_rectangle([price_box_x1, price_box_y1, price_box_x2, price_box_y2], radius=18, fill=(196, 30, 58, 255), outline=(255, 255, 255, 220), width=2)
    
    f_lbl = get_font(font_bold_path, 20)
    f_old = get_font(font_bold_path, 24)
    
    draw.text((price_box_x1 + 35, price_box_y1 + 18), "OFERTA HOY:", fill=(255, 223, 94, 255), font=f_lbl)
    draw.text((price_box_x1 + 45, price_box_y1 + 48), "Antes $29", fill=(240, 200, 200, 255), font=f_old)
    draw.text((price_box_x1 + 25, price_box_y1 + 80), "$9.90", fill=(255, 255, 255, 255), font=f_price)
    draw.text((price_box_x1 + 55, price_box_y1 + 145), "USD", fill=(255, 223, 94, 255), font=f_lbl)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "criativo_3_natal_oferta_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "criativo_3_natal_oferta_feed.jpg"), quality=95)
    print("Criativo 3 Feed created!")

def create_criativo_3_story():
    """CRIATIVO 3: Oportunidade de Natal (Story 1080x1920)"""
    w, h = 1080, 1920
    canvas = Image.new("RGBA", (w, h), (12, 17, 26, 255))
    
    caja_path = os.path.join(BASE_DIR, "caja_regalo.jpg")
    bg = Image.open(caja_path).convert("RGBA")
    bg_w, bg_h = bg.size
    scale = max(w / bg_w, h / bg_h)
    new_w, new_h = int(bg_w * scale), int(bg_h * scale)
    bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    bg_cropped = bg.crop((left, top, left + w, top + h))
    canvas.paste(ImageEnhance.Color(bg_cropped).enhance(1.1), (0, 0))
    
    top_overlay = Image.new("RGBA", (w, 440), (8, 12, 20, 230))
    bot_overlay = Image.new("RGBA", (w, 680), (8, 12, 20, 245))
    canvas.paste(top_overlay, (0, 0), top_overlay)
    canvas.paste(bot_overlay, (0, h - 680), bot_overlay)
    
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(font_bold_path, 28)
    f_title = get_font(font_impact, 64)
    f_sub = get_font(font_bold_path, 34)
    f_bonus = get_font(font_bold_path, 30)
    f_cta = get_font(font_bold_path, 32)
    
    draw.rounded_rectangle([70, 90, w - 70, 155], radius=28, fill=(196, 30, 58, 250), outline=(255, 215, 0, 220), width=2)
    kicker_txt = "TEMPORADA NAVIDEÑA 2024 - CUPOS LIMITADOS"
    bbox_k = f_kicker.getbbox(kicker_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 106), kicker_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    title_txt = "GANA DE $300 A $800 USD ESTA NAVIDAD"
    bbox_t = f_title.getbbox(title_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2 + 2, 180 + 2), title_txt, fill=(0, 0, 0, 240), font=f_title)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 180), title_txt, fill=(255, 223, 94, 255), font=f_title)
    
    sub_txt = "Vendiendo Postres Gourmet en Vasitos desde Casa"
    bbox_s = f_sub.getbbox(sub_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 265), sub_txt, fill=(255, 255, 255, 255), font=f_sub)
    
    card_y = 1270
    draw.rounded_rectangle([50, card_y, w - 50, 1680], radius=24, fill=(18, 24, 38, 250), outline=(255, 215, 0, 230), width=3)
    
    draw.text((85, card_y + 35), "+ Manual Digital Completo: 30 Recetas", fill=(255, 255, 255, 255), font=f_bonus)
    draw.text((85, card_y + 95), "+ Bono 1: Calculadora Excel de Costos", fill=(255, 223, 94, 255), font=f_bonus)
    draw.text((85, card_y + 155), "+ Bono 2: Guia de Empaques Navideños", fill=(255, 223, 94, 255), font=f_bonus)
    draw.text((85, card_y + 215), "+ Bono 3: Scripts de Venta por WhatsApp", fill=(255, 223, 94, 255), font=f_bonus)
    draw.text((85, card_y + 275), "+ Acceso de por Vida - Garantia de 7 Dias", fill=(100, 255, 150, 255), font=f_bonus)
    
    cta_bar_y = 1730
    cta_txt = "QUIERO MI MANUAL POR $9.90 USD!"
    bbox_c = f_cta.getbbox(cta_txt)
    draw.rounded_rectangle([60, cta_bar_y, w - 60, cta_bar_y + 90], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 230), width=3)
    draw.text(((w - (bbox_c[2] - bbox_c[0])) // 2, cta_bar_y + 26), cta_txt, fill=(255, 255, 255, 255), font=f_cta)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "criativo_3_natal_oferta_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "criativo_3_natal_oferta_story.jpg"), quality=95)
    print("Criativo 3 Story created!")

if __name__ == "__main__":
    create_criativo_1()
    create_criativo_1_story()
    create_criativo_2()
    create_criativo_2_story()
    create_criativo_3()
    create_criativo_3_story()
