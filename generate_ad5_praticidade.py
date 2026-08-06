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

def draw_step_badge(draw, cx, cy, num_str, r=16, bg_color=(196, 30, 58, 255)):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg_color, outline=(255, 215, 0, 230), width=2)
    f_num = get_font(FONT_BOLD, 18)
    bbox = f_num.getbbox(num_str)
    draw.text((cx - (bbox[2] - bbox[0]) // 2, cy - (bbox[3] - bbox[1]) // 2 - 2), num_str, fill=(255, 255, 255, 255), font=f_num)

# ══════════════════════════════════════════════════════════════════
# REFINED AD 5: 3-STEP PRATICIDADE & ZERO HORNO (Feed 1:1)
# ══════════════════════════════════════════════════════════════════

def create_refined_ad5_feed():
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    
    # Hero Image with high vibrancy
    bg_path = os.path.join(BASE_DIR, "carlota_fresa.jpg")
    bg = Image.open(bg_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    canvas.paste(ImageEnhance.Color(bg).enhance(1.12), (0, 0))
    
    # Elegant top gradient & solid bottom card background
    top_grad = Image.new("RGBA", (w, 320), (6, 10, 16, 235))
    bot_grad = Image.new("RGBA", (w, 420), (6, 10, 16, 245))
    canvas.paste(top_grad, (0, 0), top_grad)
    canvas.paste(bot_grad, (0, h - 420), bot_grad)
    
    draw = ImageDraw.Draw(canvas)
    
    # 1. Top Kicker Badge
    draw.rounded_rectangle([110, 20, w - 110, 64], radius=20, fill=(0, 168, 77, 255), outline=(255, 255, 255, 220), width=2)
    f_kicker = get_font(FONT_BOLD, 21)
    k_txt = "METODO FACIL PARA PRINCIPIANTES · 100% EN FRIO"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 29), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    # 2. Headline Hook
    f_title = get_font(FONT_IMPACT, 54)
    t_txt = "¡SIN HORNO Y EN SOLO 3 PASOS!"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 78), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    f_sub = get_font(FONT_REGULAR, 23)
    s_txt = "Aprende a preparar 30 postres gourmet en vasito sin experiencia"
    bbox_s = f_sub.getbbox(s_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 140), s_txt, fill=(230, 240, 255, 255), font=f_sub)
    
    # 3. 3-Step Visual Cards in the Upper Middle (Floating neatly above the dessert)
    step_w = 310
    step_h = 100
    gap = 25
    start_x = (w - (step_w * 3 + gap * 2)) // 2
    step_y = 190
    
    steps = [
        ("Paso 1", "Mezcla en 5 min", "Sin batidoras caras"),
        ("Paso 2", "Arma en vasitos", "Porciones individuales"),
        ("Paso 3", "Refrigera y listo", "¡Directo a la venta!")
    ]
    
    f_s_num = get_font(FONT_BOLD, 18)
    f_s_t = get_font(FONT_BOLD, 20)
    f_s_sub = get_font(FONT_REGULAR, 16)
    
    for idx, (p_num, p_title, p_desc) in enumerate(steps):
        sx = start_x + idx * (step_w + gap)
        add_drop_shadow(canvas, (sx, step_y, sx + step_w, step_y + step_h), radius=10, offset=(0, 4), shadow_color=(0, 0, 0, 160))
        draw.rounded_rectangle([sx, step_y, sx + step_w, step_y + step_h], radius=14, fill=(12, 18, 28, 245), outline=(255, 215, 0, 190), width=2)
        
        # Draw step number pill
        draw.rounded_rectangle([sx + 12, step_y + 12, sx + 80, step_y + 36], radius=8, fill=(196, 30, 58, 255))
        draw.text((sx + 20, step_y + 14), p_num, fill=(255, 255, 255, 255), font=f_s_num)
        
        draw.text((sx + 15, step_y + 44), p_title, fill=(255, 255, 255, 255), font=f_s_t)
        draw.text((sx + 15, step_y + 70), p_desc, fill=(100, 255, 160, 255), font=f_s_sub)
    
    # 4. Floating Quality Stamp over Dessert (Bottom Right)
    stamp_box = (w - 320, 560, w - 50, 640)
    add_drop_shadow(canvas, stamp_box, radius=12, offset=(0, 4), shadow_color=(0, 0, 0, 180))
    draw.rounded_rectangle(stamp_box, radius=16, fill=(0, 150, 70, 240), outline=(255, 255, 255, 220), width=2)
    f_stamp = get_font(FONT_BOLD, 22)
    draw_vector_check(draw, w - 285, 600, r=14)
    draw.text((w - 255, 588), "100% Cero Horno", fill=(255, 255, 255, 255), font=f_stamp)
    
    # 5. Bottom Offer & CTA Card
    bot_y1 = 675
    bot_y2 = 1045
    add_drop_shadow(canvas, (45, bot_y1, w - 45, bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([45, bot_y1, w - 45, bot_y2], radius=20, fill=(12, 18, 28, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((80, bot_y1 + 22), "Manual Digital: 30 Recetas Navideñas Paso a Paso", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 28))
    
    f_b_item = get_font(FONT_REGULAR, 22)
    draw_vector_check(draw, 95, bot_y1 + 75, r=10)
    draw.text((120, bot_y1 + 63), "Recetas exactas con fotos y medidas explicadas desde cero", fill=(215, 230, 245, 255), font=f_b_item)
    
    draw_vector_check(draw, 95, bot_y1 + 112, r=10)
    draw.text((120, bot_y1 + 100), "Incluye 3 Bonos Gratis: Calculadora Excel + Empaques + WhatsApp", fill=(255, 223, 94, 255), font=f_b_item)
    
    draw_vector_check(draw, 95, bot_y1 + 149, r=10)
    draw.text((120, bot_y1 + 137), "Garantia de 7 Dias · Acceso Inmediato de por Vida en PDF", fill=(100, 255, 150, 255), font=f_b_item)
    
    btn_y = bot_y1 + 195
    draw.rounded_rectangle([70, btn_y, w - 70, btn_y + 85], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    btn_txt = "OBTEN EL MANUAL COMPLETO · SOLO $9.90 USD"
    f_btn = get_font(FONT_BOLD, 28)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 24), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_5_praticidade_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_5_praticidade_feed.jpg"), quality=95)
    print("Refined V2 Criativo 5 Praticidade Feed created!")

# ══════════════════════════════════════════════════════════════════
# REFINED AD 5: 3-STEP PRATICIDADE & ZERO HORNO (Story 9:16)
# ══════════════════════════════════════════════════════════════════

def create_refined_ad5_story():
    w, h = 1080, 1920
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    
    bg_path = os.path.join(BASE_DIR, "carlota_fresa.jpg")
    bg = Image.open(bg_path).convert("RGBA")
    bg_w, bg_h = bg.size
    scale = max(w / bg_w, h / bg_h)
    new_w, new_h = int(bg_w * scale), int(bg_h * scale)
    bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    bg_cropped = bg.crop((left, top, left + w, top + h))
    canvas.paste(ImageEnhance.Color(bg_cropped).enhance(1.12), (0, 0))
    
    top_over = Image.new("RGBA", (w, 640), (8, 12, 18, 235))
    bot_over = Image.new("RGBA", (w, 660), (8, 12, 18, 245))
    canvas.paste(top_over, (0, 0), top_over)
    canvas.paste(bot_over, (0, h - 660), bot_over)
    
    draw = ImageDraw.Draw(canvas)
    
    # 1. Top Kicker
    draw.rounded_rectangle([70, 70, w - 70, 135], radius=24, fill=(0, 168, 77, 255), outline=(255, 255, 255, 220), width=2)
    f_kicker = get_font(FONT_BOLD, 24)
    k_txt = "METODO FACIL PARA PRINCIPIANTES · 100% EN FRIO"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 85), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    # 2. Big Story Hook
    f_title = get_font(FONT_IMPACT, 64)
    t_txt = "¡SIN HORNO Y EN 3 PASOS!"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 160), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    f_sub = get_font(FONT_REGULAR, 26)
    s_txt = "Aprende a preparar 30 postres en vasito en solo 15 minutos"
    bbox_s = f_sub.getbbox(s_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 245), s_txt, fill=(210, 225, 240, 255), font=f_sub)
    
    # 3. 3 Step Cards in Vertical/Horizontal grid
    step_box = (60, 310, w - 60, 580)
    add_drop_shadow(canvas, step_box, radius=14, offset=(0, 6), shadow_color=(0, 0, 0, 180))
    draw.rounded_rectangle(step_box, radius=20, fill=(15, 22, 34, 245), outline=(255, 215, 0, 200), width=2)
    
    steps = [
        ("Paso 1", "Mezcla en 5 minutos con utensilios de casa"),
        ("Paso 2", "Arma capas en tus vasitos individuales"),
        ("Paso 3", "Refrigera 10 minutos y ¡listo para vender!")
    ]
    
    f_s_num = get_font(FONT_BOLD, 22)
    f_s_txt = get_font(FONT_BOLD, 24)
    
    for idx, (p_num, p_text) in enumerate(steps):
        sy = 340 + idx * 75
        draw.rounded_rectangle([90, sy, 180, sy + 45], radius=10, fill=(196, 30, 58, 255))
        draw.text((105, sy + 8), p_num, fill=(255, 255, 255, 255), font=f_s_num)
        draw.text((205, sy + 8), p_text, fill=(255, 255, 255, 255), font=f_s_txt)
        
    # Floating stamp
    stamp_box = (w - 380, 1140, w - 60, 1230)
    add_drop_shadow(canvas, stamp_box, radius=12, offset=(0, 4), shadow_color=(0, 0, 0, 180))
    draw.rounded_rectangle(stamp_box, radius=18, fill=(0, 150, 70, 240), outline=(255, 255, 255, 220), width=2)
    draw_vector_check(draw, w - 340, 1185, r=16)
    draw.text((w - 305, 1170), "100% Cero Horno", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 26))
    
    # Bottom Offer Box
    card_bot_y1 = 1290
    card_bot_y2 = 1680
    add_drop_shadow(canvas, (50, card_bot_y1, w - 50, card_bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, card_bot_y1, w - 50, card_bot_y2], radius=22, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((85, card_bot_y1 + 35), "Manual Digital: 30 Postres Navidenos", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 32))
    draw.text((85, card_bot_y1 + 85), "Recetas paso a paso con medidas exactas y fotos", fill=(210, 220, 235, 255), font=get_font(FONT_REGULAR, 26))
    draw.text((85, card_bot_y1 + 130), "+ 3 Bonos Gratis: Calculadora Excel + Empaques + WhatsApp", fill=(255, 223, 94, 255), font=get_font(FONT_REGULAR, 24))
    draw.text((85, card_bot_y1 + 175), "Acceso Inmediato de por Vida - Garantia de 7 Dias", fill=(100, 255, 150, 255), font=get_font(FONT_REGULAR, 24))
    
    btn_y = 1730
    draw.rounded_rectangle([60, btn_y, w - 60, btn_y + 95], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=3)
    btn_txt = "TOCA AQUI PARA DESCARGAR ($9.90 USD)"
    f_btn = get_font(FONT_BOLD, 32)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 26), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_5_praticidade_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_5_praticidade_story.jpg"), quality=95)
    print("Refined V2 Criativo 5 Praticidade Story created!")

if __name__ == "__main__":
    create_refined_ad5_feed()
    create_refined_ad5_story()
