from PIL import Image, ImageDraw, ImageFont

class ImageLoader:
    def __init__(self):
        self.loaded_image: Image = None
        self.watermarked_image: Image = None

    def load_image(self, filename: str) -> Image:
        self.loaded_image = Image.open(filename)
        return self.loaded_image

    def add_watermark(self, watermark_text: str) -> Image:
        self.watermarked_image = self.loaded_image.copy()
        img_width, img_height = self.watermarked_image.size
        font_size = img_width/len(watermark_text)
        draw = ImageDraw.Draw(self.watermarked_image)
        font = ImageFont.truetype("Geneva.ttf", font_size)
        bbox = draw.textbbox((0, 0), f"@{watermark_text}", font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        if text_width > img_width or text_height > img_height:
            font_size = font_size*0.6
            font = ImageFont.truetype("Geneva.ttf", font_size)
        draw.text((0,img_height/2-font_size), f"@{watermark_text}", (255,255,255, 0), font=font)
        return self.watermarked_image

