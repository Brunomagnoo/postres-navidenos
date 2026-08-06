import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

BASE_DIR = r"C:\Users\bruno\.gemini\antigravity\scratch\postres-navidenos"
BRAIN_DIR = r"C:\Users\bruno\.gemini\antigravity\brain\4625a942-b87a-400c-9c2c-b7f293274965"

FONT_BOLD = "C:\\Windows\\Fonts\\segoeuib.ttf"
FONT_REGULAR = "C:\\Windows\\Fonts\\segoeui.ttf"
FONT_IMPACT = "C:\\Windows\\Fonts\\impact.ttf"
FONT_SERIF = "C:\\Windows\\Fonts\\georgiab.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.truetype("C:\\Windows\\Fonts\\arialbd.ttf", size)

def add_drop_shadow(canvas, box, radius=14, offset=(0, 6), shadow_color=(0, 0, 0, 160)):
    x1, y1, x2, y2 = box
    w = x2 - x1 + radius * 4
    h = y2 - y1 + radius * 4
    
    shadow_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_img)
    
    sx1 = radius * 2
    sy1 = radius * 2
    sx2 = sx1 + (x2 - x1)
    sy2 = sy1 + (y2 - y1)
    
    s_draw.rounded_rectangle([sx1, sy1, sx2, sy2], radius=radius, fill=shadow_color)
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(radius))
    
    paste_x = x1 - radius * 2 + offset[0]
    paste_y = y1 - radius * 2 + offset[1]
    canvas.paste(shadow_img, (paste_x, paste_y), shadow_img)

def draw_vector_check(draw, cx, cy, r=12, bg_color=(0, 180, 80, 255), fg_color=(255, 255, 255, 255)):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg_color)
    p1 = (cx - r * 0.45, cy)
    p2 = (cx - r * 0.1, cy + r * 0.35)
    p3 = (cx + r * 0.5, cy - r * 0.35)
    draw.line([p1, p2, p3], fill=fg_color, width=max(2, int(r * 0.22)), joint="curve")

def draw_vector_cross(draw, cx, cy, r=12, bg_color=(220, 50, 50, 255), fg_color=(255, 255, 255, 255)):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg_color)
    d = r * 0.35
    draw.line([(cx - d, cy - d), (cx + d, cy + d)], fill=fg_color, width=max(2, int(r * 0.22)))
    draw.line([(cx + d, cy - d), (cx - d, cy + d)], fill=fg_color, width=max(2, int(r * 0.22)))

def draw_clock_badge(draw, cx, cy, r=14, bg_color=(255, 190, 0, 255), fg_color=(20, 20, 20, 255)):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg_color)
    draw.line([(cx, cy), (cx, cy - r * 0.55)], fill=fg_color, width=3)
    draw.line([(cx, cy), (cx + r * 0.45, cy)], fill=fg_color, width=3)

# ══════════════════════════════════════════════════════════════════
# VARIANTE 2: O DESAFIO DOS 15 MINUTOS (FEED 1:1)
# ══════════════════════════════════════════════════════════════════

