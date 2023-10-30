import io
import base64
from PIL import Image
from product.utils.delete_temp_image import delete_temp_image

def base64_to_image(base64_string, output_path):
    delete_temp_image(output_path)

    try:
        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data))
        image.save(output_path)
        return {'success': True}

    except Exception as e:
        return {'error': f'{e}'}