import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

BASE_DIR = r"C:\Users\bruno\.gemini\antigravity\scratch\postres-navidenos"
BRAIN_DIR = r"C:\Users\bruno\.gemini\antigravity\brain\4625a942-b87a-400c-9c2c-b7f293274965"

# System Fonts
FONT_BOLD = "C:\\Windows\\Fonts\\segoeuib.ttf"
FONT_REGULAR = "C:\\Windows\\Fonts\\segoeui.ttf"
FONT_SEMI = "C:\\Windows\\Fonts\\segoeuisl.ttf"
FONT_SERIF = "C:\\Windows\\Fonts\\georgiab.ttf"
FONT_IMPACT = "C:\\Windows\\Fonts\\impact.ttf"

def get_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.truetype("C:\\Windows\\Fonts\\arialbd.ttf", size)

def add_drop_shadow(canvas, box, radius=15, offset=(0, 8), shadow_color=(0, 0, 0, 140)):
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
    """Draws a crisp round green badge with a white checkmark"""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg_color)
    p1 = (cx - r * 0.45, cy)
    p2 = (cx - r * 0.1, cy + r * 0.35)
    p3 = (cx + r * 0.5, cy - r * 0.35)
    draw.line([p1, p2, p3], fill=fg_color, width=max(2, int(r * 0.22)), joint="curve")

def draw_vector_cross(draw, cx, cy, r=12, bg_color=(220, 50, 50, 255), fg_color=(255, 255, 255, 255)):
    """Draws a crisp round red badge with a white X"""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=bg_color)
    d = r * 0.35
    draw.line([(cx - d, cy - d), (cx + d, cy + d)], fill=fg_color, width=max(2, int(r * 0.22)))
    draw.line([(cx + d, cy - d), (cx - d, cy + d)], fill=fg_color, width=max(2, int(r * 0.22)))

def draw_double_check(draw, x, y, color=(52, 183, 241, 255)):
    """Draws WhatsApp blue double checkmarks"""
    draw.line([(x, y + 4), (x + 4, y + 8), (x + 12, y)], fill=color, width=2)
    draw.line([(x + 6, y + 4), (x + 10, y + 8), (x + 18, y)], fill=color, width=2)

# ══════════════════════════════════════════════════════════════════
# FORMAT 1: VIRAL SOCIAL PROOF / TWEET HOOK (Feed & Story)
# ══════════════════════════════════════════════════════════════════

