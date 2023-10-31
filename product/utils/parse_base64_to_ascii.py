import io
import base64
from PIL import Image

def base64_to_ascii(base64_string, size):
    try:
        splited = base64_string.split(',')

        if len(splited) > 1:
            encode = splited[1]
        else:
            encode = splited[0]
        
        image_data = base64.b64decode(encode)
        image = Image.open(io.BytesIO(image_data))

        width, height = image.size
        aspect_ratio = height/width
        new_width = 30 if size == 'xs' else 50 if size == 's' else 80 if size == 'md' else 120 if size == 'lg' else 170
        new_height = aspect_ratio * new_width * 0.55
        image = image.resize((new_width, int(new_height)))

        image = image.convert('L')
        chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", ".",]
        
        pixels = image.getdata()
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        new_pixels_count = len(new_pixels)
        ascii_art = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_art = "\n".join(ascii_art)
        print(ascii_art)
        return {"success": True, "ascii_art": ascii_art}

    except Exception as e:
        return {'error': f'{e}'}
