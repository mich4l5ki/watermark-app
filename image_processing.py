from PIL import Image, ImageDraw, ImageFont

class ImageLoader:
    def __init__(self):
        self.loaded_image: Image = None
        self.watermarked_image: Image = None

    def load_image(self, filename: str) -> Image:
        self.loaded_image = Image.open(filename)
        return self.loaded_image

    def add_watermark(self, watermark_text: str) -> Image:
        if self.loaded_image is None:
            return False
        self.watermarked_image = self.loaded_image.copy()

        img_width, img_height = self.watermarked_image.size

        font_size = img_width/len(watermark_text)
        font = ImageFont.truetype("Geneva.ttf", font_size)

        draw = ImageDraw.Draw(self.watermarked_image)
        _, _, w, h = draw.textbbox((0,0), f"@{watermark_text}", font=font)
        draw.text(((img_width-w)/2, (img_height-h)/2), f"@{watermark_text}", font=font)

        return self.watermarked_image

    def _get_text_diamaters(self, draw, watermark_text, font):
        bbox = draw.textbbox((0, 0), f"@{watermark_text}", font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        return text_width, text_height