def create_format_1_tweet_feed():
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    
    bg_path = os.path.join(BASE_DIR, "cheesecake_frutos_rojos.jpg")
    bg = Image.open(bg_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    canvas.paste(ImageEnhance.Color(bg).enhance(1.1), (0, 0))
    
    top_vignette = Image.new("RGBA", (w, 380), (8, 12, 18, 235))
    bot_vignette = Image.new("RGBA", (w, 360), (8, 12, 18, 245))
    canvas.paste(top_vignette, (0, 0), top_vignette)
    canvas.paste(bot_vignette, (0, h - 360), bot_vignette)
    
    card_x1, card_y1, card_x2, card_y2 = 50, 45, w - 50, 315
    add_drop_shadow(canvas, (card_x1, card_y1, card_x2, card_y2), radius=16, offset=(0, 8), shadow_color=(0, 0, 0, 160))
    
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=20, fill=(255, 255, 255, 252), outline=(220, 225, 235, 255), width=2)
    
    avatar_path = os.path.join(BASE_DIR, "avatar_sofia.jpg")
    if os.path.exists(avatar_path):
        av = Image.open(avatar_path).convert("RGBA").resize((80, 80), Image.Resampling.LANCZOS)
        av_mask = Image.new("L", (80, 80), 0)
        ImageDraw.Draw(av_mask).ellipse([0, 0, 80, 80], fill=255)
        canvas.paste(av, (card_x1 + 25, card_y1 + 25), av_mask)
        draw.ellipse([card_x1 + 25, card_y1 + 25, card_x1 + 105, card_y1 + 105], outline=(196, 30, 58, 255), width=2)
    
    f_name = get_font(FONT_BOLD, 26)
    f_handle = get_font(FONT_REGULAR, 22)
    f_tweet = get_font(FONT_BOLD, 26)
    f_tweet_hl = get_font(FONT_BOLD, 28)
    
    draw.text((card_x1 + 120, card_y1 + 32), "Sofia Morales", fill=(20, 25, 35, 255), font=f_name)
    draw.text((card_x1 + 285, card_y1 + 36), "@sofia_postres - Repostera en Casa", fill=(110, 120, 135, 255), font=f_handle)
    
    draw.text((card_x1 + 30, card_y1 + 125), '"Me decian que no iba a vender nada sin horno...', fill=(40, 45, 55, 255), font=f_tweet)
    draw.text((card_x1 + 30, card_y1 + 165), 'Ayer entregue 42 vasitos navidenos y gane', fill=(40, 45, 55, 255), font=f_tweet)
    draw.text((card_x1 + 30, card_y1 + 208), '$105 USD limpios en una sola tarde!"', fill=(196, 30, 58, 255), font=f_tweet_hl)
    
    draw.rounded_rectangle([70, 680, w - 70, 755], radius=16, fill=(0, 168, 77, 245), outline=(255, 255, 255, 220), width=2)
    f_badge = get_font(FONT_BOLD, 30)
    badge_txt = "100% SIN HORNO - LISTOS EN 15 MINUTOS"
    bbox_b = f_badge.getbbox(badge_txt)
    draw.text(((w - (bbox_b[2] - bbox_b[0])) // 2, 700), badge_txt, fill=(255, 255, 255, 255), font=f_badge)
    
    card_bot_y1 = 780
    card_bot_y2 = 1040
    add_drop_shadow(canvas, (50, card_bot_y1, w - 50, card_bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, card_bot_y1, w - 50, card_bot_y2], radius=20, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    f_h2 = get_font(FONT_BOLD, 30)
    f_sub = get_font(FONT_REGULAR, 22)
    f_btn = get_font(FONT_BOLD, 28)
    
    draw.text((85, card_bot_y1 + 25), "Manual Digital: 30 Postres Navidenos en Vasito", fill=(255, 255, 255, 255), font=f_h2)
    draw.text((85, card_bot_y1 + 68), "+ 3 Bonos Gratis: Calculadora Excel + Empaques + Scripts WhatsApp", fill=(255, 223, 94, 255), font=f_sub)
    
    btn_y = card_bot_y1 + 125
    draw.rounded_rectangle([80, btn_y, w - 80, btn_y + 80], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    btn_txt = "Descarga Todo Hoy por solo $9.90 USD"
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 22), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_1_viral_tweet_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_1_viral_tweet_feed.jpg"), quality=95)
    print("V2 Criativo 1 Tweet Feed updated!")

def create_format_1_tweet_story():
    w, h = 1080, 1920
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    
    bg_path = os.path.join(BASE_DIR, "cheesecake_frutos_rojos.jpg")
    bg = Image.open(bg_path).convert("RGBA")
    bg_w, bg_h = bg.size
    scale = max(w / bg_w, h / bg_h)
    new_w, new_h = int(bg_w * scale), int(bg_h * scale)
    bg = bg.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - w) // 2
    top = (new_h - h) // 2
    bg_cropped = bg.crop((left, top, left + w, top + h))
    canvas.paste(ImageEnhance.Color(bg_cropped).enhance(1.1), (0, 0))
    
    top_over = Image.new("RGBA", (w, 560), (8, 12, 18, 230))
    bot_over = Image.new("RGBA", (w, 600), (8, 12, 18, 245))
    canvas.paste(top_over, (0, 0), top_over)
    canvas.paste(bot_over, (0, h - 600), bot_over)
    
    card_x1, card_y1, card_x2, card_y2 = 50, 120, w - 50, 480
    add_drop_shadow(canvas, (card_x1, card_y1, card_x2, card_y2), radius=16, offset=(0, 8), shadow_color=(0, 0, 0, 180))
    
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=22, fill=(255, 255, 255, 252), outline=(220, 225, 235, 255), width=2)
    
    avatar_path = os.path.join(BASE_DIR, "avatar_sofia.jpg")
    if os.path.exists(avatar_path):
        av = Image.open(avatar_path).convert("RGBA").resize((95, 95), Image.Resampling.LANCZOS)
        av_mask = Image.new("L", (95, 95), 0)
        ImageDraw.Draw(av_mask).ellipse([0, 0, 95, 95], fill=255)
        canvas.paste(av, (card_x1 + 30, card_y1 + 30), av_mask)
        draw.ellipse([card_x1 + 30, card_y1 + 30, card_x1 + 125, card_y1 + 125], outline=(196, 30, 58, 255), width=3)
    
    f_name = get_font(FONT_BOLD, 30)
    f_handle = get_font(FONT_REGULAR, 24)
    f_tweet = get_font(FONT_BOLD, 30)
    f_tweet_hl = get_font(FONT_BOLD, 34)
    
    draw.text((card_x1 + 145, card_y1 + 38), "Sofia Morales", fill=(20, 25, 35, 255), font=f_name)
    draw.text((card_x1 + 335, card_y1 + 42), "@sofia_postres - Repostera en Casa", fill=(110, 120, 135, 255), font=f_handle)
    
    draw.text((card_x1 + 35, card_y1 + 155), '"Me decian que no iba a vender nada sin horno...', fill=(40, 45, 55, 255), font=f_tweet)
    draw.text((card_x1 + 35, card_y1 + 205), 'Ayer entregue 42 vasitos navidenos y gane', fill=(40, 45, 55, 255), font=f_tweet)
    draw.text((card_x1 + 35, card_y1 + 260), '$105 USD limpios en una sola tarde!"', fill=(196, 30, 58, 255), font=f_tweet_hl)
    
    draw.rounded_rectangle([70, 1180, w - 70, 1275], radius=20, fill=(0, 168, 77, 250), outline=(255, 255, 255, 230), width=3)
    f_badge = get_font(FONT_BOLD, 34)
    badge_txt = "100% SIN HORNO - LISTOS EN 15 MIN"
    bbox_b = f_badge.getbbox(badge_txt)
    draw.text(((w - (bbox_b[2] - bbox_b[0])) // 2, 1208), badge_txt, fill=(255, 255, 255, 255), font=f_badge)
    
    card_bot_y1 = 1350
    card_bot_y2 = 1700
    add_drop_shadow(canvas, (50, card_bot_y1, w - 50, card_bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, card_bot_y1, w - 50, card_bot_y2], radius=22, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    f_h2 = get_font(FONT_BOLD, 36)
    f_sub = get_font(FONT_REGULAR, 26)
    f_btn = get_font(FONT_BOLD, 32)
    
    draw.text((85, card_bot_y1 + 35), "Manual Digital: 30 Postres Navidenos", fill=(255, 255, 255, 255), font=f_h2)
    draw.text((85, card_bot_y1 + 90), "Aprende paso a paso como emprender desde casa", fill=(210, 220, 235, 255), font=f_sub)
    draw.text((85, card_bot_y1 + 135), "+ 3 Bonos Gratis: Calculadora Excel + Empaques + WhatsApp", fill=(255, 223, 94, 255), font=f_sub)
    draw.text((85, card_bot_y1 + 180), "Garantia de 7 Dias - Acceso Inmediato de por Vida", fill=(100, 255, 150, 255), font=f_sub)
    
    btn_y = 1750
    draw.rounded_rectangle([60, btn_y, w - 60, btn_y + 95], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=3)
    btn_txt = "TOCA AQUI PARA DESCARGAR ($9.90 USD)"
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 26), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_1_viral_tweet_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_1_viral_tweet_story.jpg"), quality=95)
    print("V2 Criativo 1 Tweet Story updated!")

# ══════════════════════════════════════════════════════════════════
# FORMAT 2: 6-GRID RECIPE CATALOG (Feed & Story)
# ══════════════════════════════════════════════════════════════════

def create_format_2_catalogo_feed():
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(FONT_BOLD, 20)
    f_title = get_font(FONT_IMPACT, 48)
    
    draw.rounded_rectangle([70, 20, w - 70, 60], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 200), width=2)
    k_txt = "CATALOGO DE TEMPORADA 2024 - 100% SIN HORNO"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 28), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    t_txt = "LOS 6 POSTRES MAS PEDIDOS PARA NAVIDAD"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 75), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    # Accurate filenames checked and verified
    recipes = [
        ("Mousse Ferrero", "15 min | Sin Horno", "mousse_chocolate.jpg"),
        ("Carlota de Fresa", "15 min | Sin Horno", "carlota_fresa.jpg"),
        ("Mousse Maracuya", "15 min | Sin Horno", "mousse_maracuya.jpg"),
        ("Tiramisu Navideno", "15 min | Sin Horno", "tiramisu_navideno.jpg"),
        ("Chocoflan Cup", "15 min | Sin Horno", "chocoflan_navideno.jpg"),
        ("Cheesecake Frutos", "15 min | Sin Horno", "cheesecake_frutos_rojos.jpg"),
    ]
    
    grid_w, grid_h = 310, 255
    start_x, start_y = 45, 140
    gap_x, gap_y = 30, 25
    
    f_card_t = get_font(FONT_BOLD, 21)
    f_card_sub = get_font(FONT_REGULAR, 17)
    
    for i, (name, tag, img_file) in enumerate(recipes):
        row = i // 3
        col = i % 3
        cx = start_x + col * (grid_w + gap_x)
        cy = start_y + row * (grid_h + gap_y)
        
        add_drop_shadow(canvas, (cx, cy, cx + grid_w, cy + grid_h), radius=10, offset=(0, 4), shadow_color=(0, 0, 0, 140))
        draw.rounded_rectangle([cx, cy, cx + grid_w, cy + grid_h], radius=16, fill=(15, 22, 34, 255), outline=(255, 215, 0, 180), width=2)
        
        img_path = os.path.join(BASE_DIR, img_file)
        if os.path.exists(img_path):
            im = Image.open(img_path).convert("RGBA").resize((grid_w - 12, 170), Image.Resampling.LANCZOS)
            canvas.paste(im, (cx + 6, cy + 6))
        else:
            print(f"Warning: image {img_file} not found!")
            
        t_box = f_card_t.getbbox(name)
        draw.text((cx + (grid_w - (t_box[2] - t_box[0])) // 2, cy + 185), name, fill=(255, 255, 255, 255), font=f_card_t)
        
        s_box = f_card_sub.getbbox(tag)
        draw.text((cx + (grid_w - (s_box[2] - s_box[0])) // 2, cy + 215), tag, fill=(100, 255, 150, 255), font=f_card_sub)
        
    card_bot_y1 = 735
    card_bot_y2 = 1045
    add_drop_shadow(canvas, (45, card_bot_y1, w - 45, card_bot_y2), radius=14, offset=(0, 6))
    draw.rounded_rectangle([45, card_bot_y1, w - 45, card_bot_y2], radius=20, fill=(12, 18, 28, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((75, card_bot_y1 + 25), "Aprende estas 6 y 24 recetas mas en el Manual Digital Completo", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 26))
    draw.text((75, card_bot_y1 + 65), "+ Incluye Calculadora Excel de Costos + Guia de Empaques + WhatsApp", fill=(255, 223, 94, 255), font=get_font(FONT_REGULAR, 21))
    
    btn_y = card_bot_y1 + 120
    draw.rounded_rectangle([70, btn_y, w - 70, btn_y + 80], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    btn_txt = "QUIERO EL MANUAL COMPLETO - SOLO $9.90 USD"
    f_btn = get_font(FONT_BOLD, 28)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 22), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_2_catalogo_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_2_catalogo_feed.jpg"), quality=95)
    print("V2 Criativo 2 Catalogo Feed created!")

def create_format_2_catalogo_story():
    w, h = 1080, 1920
    canvas = Image.new("RGBA", (w, h), (10, 14, 22, 255))
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(FONT_BOLD, 24)
    f_title = get_font(FONT_IMPACT, 60)
    
    draw.rounded_rectangle([70, 70, w - 70, 135], radius=24, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    k_txt = "CATALOGO DE TEMPORADA - 100% SIN HORNO"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 85), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    t_txt = "LOS 6 POSTRES MAS VENDIDOS"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 160), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    recipes = [
        ("Mousse Ferrero", "15 min | Sin Horno", "mousse_chocolate.jpg"),
        ("Carlota de Fresa", "15 min | Sin Horno", "carlota_fresa.jpg"),
        ("Mousse Maracuya", "15 min | Sin Horno", "mousse_maracuya.jpg"),
        ("Tiramisu Navideno", "15 min | Sin Horno", "tiramisu_navideno.jpg"),
        ("Chocoflan Cup", "15 min | Sin Horno", "chocoflan_navideno.jpg"),
        ("Cheesecake Frutos", "15 min | Sin Horno", "cheesecake_frutos_rojos.jpg"),
    ]
    
    grid_w, grid_h = 460, 310
    start_x, start_y = 55, 260
    gap_x, gap_y = 50, 35
    
    f_card_t = get_font(FONT_BOLD, 26)
    f_card_sub = get_font(FONT_REGULAR, 21)
    
    for i, (name, tag, img_file) in enumerate(recipes):
        row = i // 2
        col = i % 2
        cx = start_x + col * (grid_w + gap_x)
        cy = start_y + row * (grid_h + gap_y)
        
        add_drop_shadow(canvas, (cx, cy, cx + grid_w, cy + grid_h), radius=12, offset=(0, 6), shadow_color=(0, 0, 0, 160))
        draw.rounded_rectangle([cx, cy, cx + grid_w, cy + grid_h], radius=18, fill=(15, 22, 34, 255), outline=(255, 215, 0, 200), width=2)
        
        img_path = os.path.join(BASE_DIR, img_file)
        if os.path.exists(img_path):
            im = Image.open(img_path).convert("RGBA").resize((grid_w - 16, 210), Image.Resampling.LANCZOS)
            canvas.paste(im, (cx + 8, cy + 8))
            
        t_box = f_card_t.getbbox(name)
        draw.text((cx + (grid_w - (t_box[2] - t_box[0])) // 2, cy + 228), name, fill=(255, 255, 255, 255), font=f_card_t)
        
        s_box = f_card_sub.getbbox(tag)
        draw.text((cx + (grid_w - (s_box[2] - s_box[0])) // 2, cy + 265), tag, fill=(100, 255, 150, 255), font=f_card_sub)
        
    card_bot_y1 = 1330
    card_bot_y2 = 1680
    add_drop_shadow(canvas, (50, card_bot_y1, w - 50, card_bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, card_bot_y1, w - 50, card_bot_y2], radius=22, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((85, card_bot_y1 + 35), "Manual Digital: 30 Postres Navidenos", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 32))
    draw.text((85, card_bot_y1 + 85), "Aprende estas 6 y 24 recetas mas con fotos y costos", fill=(210, 220, 235, 255), font=get_font(FONT_REGULAR, 26))
    draw.text((85, card_bot_y1 + 130), "+ 3 Bonos Gratis: Calculadora Excel + Empaques + Scripts", fill=(255, 223, 94, 255), font=get_font(FONT_REGULAR, 24))
    draw.text((85, card_bot_y1 + 175), "Acceso Inmediato de por Vida - Garantia de 7 Dias", fill=(100, 255, 150, 255), font=get_font(FONT_REGULAR, 24))
    
    btn_y = 1730
    draw.rounded_rectangle([60, btn_y, w - 60, btn_y + 95], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=3)
    btn_txt = "TOCA AQUI PARA OBTENER EL MANUAL ($9.90)"
    f_btn = get_font(FONT_BOLD, 30)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 26), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_2_catalogo_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_2_catalogo_story.jpg"), quality=95)
    print("V2 Criativo 2 Catalogo Story created!")

# ══════════════════════════════════════════════════════════════════
# FORMAT 3: WHATSAPP ORDER / REAL SOCIAL PROOF (Feed & Story)
# ══════════════════════════════════════════════════════════════════

def create_format_3_whatsapp_feed():
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (12, 17, 26, 255))
    
    caja_path = os.path.join(BASE_DIR, "caja_regalo.jpg")
    bg = Image.open(caja_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    canvas.paste(bg, (0, 0))
    
    top_over = Image.new("RGBA", (w, 180), (8, 12, 18, 220))
    bot_over = Image.new("RGBA", (w, 360), (8, 12, 18, 245))
    canvas.paste(top_over, (0, 0), top_over)
    canvas.paste(bot_over, (0, h - 360), bot_over)
    
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(FONT_BOLD, 22)
    f_title = get_font(FONT_IMPACT, 52)
    
    draw.rounded_rectangle([80, 20, w - 80, 65], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 200), width=2)
    k_txt = "CASO REAL: PEDIDOS DE NAVIDAD POR WHATSAPP"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 28), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    t_txt = "ASI SE VENDEN LOS VASITOS EN DICIEMBRE"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 80), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    chat_x1, chat_y1, chat_x2, chat_y2 = 60, 200, w - 60, 670
    add_drop_shadow(canvas, (chat_x1, chat_y1, chat_x2, chat_y2), radius=20, offset=(0, 10), shadow_color=(0, 0, 0, 180))
    
    draw.rounded_rectangle([chat_x1, chat_y1, chat_x2, chat_y1 + 75], radius=16, fill=(7, 94, 84, 255))
    f_wa_name = get_font(FONT_BOLD, 24)
    f_wa_status = get_font(FONT_REGULAR, 18)
    draw.text((chat_x1 + 30, chat_y1 + 14), "Cliente: Laura Gomez (Empresa)", fill=(255, 255, 255, 255), font=f_wa_name)
    draw.text((chat_x1 + 30, chat_y1 + 44), "en linea", fill=(180, 240, 200, 255), font=f_wa_status)
    
    draw.rounded_rectangle([chat_x1, chat_y1 + 70, chat_x2, chat_y2], radius=16, fill=(234, 228, 220, 250))
    
    f_msg = get_font(FONT_REGULAR, 22)
    f_time = get_font(FONT_REGULAR, 16)
    
    # Bubble 1: Incoming from Client
    b1_x1, b1_y1, b1_x2, b1_y2 = chat_x1 + 25, chat_y1 + 95, chat_x1 + 680, chat_y1 + 195
    draw.rounded_rectangle([b1_x1, b1_y1, b1_x2, b1_y2], radius=14, fill=(255, 255, 255, 255), outline=(220, 220, 220, 255))
    draw.text((b1_x1 + 18, b1_y1 + 14), "Hola Maria! Quiero apartar 4 cajas de", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b1_x1 + 18, b1_y1 + 44), "6 vasitos para la cena del 24. Cuanto es?", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b1_x2 - 85, b1_y2 - 28), "10:14 AM", fill=(140, 140, 140, 255), font=f_time)
    
    # Bubble 2: Outgoing from Seller (Green)
    b2_x1, b2_y1, b2_x2, b2_y2 = chat_x2 - 680, chat_y1 + 215, chat_x2 - 25, chat_y1 + 315
    draw.rounded_rectangle([b2_x1, b2_y1, b2_x2, b2_y2], radius=14, fill=(217, 253, 211, 255), outline=(180, 230, 180, 255))
    draw.text((b2_x1 + 18, b2_y1 + 14), "Hola Laura! Con gusto. Son 24 vasitos", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b2_x1 + 18, b2_y1 + 44), "surtidos por $60 USD en total.", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b2_x2 - 120, b2_y2 - 28), "10:15 AM", fill=(100, 150, 100, 255), font=f_time)
    draw_double_check(draw, b2_x2 - 45, b2_y2 - 24)
    
    # Bubble 3: Incoming from Client
    b3_x1, b3_y1, b3_x2, b3_y2 = chat_x1 + 25, chat_y1 + 335, chat_x1 + 650, chat_y1 + 430
    draw.rounded_rectangle([b3_x1, b3_y1, b3_x2, b3_y2], radius=14, fill=(255, 255, 255, 255), outline=(220, 220, 220, 255))
    draw.text((b3_x1 + 18, b3_y1 + 14), "Perfecto! Ya te hice la transferencia.", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b3_x1 + 18, b3_y1 + 44), "Muchas gracias, se ven hermosos!", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b3_x2 - 85, b3_y2 - 28), "10:16 AM", fill=(140, 140, 140, 255), font=f_time)
    
    card_bot_y1 = 740
    card_bot_y2 = 1040
    add_drop_shadow(canvas, (50, card_bot_y1, w - 50, card_bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, card_bot_y1, w - 50, card_bot_y2], radius=20, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((85, card_bot_y1 + 25), "Aprende el Metodo Paso a Paso de Ventas por WhatsApp", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 28))
    draw.text((85, card_bot_y1 + 68), "30 Recetas en Vasito + Scripts de Venta Listos + Calculadora de Costos", fill=(255, 223, 94, 255), font=get_font(FONT_REGULAR, 22))
    
    btn_y = card_bot_y1 + 125
    draw.rounded_rectangle([75, btn_y, w - 75, btn_y + 80], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    btn_txt = "DESCARGA TODO EL PAQUETE POR $9.90 USD"
    f_btn = get_font(FONT_BOLD, 28)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 22), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_3_whatsapp_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_3_whatsapp_feed.jpg"), quality=95)
    print("V2 Criativo 3 WhatsApp Feed updated!")

