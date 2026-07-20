from PIL import Image

def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    message += chr(0) 
    binary_msg = ''.join(format(ord(c), '08b') for c in message)

    data_index = 0
    pixels = encoded.load()
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_msg):
                r, g, b = pixels[x, y][:3]
                r = (r & ~1) | int(binary_msg[data_index])
                pixels[x, y] = (r, g, b)
                data_index += 1
    encoded.save(output_path)
    print(f"Message hidden in {output_path}")