def create_var2_15min_feed():
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    
    # Hero: Tiramisu Navideno (rich cocoa & cream layers)
    bg_path = os.path.join(BASE_DIR, "tiramisu_navideno.jpg")
    bg = Image.open(bg_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    canvas.paste(ImageEnhance.Color(bg).enhance(1.12), (0, 0))
    
    top_grad = Image.new("RGBA", (w, 310), (6, 10, 16, 235))
    bot_grad = Image.new("RGBA", (w, 390), (6, 10, 16, 245))
    canvas.paste(top_grad, (0, 0), top_grad)
    canvas.paste(bot_grad, (0, h - 390), bot_grad)
    
    draw = ImageDraw.Draw(canvas)
    
    # 1. Top Kicker
    draw.rounded_rectangle([100, 20, w - 100, 65], radius=20, fill=(0, 168, 77, 255), outline=(255, 255, 255, 220), width=2)
    f_kicker = get_font(FONT_BOLD, 21)
    k_txt = "METODO ULTRA RAPIDO · 100% SIN HORNO"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 30), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    # 2. Big Stopwatch Hook
    f_title = get_font(FONT_IMPACT, 52)
    t_txt = "¿TIENES 15 MINUTOS LIBRES HOY?"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 78), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    f_sub = get_font(FONT_REGULAR, 23)
    s_txt = "Es todo el tiempo que necesitas para preparar postres navideños"
    bbox_s = f_sub.getbbox(s_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 140), s_txt, fill=(230, 240, 255, 255), font=f_sub)
    
    # 3. Two Floating Feature Chips on Top of the Image
    p1_box = (60, 195, 520, 265)
    p2_box = (560, 195, 1020, 265)
    
    add_drop_shadow(canvas, p1_box, radius=10, offset=(0, 4), shadow_color=(0, 0, 0, 160))
    add_drop_shadow(canvas, p2_box, radius=10, offset=(0, 4), shadow_color=(0, 0, 0, 160))
    
    draw.rounded_rectangle(p1_box, radius=16, fill=(12, 18, 28, 245), outline=(255, 215, 0, 200), width=2)
    draw.rounded_rectangle(p2_box, radius=16, fill=(12, 18, 28, 245), outline=(100, 255, 150, 200), width=2)
    
    f_chip = get_font(FONT_BOLD, 22)
    draw_clock_badge(draw, 95, 230, r=14)
    draw.text((125, 217), "15 Minutos de Preparación", fill=(255, 215, 0, 255), font=f_chip)
    
    draw_vector_check(draw, 595, 230, r=14)
    draw.text((625, 217), "100% en Frío (Sin Horno)", fill=(100, 255, 150, 255), font=f_chip)
    
    # 4. Floating badge on the dessert (Timer badge)
    t_badge_box = (w - 300, 560, w - 50, 640)
    add_drop_shadow(canvas, t_badge_box, radius=12, offset=(0, 4), shadow_color=(0, 0, 0, 180))
    draw.rounded_rectangle(t_badge_box, radius=16, fill=(196, 30, 58, 240), outline=(255, 215, 0, 220), width=2)
    draw_clock_badge(draw, w - 265, 600, r=15)
    f_tb = get_font(FONT_BOLD, 22)
    draw.text((w - 235, 588), "Listos en 15 min", fill=(255, 255, 255, 255), font=f_tb)
    
    # 5. Bottom Offer Card
    bot_y1 = 705
    bot_y2 = 1045
    add_drop_shadow(canvas, (45, bot_y1, w - 45, bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([45, bot_y1, w - 45, bot_y2], radius=20, fill=(12, 18, 28, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((80, bot_y1 + 22), "Manual Digital: 30 Recetas en Vasito Paso a Paso", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 28))
    
    f_b_item = get_font(FONT_REGULAR, 22)
    draw_vector_check(draw, 95, bot_y1 + 75, r=10)
    draw.text((120, bot_y1 + 63), "Ideal para personas ocupadas: recetas fáciles sin maquinaria", fill=(215, 230, 245, 255), font=f_b_item)
    
    draw_vector_check(draw, 95, bot_y1 + 112, r=10)
    draw.text((120, bot_y1 + 100), "+ 3 Bonos Gratis: Calculadora Excel + Empaques + WhatsApp", fill=(255, 223, 94, 255), font=f_b_item)
    
    draw_vector_check(draw, 95, bot_y1 + 149, r=10)
    draw.text((120, bot_y1 + 137), "Acceso Inmediato de por Vida · Garantía de 7 Días", fill=(100, 255, 150, 255), font=f_b_item)
    
    btn_y = bot_y1 + 195
    draw.rounded_rectangle([70, btn_y, w - 70, btn_y + 85], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    btn_txt = "QUIERO EL MANUAL COMPLETO · SOLO $9.90 USD"
    f_btn = get_font(FONT_BOLD, 26)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 24), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v3_criativo_var2_15min_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v3_criativo_var2_15min_feed.jpg"), quality=95)
    print("V3 Criativo Var 2 (15 Min) Feed created!")

# ══════════════════════════════════════════════════════════════════
# VARIANTE 2: O DESAFIO DOS 15 MINUTOS (STORY 9:16)
# ══════════════════════════════════════════════════════════════════

def create_var2_15min_story():
    w, h = 1080, 1920
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    
    bg_path = os.path.join(BASE_DIR, "tiramisu_navideno.jpg")
    bg = Image.open(bg_path).convert("RGBA")
    bg_w, bg_h = bg.size
    scale = max(w / bg_w, h / bg_h)
    new_w, new_h = int(bg_w * scale), int(bg_h * scale)
    bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    bg_cropped = bg.crop((left, top, left + w, top + h))
    canvas.paste(ImageEnhance.Color(bg_cropped).enhance(1.12), (0, 0))
    
    top_over = Image.new("RGBA", (w, 560), (8, 12, 18, 235))
    bot_over = Image.new("RGBA", (w, 660), (8, 12, 18, 245))
    canvas.paste(top_over, (0, 0), top_over)
    canvas.paste(bot_over, (0, h - 660), bot_over)
    
    draw = ImageDraw.Draw(canvas)
    
    # 1. Top Kicker
    draw.rounded_rectangle([70, 70, w - 70, 135], radius=24, fill=(0, 168, 77, 255), outline=(255, 255, 255, 220), width=2)
    f_kicker = get_font(FONT_BOLD, 24)
    k_txt = "METODO ULTRA RAPIDO · 100% SIN HORNO"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 85), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    # 2. Story Title Hook
    f_title = get_font(FONT_IMPACT, 60)
    t_txt = "¿TIENES 15 MINUTOS LIBRES?"
    t_txt2 = "PREPARA POSTRES NAVIDEÑOS"
    bbox_t = f_title.getbbox(t_txt)
    bbox_t2 = f_title.getbbox(t_txt2)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 160), t_txt, fill=(255, 255, 255, 255), font=f_title)
    draw.text(((w - (bbox_t2[2] - bbox_t2[0])) // 2, 230), t_txt2, fill=(255, 223, 94, 255), font=f_title)
    
    f_sub = get_font(FONT_REGULAR, 26)
    s_txt = "Sin horno, sin batidoras caras y listos para vender"
    bbox_s = f_sub.getbbox(s_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 310), s_txt, fill=(210, 225, 240, 255), font=f_sub)
    
    # 3. Middle Feature Card
    f_box = (60, 370, w - 60, 500)
    add_drop_shadow(canvas, f_box, radius=12, offset=(0, 6), shadow_color=(0, 0, 0, 160))
    draw.rounded_rectangle(f_box, radius=20, fill=(15, 22, 34, 240), outline=(255, 215, 0, 200), width=2)
    
    f_feat = get_font(FONT_BOLD, 25)
    draw_clock_badge(draw, 105, 435, r=16)
    draw.text((140, 420), "15 Minutos", fill=(255, 215, 0, 255), font=f_feat)
    
    draw_vector_check(draw, 380, 435, r=16)
    draw.text((415, 420), "Cero Horno", fill=(100, 255, 150, 255), font=f_feat)
    
    draw_vector_check(draw, 680, 435, r=16)
    draw.text((715, 420), "300% Ganancia", fill=(100, 255, 150, 255), font=f_feat)
    
    # 4. Bottom Offer Card
    card_bot_y1 = 1290
    card_bot_y2 = 1680
    add_drop_shadow(canvas, (50, card_bot_y1, w - 50, card_bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, card_bot_y1, w - 50, card_bot_y2], radius=22, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((85, card_bot_y1 + 35), "Manual Digital: 30 Postres Navideños", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 32))
    draw.text((85, card_bot_y1 + 85), "Recetas paso a paso con medidas exactas y fotos", fill=(210, 220, 235, 255), font=get_font(FONT_REGULAR, 26))
    draw.text((85, card_bot_y1 + 130), "+ 3 Bonos Gratis: Calculadora Excel + Empaques + WhatsApp", fill=(255, 223, 94, 255), font=get_font(FONT_REGULAR, 24))
    draw.text((85, card_bot_y1 + 175), "Acceso Inmediato de por Vida - Garantia de 7 Dias", fill=(100, 255, 150, 255), font=get_font(FONT_REGULAR, 24))
    
    btn_y = 1730
    draw.rounded_rectangle([60, btn_y, w - 60, btn_y + 95], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=3)
    btn_txt = "TOCA AQUI PARA DESCARGAR ($9.90 USD)"
    f_btn = get_font(FONT_BOLD, 32)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 26), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v3_criativo_var2_15min_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v3_criativo_var2_15min_story.jpg"), quality=95)
    print("V3 Criativo Var 2 (15 Min) Story created!")