def create_format_3_whatsapp_story():
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
    canvas.paste(bg_cropped, (0, 0))
    
    top_over = Image.new("RGBA", (w, 360), (8, 12, 18, 225))
    bot_over = Image.new("RGBA", (w, 640), (8, 12, 18, 245))
    canvas.paste(top_over, (0, 0), top_over)
    canvas.paste(bot_over, (0, h - 640), bot_over)
    
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(FONT_BOLD, 26)
    f_title = get_font(FONT_IMPACT, 62)
    
    draw.rounded_rectangle([70, 80, w - 70, 145], radius=24, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    k_txt = "CASO REAL: PEDIDOS DE NAVIDAD POR WHATSAPP"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 96), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    t_txt = "ASI SE VENDEN LOS VASITOS EN DICIEMBRE"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 175), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    chat_x1, chat_y1, chat_x2, chat_y2 = 50, 420, w - 50, 1180
    add_drop_shadow(canvas, (chat_x1, chat_y1, chat_x2, chat_y2), radius=20, offset=(0, 10), shadow_color=(0, 0, 0, 180))
    
    draw.rounded_rectangle([chat_x1, chat_y1, chat_x2, chat_y1 + 95], radius=20, fill=(7, 94, 84, 255))
    f_wa_name = get_font(FONT_BOLD, 30)
    f_wa_status = get_font(FONT_REGULAR, 22)
    draw.text((chat_x1 + 35, chat_y1 + 18), "Cliente: Laura Gomez (Empresa)", fill=(255, 255, 255, 255), font=f_wa_name)
    draw.text((chat_x1 + 35, chat_y1 + 54), "en linea", fill=(180, 240, 200, 255), font=f_wa_status)
    
    draw.rounded_rectangle([chat_x1, chat_y1 + 90, chat_x2, chat_y2], radius=20, fill=(234, 228, 220, 250))
    
    f_msg = get_font(FONT_REGULAR, 28)
    f_time = get_font(FONT_REGULAR, 20)
    
    # Bubble 1
    b1_x1, b1_y1, b1_x2, b1_y2 = chat_x1 + 30, chat_y1 + 130, chat_x1 + 780, chat_y1 + 270
    draw.rounded_rectangle([b1_x1, b1_y1, b1_x2, b1_y2], radius=16, fill=(255, 255, 255, 255), outline=(220, 220, 220, 255))
    draw.text((b1_x1 + 22, b1_y1 + 20), "Hola Maria! Quiero apartar 4 cajas de", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b1_x1 + 22, b1_y1 + 60), "6 vasitos para la cena del 24. Cuanto es?", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b1_x2 - 110, b1_y2 - 35), "10:14 AM", fill=(140, 140, 140, 255), font=f_time)
    
    # Bubble 2
    b2_x1, b2_y1, b2_x2, b2_y2 = chat_x2 - 780, chat_y1 + 310, chat_x2 - 30, chat_y1 + 450
    draw.rounded_rectangle([b2_x1, b2_y1, b2_x2, b2_y2], radius=16, fill=(217, 253, 211, 255), outline=(180, 230, 180, 255))
    draw.text((b2_x1 + 22, b2_y1 + 20), "Hola Laura! Con gusto. Son 24 vasitos", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b2_x1 + 22, b2_y1 + 60), "surtidos por $60 USD en total.", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b2_x2 - 145, b2_y2 - 35), "10:15 AM", fill=(100, 150, 100, 255), font=f_time)
    draw_double_check(draw, b2_x2 - 50, b2_y2 - 30)
    
    # Bubble 3
    b3_x1, b3_y1, b3_x2, b3_y2 = chat_x1 + 30, chat_y1 + 490, chat_x1 + 750, chat_y1 + 630
    draw.rounded_rectangle([b3_x1, b3_y1, b3_x2, b3_y2], radius=16, fill=(255, 255, 255, 255), outline=(220, 220, 220, 255))
    draw.text((b3_x1 + 22, b3_y1 + 20), "Perfecto! Ya te hice la transferencia.", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b3_x1 + 22, b3_y1 + 60), "Muchas gracias, se ven hermosos!", fill=(20, 20, 20, 255), font=f_msg)
    draw.text((b3_x2 - 110, b3_y2 - 35), "10:16 AM", fill=(140, 140, 140, 255), font=f_time)
    
    card_bot_y1 = 1320
    card_bot_y2 = 1680
    add_drop_shadow(canvas, (50, card_bot_y1, w - 50, card_bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, card_bot_y1, w - 50, card_bot_y2], radius=22, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((85, card_bot_y1 + 35), "Aprende el Metodo de Ventas por WhatsApp", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 32))
    draw.text((85, card_bot_y1 + 85), "30 Recetas en Vasito + Scripts Listos + Calculadora", fill=(255, 223, 94, 255), font=get_font(FONT_REGULAR, 26))
    draw.text((85, card_bot_y1 + 130), "Empieza a generar ingresos desde tu propia cocina", fill=(210, 220, 235, 255), font=get_font(FONT_REGULAR, 24))
    draw.text((85, card_bot_y1 + 175), "Acceso Inmediato de por Vida - Garantia 7 Dias", fill=(100, 255, 150, 255), font=get_font(FONT_REGULAR, 24))
    
    btn_y = 1730
    draw.rounded_rectangle([60, btn_y, w - 60, btn_y + 95], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=3)
    btn_txt = "TOCA AQUI PARA DESCARGAR ($9.90 USD)"
    f_btn = get_font(FONT_BOLD, 32)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 26), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_3_whatsapp_story.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_3_whatsapp_story.jpg"), quality=95)
    print("V2 Criativo 3 WhatsApp Story updated!")

