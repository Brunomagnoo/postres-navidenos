import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_hotmart_mockup():
    w, h = 1000, 1000
    
    # Base canvas
    img = Image.new("RGBA", (w, h), (12, 17, 26, 255))
    draw = ImageDraw.Draw(img)
    
    # Load and process hero image as background backdrop with blur and dark gradient
    hero_path = r"C:\Users\bruno\.gemini\antigravity\scratch\postres-navidenos\hero_portada.jpg"
    caja_path = r"C:\Users\bruno\.gemini\antigravity\scratch\postres-navidenos\caja_regalo.jpg"
    
    if os.path.exists(hero_path):
        bg = Image.open(hero_path).convert("RGBA")
        bg = bg.resize((w, h), Image.Resampling.LANCZOS)
        bg_blur = bg.filter(ImageFilter.GaussianBlur(radius=6))
        overlay = Image.new("RGBA", (w, h), (10, 14, 20, 205))
        bg_blur.paste(overlay, (0, 0), overlay)
        img.paste(bg_blur, (0, 0))
    
    # Fonts
    font_bold_path = "C:\\Windows\\Fonts\\arialbd.ttf"
    font_impact = "C:\\Windows\\Fonts\\impact.ttf"
    
    font_kicker = ImageFont.truetype(font_bold_path, 24)
    font_title_main = ImageFont.truetype(font_impact, 68)
    font_title_sub = ImageFont.truetype(font_bold_path, 36)
    font_badge = ImageFont.truetype(font_bold_path, 25)
    font_bullet = ImageFont.truetype(font_bold_path, 22)
    
    # Top Kicker Banner
    banner_y = 42
    banner_h = 50
    draw.rounded_rectangle([70, banner_y, w - 70, banner_y + banner_h], radius=25, fill=(196, 30, 58, 250), outline=(255, 215, 0, 220), width=2)
    kicker_text = "EDICION ESPECIAL NAVIDAD · GUIA PRACTICA 2024"
    bbox = font_kicker.getbbox(kicker_text)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, banner_y + 12), kicker_text, fill=(255, 255, 255, 255), font=font_kicker)
    
    # Main Product Title
    title_1 = "POSTRES NAVIDEÑOS"
    bbox1 = font_title_main.getbbox(title_1)
    tw1 = bbox1[2] - bbox1[0]
    draw.text(((w - tw1) // 2 + 3, 115 + 3), title_1, fill=(0, 0, 0, 240), font=font_title_main)
    draw.text(((w - tw1) // 2, 115), title_1, fill=(255, 223, 94, 255), font=font_title_main)
    
    title_2 = "RENTABLES EN VASITOS"
    bbox2 = font_title_sub.getbbox(title_2)
    tw2 = bbox2[2] - bbox2[0]
    draw.text(((w - tw2) // 2 + 2, 190 + 2), title_2, fill=(0, 0, 0, 220), font=font_title_sub)
    draw.text(((w - tw2) // 2, 190), title_2, fill=(255, 255, 255, 255), font=font_title_sub)
    
    # Subtitle Pills
    pill_text = "30 RECETAS PASO A PASO · 100% SIN HORNO"
    bbox_p = font_badge.getbbox(pill_text)
    tw_p = bbox_p[2] - bbox_p[0]
    pill_x1 = (w - tw_p) // 2 - 24
    pill_x2 = (w + tw_p) // 2 + 24
    draw.rounded_rectangle([pill_x1, 246, pill_x2, 290], radius=18, fill=(0, 168, 77, 245), outline=(255, 255, 255, 180), width=1)
    draw.text(((w - tw_p) // 2, 254), pill_text, fill=(255, 255, 255, 255), font=font_badge)
    
    # Center Showcase: Inset Card with Caja Regalo
    card_x1, card_y1, card_x2, card_y2 = 135, 318, w - 135, 825
    
    if os.path.exists(caja_path):
        caja = Image.open(caja_path).convert("RGBA")
        target_cw = card_x2 - card_x1
        target_ch = card_y2 - card_y1
        caja_resized = caja.resize((target_cw, target_ch), Image.Resampling.LANCZOS)
        
        mask = Image.new("L", (target_cw, target_ch), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([0, 0, target_cw, target_ch], radius=24, fill=255)
        
        draw.rounded_rectangle([card_x1 - 6, card_y1 - 6, card_x2 + 6, card_y2 + 6], radius=28, fill=(0, 0, 0, 190))
        img.paste(caja_resized, (card_x1, card_y1), mask)
        draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=24, outline=(255, 215, 0, 220), width=4)
        
        # Floating badge top-left: "+ 3 BONOS DE REGALO"
        badge_text_1 = "+3 BONOS DE REGALO"
        bbox_b1 = font_bullet.getbbox(badge_text_1)
        bw1 = bbox_b1[2] - bbox_b1[0]
        b_x1, b_y1, b_x2, b_y2 = card_x1 + 18, card_y1 + 18, card_x1 + 18 + bw1 + 36, card_y1 + 68
        draw.rounded_rectangle([b_x1, b_y1, b_x2, b_y2], radius=12, fill=(196, 30, 58, 250), outline=(255, 255, 255, 220), width=2)
        draw.text((b_x1 + 18, b_y1 + 12), badge_text_1, fill=(255, 255, 255, 255), font=font_bullet)
        
        # Floating badge bottom-right: "CALCULADORA EXCEL INCLUIDA"
        badge_text_2 = "Calculadora Excel Incluida"
        bbox_b2 = font_bullet.getbbox(badge_text_2)
        bw2 = bbox_b2[2] - bbox_b2[0]
        b2_x1, b2_y1, b2_x2, b2_y2 = card_x2 - bw2 - 54, card_y2 - 68, card_x2 - 18, card_y2 - 18
        draw.rounded_rectangle([b2_x1, b2_y1, b2_x2, b2_y2], radius=12, fill=(22, 27, 34, 250), outline=(255, 215, 0, 220), width=2)
        draw.text((b2_x1 + 18, b2_y1 + 12), badge_text_2, fill=(255, 223, 94, 255), font=font_bullet)
    
    # Bottom Benefit Bar
    bot_y1 = 855
    bot_y2 = 945
    draw.rounded_rectangle([45, bot_y1, w - 45, bot_y2], radius=20, fill=(15, 23, 42, 245), outline=(255, 255, 255, 70), width=2)
    
    bullet_line = "Acceso Inmediato de por Vida  |  Costos desde $0.60 USD  |  Garantia 7 Dias"
    bbox_b = font_bullet.getbbox(bullet_line)
    tw_b = bbox_b[2] - bbox_b[0]
    draw.text(((w - tw_b) // 2, bot_y1 + 32), bullet_line, fill=(255, 255, 255, 255), font=font_bullet)
    
    out_1000 = r"C:\Users\bruno\.gemini\antigravity\scratch\postres-navidenos\hotmart_cover_1000.png"
    out_600 = r"C:\Users\bruno\.gemini\antigravity\scratch\postres-navidenos\hotmart_cover_600.png"
    out_jpg = r"C:\Users\bruno\.gemini\antigravity\scratch\postres-navidenos\hotmart_cover_600.jpg"
    
    rgb_img = img.convert("RGB")
    rgb_img.save(out_1000, quality=95)
    
    img_600 = rgb_img.resize((600, 600), Image.Resampling.LANCZOS)
    img_600.save(out_600, quality=95)
    img_600.save(out_jpg, quality=95)
    
    print("Hotmart covers re-generated with clean typography!")

if __name__ == "__main__":
    create_hotmart_mockup()