# ══════════════════════════════════════════════════════════════════
# VARIANTE 3: O TESTE DO PRINCIPIANTE TOTAL (FEED 1:1)
# ══════════════════════════════════════════════════════════════════

def create_var3_principiante_feed():
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    
    # Hero: Mousse de Maracuya (bright golden aesthetic)
    bg_path = os.path.join(BASE_DIR, "mousse_maracuya.jpg")
    bg = Image.open(bg_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    canvas.paste(ImageEnhance.Color(bg).enhance(1.12), (0, 0))
    
    top_grad = Image.new("RGBA", (w, 310), (6, 10, 16, 235))
    bot_grad = Image.new("RGBA", (w, 400), (6, 10, 16, 245))
    canvas.paste(top_grad, (0, 0), top_grad)
    canvas.paste(bot_grad, (0, h - 400), bot_grad)
    
    draw = ImageDraw.Draw(canvas)
    
    # 1. Top Kicker
    draw.rounded_rectangle([100, 20, w - 100, 65], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    f_kicker = get_font(FONT_BOLD, 21)
    k_txt = "METODO A PRUEBA DE ERRORES · PARA PRINCIPIANTES"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 30), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    # 2. Hook
    f_title = get_font(FONT_IMPACT, 52)
    t_txt = "¿CERO EXPERIENCIA EN REPOSTERIA?"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 78), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    f_sub = get_font(FONT_REGULAR, 23)
    s_txt = "Aprende a preparar postres que NUNCA se queman ni se bajan"
    bbox_s = f_sub.getbbox(s_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 140), s_txt, fill=(230, 240, 255, 255), font=f_sub)
    
    # 3. 3 Objection-Busting Bullets in Header
    bx1, bx2 = 60, w - 60
    b_y = 185
    b_h = 95
    add_drop_shadow(canvas, (bx1, b_y, bx2, b_y + b_h), radius=10, offset=(0, 4), shadow_color=(0, 0, 0, 160))
    draw.rounded_rectangle([bx1, b_y, bx2, b_y + b_h], radius=16, fill=(12, 18, 28, 245), outline=(255, 215, 0, 190), width=2)
    
    f_mini = get_font(FONT_BOLD, 19)
    
    draw_vector_cross(draw, bx1 + 35, b_y + 30, r=10)
    draw.text((bx1 + 55, b_y + 18), "Sin batidoras industriales", fill=(255, 200, 200, 255), font=f_mini)
    
    draw_vector_cross(draw, bx1 + 35, b_y + 65, r=10)
    draw.text((bx1 + 55, b_y + 53), "Sin horas frente al horno", fill=(255, 200, 200, 255), font=f_mini)
    
    draw_vector_check(draw, bx1 + 500, b_y + 30, r=10)
    draw.text((bx1 + 520, b_y + 18), "100% en frío (solo refrigerador)", fill=(120, 255, 170, 255), font=f_mini)
    
    draw_vector_check(draw, bx1 + 500, b_y + 65, r=10)
    draw.text((bx1 + 520, b_y + 53), "Recetas exactas paso a paso", fill=(120, 255, 170, 255), font=f_mini)
    
    # 4. Stamp on Image
    stamp_box = (w - 330, 560, w - 50, 640)
    add_drop_shadow(canvas, stamp_box, radius=12, offset=(0, 4), shadow_color=(0, 0, 0, 180))
    draw.rounded_rectangle(stamp_box, radius=16, fill=(0, 150, 70, 240), outline=(255, 255, 255, 220), width=2)
    draw_vector_check(draw, w - 295, 600, r=14)
    draw.text((w - 265, 588), "¡Imposible Fallar!", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 22))
    
    # 5. Bottom Offer Card
    bot_y1 = 695
    bot_y2 = 1045
    add_drop_shadow(canvas, (45, bot_y1, w - 45, bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([45, bot_y1, w - 45, bot_y2], radius=20, fill=(12, 18, 28, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((80, bot_y1 + 22), "Manual Digital: 30 Recetas Navideñas Sin Horno", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 28))
    
    f_b_item = get_font(FONT_REGULAR, 22)
    draw_vector_check(draw, 95, bot_y1 + 75, r=10)
    draw.text((120, bot_y1 + 63), "Aprende desde cero con fotos y medidas exactas por vasito", fill=(215, 230, 245, 255), font=f_b_item)
    
    draw_vector_check(draw, 95, bot_y1 + 112, r=10)
    draw.text((120, bot_y1 + 100), "+ 3 Bonos Gratis: Calculadora Excel + Empaques + WhatsApp", fill=(255, 223, 94, 255), font=f_b_item)
    
    draw_vector_check(draw, 95, bot_y1 + 149, r=10)
    draw.text((120, bot_y1 + 137), "Garantía de 7 Días · Acceso Inmediato de por Vida al PDF", fill=(100, 255, 150, 255), font=f_b_item)
    
    btn_y = bot_y1 + 195
    draw.rounded_rectangle([70, btn_y, w - 70, btn_y + 85], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    btn_txt = "ACCEDE HOY CON 65% OFF · SOLO $9.90 USD"
    f_btn = get_font(FONT_BOLD, 26)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 24), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v3_criativo_var3_principiante_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v3_criativo_var3_principiante_feed.jpg"), quality=95)
    print("V3 Criativo Var 3 (Principiante) Feed created!")

# ══════════════════════════════════════════════════════════════════
# VARIANTE 3: O TESTE DO PRINCIPIANTE TOTAL (STORY 9:16)
# ══════════════════════════════════════════════════════════════════

def create_var3_principiante_story():
    w, h = 1080, 1920
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    
    bg_path = os.path.join(BASE_DIR, "mousse_maracuya.jpg")
    bg = Image.open(bg_path).convert("RGBA")
    bg_w, bg_h = bg.size
    scale = max(w / bg_w, h / bg_h)
    new_w, new_h = int(bg_w * scale), int(bg_h * scale)
    bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    bg_cropped = bg.crop((left, top, left + w, top + h))
    canvas.paste(ImageEnhance.Color(bg_cropped).enhance(1.12), (0, 0))
    
    top_over = Image.new("RGBA", (w, 580), (8, 12, 18, 235))
    bot_over = Image.new("RGBA", (w, 660), (8, 12, 18, 245))
    canvas.paste(top_over, (0, 0), top_over)
    canvas.paste(bot_over, (0, h - 660), bot_over)
    
    draw = ImageDraw.Draw(canvas)
    
    # 1. Top Kicker
    draw.rounded_rectangle([70, 70, w - 70, 135], radius=24, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    f_kicker = get_font(FONT_BOLD, 24)
    k_txt = "METODO A PRUEBA DE ERRORES · PARA PRINCIPIANTES"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 85), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    # 2. Big Story Hook
    f_title = get_font(FONT_IMPACT, 58)
    t_txt = "¿CERO EXPERIENCIA EN REPOSTERIA?"
    t_txt2 = "¡ESTE METODO ES IMPOSIBLE DE FALLAR!"
    bbox_t = f_title.getbbox(t_txt)
    bbox_t2 = f_title.getbbox(t_txt2)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 160), t_txt, fill=(255, 255, 255, 255), font=f_title)
    draw.text(((w - (bbox_t2[2] - bbox_t2[0])) // 2, 230), t_txt2, fill=(255, 223, 94, 255), font=f_title)
    
    f_sub = get_font(FONT_REGULAR, 26)
    s_txt = "Aprende 30 postres en vasito que nunca se queman"
    bbox_s = f_sub.getbbox(s_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 310), s_txt, fill=(210, 225, 240, 255), font=f_sub)
    
    # 3. Middle Objection Card
    f_box = (60, 370, w - 60, 510)
    add_drop_shadow(canvas, f_box, radius=12, offset=(0, 6), shadow_color=(0, 0, 0, 160))
    draw.rounded_rectangle(f_box, radius=20, fill=(15, 22, 34, 240), outline=(255, 215, 0, 200), width=2)
    
    f_feat = get_font(FONT_BOLD, 24)
    draw_vector_cross(draw, 100, 440, r=16)
    draw.text((135, 425), "Cero Horno", fill=(255, 190, 190, 255), font=f_feat)
    
    draw_vector_check(draw, 380, 440, r=16)
    draw.text((415, 425), "100% en Frío", fill=(100, 255, 150, 255), font=f_feat)
    
    draw_vector_check(draw, 680, 440, r=16)
    draw.text((715, 425), "Paso a Paso", fill=(100, 255, 150, 255), font=f_feat)
    
    # 4. Bottom Offer Card
    card_bot_y1 = 1290
    card_bot_y2 = 1680
    add_drop_shadow(canvas, (50, card_bot_y1, w - 50, card_bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, card_bot_y1, w - 50, card_bot_y2], radius=22, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((85, card_bot_y1 + 35), "Manual Digital: 30 Postres Navideños", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 32))
    draw.text((85, card_bot_y1 + 85), "Recetas paso a paso con medidas exactas y fotos", fill=(210, 220, 235, 255), font=get_font(FONT_REGULAR, 26))
    draw.text((85, card_bot_y1 + 130), "+ 3 Bonos Gratis: Calculadora Excel + Empaques + WhatsApp", fill=(255, 223, 94, 255), font=get_font(FONT_REGULAR, 24))
    draw.text((85, card_bot_y1 + 175), "Acceso Inmediato de por Vida - Garantia de 7 Dias", fill=(100, 255, 150, 255), font=get_font(FONT_REGULAR, 24))
    
    btn_y = 1730
    draw.rounded_rectangle([60, btn_y, w - 60, btn_y + 95], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=3)
    btn_txt = "TOCA AQUI PARA DESCARGAR ($9.90 USD)"
    f_btn = get_font(FONT_BOLD, 32)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 26), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v3_criativo_var3_principiante_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v3_criativo_var3_principiante_story.jpg"), quality=95)
    print("V3 Criativo Var 3 (Principiante) Story created!")

if __name__ == "__main__":
    create_var2_15min_feed()
    create_var2_15min_story()
    create_var3_principiante_feed()
    create_var3_principiante_story()
