import PIL.Image
from product.utils.delete_temp_image import delete_temp_image

def image_to_ascii(image_path, size):
    try:
        image = PIL.Image.open(image_path)
        
        width, height = image.size
        aspect_ratio = height/width
        new_width = 20 if size == 'xs' else 50 if size == 's' else 90 if size == 'md' else 140 if size == 'lg' else 200
        new_height = aspect_ratio * new_width * 0.55
        image = image.resize((new_width, int(new_height)))
        
        image = image.convert('L')
        
        chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
        
        pixels = image.getdata()
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        new_pixels_count = len(new_pixels)
        ascii_art = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_art = "\n".join(ascii_art)
        delete_temp_image(image_path)
        return {"success": True, "ascii_art": ascii_art}

    except Exception as e:
        return {'error': f'{e}'}