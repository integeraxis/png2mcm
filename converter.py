from PIL import Image
from utils import showerror

TILE_WIDTH = 12
TILE_HEIGHT = 18

TABLE_WIDTH = 16
TABLE_HEIGHT = 16

TOTAL_WIDTH = TILE_WIDTH*TABLE_WIDTH
TOTAL_HEIGHT = TILE_HEIGHT*TABLE_HEIGHT


COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_TRANSPARENT = (127, 127, 127)

ALLOWED_COLORS = (COLOR_WHITE, COLOR_BLACK, COLOR_TRANSPARENT)

COLOR_TO_BITS = {COLOR_WHITE:"10", COLOR_BLACK:"00", COLOR_TRANSPARENT:"01"}

def rgb_to_hex(rgb:tuple) -> str:
    ##Convert an (R, G, B) tuple to a #HEX color string
    r, g, b = rgb
    return f"#{r:02X}{g:02X}{b:02X}"

# normal .png is a png that is 192x288 (so no spacing between tiles)
# a betaflight font .png is a normal png but with red borders between the tiles (useful if ur editing a betaflight .png)
def open_normal_png(path):
    img = Image.open(path)
    img = img.convert("RGB")
    if img.width != TOTAL_WIDTH or img.height != TOTAL_HEIGHT:
        showerror(f"Incorrect image size, image size needs to be {TOTAL_WIDTH}x{TOTAL_HEIGHT} pixels.")
        return -1

    return img

def open_betaflight_png(path):
    img = Image.open(path)
    if img.width != (TOTAL_WIDTH+(TABLE_WIDTH-1)) or img.height != (TOTAL_HEIGHT+(TABLE_HEIGHT-1)):
        showerror(f"Incorrect image size, image size needs to be {TOTAL_WIDTH+(TABLE_WIDTH-1)}x{TOTAL_HEIGHT+(TABLE_HEIGHT-1)} pixels.")
        return -1

    #image with red lines removed
    img_clean = Image.new(mode="RGB", size=(TOTAL_WIDTH, TOTAL_HEIGHT))

    for y in range(TABLE_HEIGHT):
        for x in range(TABLE_WIDTH):
            y_px = y*TILE_HEIGHT + y
            x_px = x*TILE_WIDTH + x

            tile = img.crop((x_px, y_px, x_px+TILE_WIDTH, y_px+TILE_HEIGHT))

            img_clean.paste(tile, (x*TILE_WIDTH, y*TILE_HEIGHT))

    return img_clean


def convert_tile(tile_img:Image):
    data=""
    #there are 64 bytes per tile, the rest is padded with COLOR_TRANSPARENT ("01")
    BYTES_PER_TILE = 64
    bytes_per_tile_used = ((TILE_WIDTH*TILE_HEIGHT)*2)//8

    #the maximum amount of 2bit pairs on one line is 4 = 1byte per line
    # I use this var to keep track of how many 2bit pairs we have put on this line
    bit_idx = 0
    bytes_used = 0
    for y in range(TILE_HEIGHT):
        for x in range(TILE_WIDTH):
            color = tile_img.getpixel((x, y))
            if color not in ALLOWED_COLORS:
                showerror(f"{rgb_to_hex(color)} is not an allowed color. The only allowed colors are: {", ".join(rgb_to_hex(c) for c in ALLOWED_COLORS)}.")
                return -1

            bits = COLOR_TO_BITS[color]
            data += bits
            bit_idx += 1
            if bit_idx >= 4:
                data += "\n"
                bit_idx = 0
                bytes_used += 1


    if bytes_used <= BYTES_PER_TILE:
        data += ((COLOR_TO_BITS[COLOR_TRANSPARENT]*4)+"\n")*(BYTES_PER_TILE-bytes_per_tile_used)

    return data


def convert(img:Image, mcm_path):
    data = ""
    data += "MAX7456\n"

    for y in range(TABLE_HEIGHT):
        for x in range(TABLE_WIDTH):
            x_px = x*TILE_WIDTH
            y_px = y*TILE_HEIGHT
            tile = img.crop((x_px, y_px, x_px+TILE_WIDTH, y_px+TILE_HEIGHT))

            result = convert_tile(tile)

            if result == -1:
                return -1

            data += result




    with open(mcm_path, "w", newline="") as mcm:
        mcm.write(data)
