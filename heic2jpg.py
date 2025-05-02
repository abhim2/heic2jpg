import os
import sys
from PIL import Image
from pillow_heif import register_heif_opener

def convert_heic_to_jpg(input_path):
    try:
        # Register HEIF opener
        register_heif_opener()
        
        # Open the HEIC image
        img = Image.open(input_path)
        
        # Create output path by replacing extension
        output_path = os.path.splitext(input_path)[0] + '.jpg'
        
        # Convert and save as JPEG
        img.save(output_path, 'JPEG', quality=95)
        return True, output_path
    except Exception as e:
        return False, str(e)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if os.path.exists(input_file) and input_file.lower().endswith('.heic'):
            success, result = convert_heic_to_jpg(input_file)
            if success:
                print(f"Successfully converted to: {result}")
            else:
                print(f"Error: {result}")
        else:
            print("Please provide a valid HEIC file path") 