# ══════════════════════════════════════════════════════════════════
# FORMAT 4: HIGH-END EDITORIAL / LUXURY GASTRONOMY (Feed 1:1)
# ══════════════════════════════════════════════════════════════════

def create_format_4_editorial_feed():
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (8, 12, 20, 255))
    
    mousse_path = os.path.join(BASE_DIR, "mousse_chocolate.jpg")
    bg = Image.open(mousse_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    canvas.paste(ImageEnhance.Color(bg).enhance(1.15), (0, 0))
    
    top_over = Image.new("RGBA", (w, 320), (5, 8, 14, 235))
    bot_over = Image.new("RGBA", (w, 380), (5, 8, 14, 245))
    canvas.paste(top_over, (0, 0), top_over)
    canvas.paste(bot_over, (0, h - 380), bot_over)
    
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(FONT_BOLD, 22)
    f_title = get_font(FONT_SERIF, 46)
    f_sub = get_font(FONT_REGULAR, 24)
    
    draw.rounded_rectangle([100, 25, w - 100, 68], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    k_txt = "GUIA DIGITAL DE REPOSTERIA GOURMET"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 33), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    t_txt = "El Negocio Mas Rentable de Navidad"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 85), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    s_txt = "Aprende 30 Recetas de Alta Presentacion (100% Sin Horno)"
    bbox_s = f_sub.getbbox(s_txt)
    draw.text(((w - (bbox_s[2] - bbox_s[0])) // 2, 145), s_txt, fill=(240, 245, 255, 255), font=f_sub)
    
    p1_box = (60, 480, 360, 550)
    p2_box = (w - 360, 480, w - 60, 550)
    
    add_drop_shadow(canvas, p1_box, radius=12, offset=(0, 6), shadow_color=(0, 0, 0, 180))
    add_drop_shadow(canvas, p2_box, radius=12, offset=(0, 6), shadow_color=(0, 0, 0, 180))
    
    draw.rounded_rectangle(p1_box, radius=16, fill=(10, 18, 30, 240), outline=(255, 215, 0, 200), width=2)
    draw.rounded_rectangle(p2_box, radius=16, fill=(10, 18, 30, 240), outline=(100, 255, 150, 200), width=2)
    
    f_pill = get_font(FONT_BOLD, 22)
    draw.text((80, 500), "Costo: $0.60 USD / vasito", fill=(255, 215, 0, 255), font=f_pill)
    draw.text((w - 340, 500), "Venta: $2.50 USD / vasito", fill=(100, 255, 150, 255), font=f_pill)
    
    bot_y1 = 730
    bot_y2 = 1040
    add_drop_shadow(canvas, (50, bot_y1, w - 50, bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([50, bot_y1, w - 50, bot_y2], radius=20, fill=(12, 18, 28, 250), outline=(255, 215, 0, 220), width=3)
    
    f_card_h = get_font(FONT_BOLD, 30)
    f_card_b = get_font(FONT_REGULAR, 22)
    
    draw.text((85, bot_y1 + 25), "Manual Digital + 3 Bonos Exclusivos", fill=(255, 255, 255, 255), font=f_card_h)
    
    draw_vector_check(draw, 100, bot_y1 + 80, r=10)
    draw.text((125, bot_y1 + 68), "30 Recetas Paso a Paso - Sin Maquinaria - Listos en 15 Minutos", fill=(210, 225, 240, 255), font=f_card_b)
    
    draw_vector_check(draw, 100, bot_y1 + 115, r=10)
    draw.text((125, bot_y1 + 103), "Incluye Calculadora Excel + Guia de Empaques + Scripts WhatsApp", fill=(255, 223, 94, 255), font=f_card_b)
    
    btn_y = bot_y1 + 155
    draw.rounded_rectangle([75, btn_y, w - 75, btn_y + 80], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    btn_txt = "ACCEDE HOY CON 65% OFF - $9.90 USD"
    f_btn = get_font(FONT_BOLD, 28)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 22), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_4_editorial_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_4_editorial_feed.jpg"), quality=95)
    print("V2 Criativo 4 Editorial Feed updated!")

# ══════════════════════════════════════════════════════════════════
# FORMAT 5: COMPARATIVE TABLE / VISUAL OBJECTION BUSTER (Feed & Story)
# ══════════════════════════════════════════════════════════════════

def create_format_5_comparativo_feed():
    w, h = 1080, 1080
    canvas = Image.new("RGBA", (w, h), (12, 17, 26, 255))
    
    bg_path = os.path.join(BASE_DIR, "caja_regalo.jpg")
    bg = Image.open(bg_path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
    bg = bg.filter(ImageFilter.GaussianBlur(6))
    canvas.paste(bg, (0, 0))
    
    overlay = Image.new("RGBA", (w, h), (8, 14, 24, 215))
    canvas.paste(overlay, (0, 0), overlay)
    
    draw = ImageDraw.Draw(canvas)
    
    f_kicker = get_font(FONT_BOLD, 22)
    f_title = get_font(FONT_IMPACT, 52)
    
    draw.rounded_rectangle([100, 25, w - 100, 68], radius=20, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    k_txt = "DESCUBRE LA FORMA MAS FACIL DE EMPRENDER"
    bbox_k = f_kicker.getbbox(k_txt)
    draw.text(((w - (bbox_k[2] - bbox_k[0])) // 2, 33), k_txt, fill=(255, 255, 255, 255), font=f_kicker)
    
    t_txt = "PASTELERIA TRADICIONAL VS POSTRES EN VASITO"
    bbox_t = f_title.getbbox(t_txt)
    draw.text(((w - (bbox_t[2] - bbox_t[0])) // 2, 85), t_txt, fill=(255, 223, 94, 255), font=f_title)
    
    bw = 465
    bh = 540
    y_box = 160
    
    # Left Card (Pasteleria Tradicional)
    add_drop_shadow(canvas, (45, y_box, 45 + bw, y_box + bh), radius=12, offset=(0, 6), shadow_color=(0, 0, 0, 160))
    draw.rounded_rectangle([45, y_box, 45 + bw, y_box + bh], radius=18, fill=(25, 18, 22, 250), outline=(220, 60, 60, 220), width=3)
    
    draw.rounded_rectangle([45, y_box, 45 + bw, y_box + 65], radius=18, fill=(180, 30, 40, 255))
    f_col_h = get_font(FONT_BOLD, 24)
    draw.text((70, y_box + 18), "Pasteleria Tradicional", fill=(255, 255, 255, 255), font=f_col_h)
    
    f_bullet = get_font(FONT_REGULAR, 21)
    
    bad_items = [
        "Hornos costosos y calientes",
        "Batidoras industriales caras",
        "Horas de preparacion y horneado",
        "Alto riesgo de quemarse o hundirse",
        "Dificiles de empacar y transportar",
        "Margen de ganancia menor al 40%"
    ]
    
    for idx, item in enumerate(bad_items):
        iy = y_box + 100 + (idx * 65)
        draw_vector_cross(draw, 75, iy + 10, r=11)
        draw.text((100, iy), item, fill=(255, 180, 180, 255), font=f_bullet)
        
    # Right Card (Postres en Vasito)
    add_drop_shadow(canvas, (w - 45 - bw, y_box, w - 45, y_box + bh), radius=12, offset=(0, 6), shadow_color=(0, 0, 0, 160))
    draw.rounded_rectangle([w - 45 - bw, y_box, w - 45, y_box + bh], radius=18, fill=(15, 30, 24, 250), outline=(0, 200, 100, 230), width=3)
    
    draw.rounded_rectangle([w - 45 - bw, y_box, w - 45, y_box + 65], radius=18, fill=(0, 150, 70, 255))
    draw.text((w - 45 - bw + 45, y_box + 18), "Postres en Vasito Navidenos", fill=(255, 255, 255, 255), font=f_col_h)
    
    good_items = [
        "100% SIN HORNO (En frio)",
        "Solo utensilios de tu cocina",
        "Listos en solo 15 minutos",
        "Faciles, nunca se queman",
        "Porciones individuales perfectas",
        "Ganancia superior al 300%"
    ]
    
    for idx, item in enumerate(good_items):
        iy = y_box + 100 + (idx * 65)
        draw_vector_check(draw, w - 45 - bw + 35, iy + 10, r=11)
        draw.text((w - 45 - bw + 60, iy), item, fill=(150, 255, 190, 255), font=f_bullet)
        
    bot_y1 = 740
    bot_y2 = 1040
    add_drop_shadow(canvas, (45, bot_y1, w - 45, bot_y2), radius=16, offset=(0, 8))
    draw.rounded_rectangle([45, bot_y1, w - 45, bot_y2], radius=20, fill=(15, 22, 34, 250), outline=(255, 215, 0, 220), width=3)
    
    draw.text((85, bot_y1 + 25), "Aprende el Metodo en Vasito con 30 Recetas Paso a Paso", fill=(255, 255, 255, 255), font=get_font(FONT_BOLD, 28))
    draw.text((85, bot_y1 + 68), "Incluye 3 Bonos Gratis: Calculadora Excel + Empaques + Scripts WhatsApp", fill=(255, 223, 94, 255), font=get_font(FONT_REGULAR, 22))
    
    btn_y = bot_y1 + 130
    draw.rounded_rectangle([75, btn_y, w - 75, btn_y + 80], radius=16, fill=(196, 30, 58, 255), outline=(255, 215, 0, 220), width=2)
    btn_txt = "OBTEN EL MANUAL CON 65% DESCUENTO - $9.90 USD"
    f_btn = get_font(FONT_BOLD, 26)
    bbox_btn = f_btn.getbbox(btn_txt)
    draw.text(((w - (bbox_btn[2] - bbox_btn[0])) // 2, btn_y + 24), btn_txt, fill=(255, 255, 255, 255), font=f_btn)
    
    canvas.convert("RGB").save(os.path.join(BASE_DIR, "v2_criativo_5_comparativo_feed.jpg"), quality=95)
    canvas.convert("RGB").save(os.path.join(BRAIN_DIR, "v2_criativo_5_comparativo_feed.jpg"), quality=95)
    print("V2 Criativo 5 Comparativo Feed updated!")

if __name__ == "__main__":
    create_format_1_tweet_feed()
    create_format_1_tweet_story()
    create_format_2_catalogo_feed()
    create_format_2_catalogo_story()
    create_format_3_whatsapp_feed()
    create_format_3_whatsapp_story()
    create_format_4_editorial_feed()
    create_format_5_comparativo_feed()
