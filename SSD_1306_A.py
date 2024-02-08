# Feb 8, 2024

import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


# Change these to the right size for your display!
WIDTH = 128
HEIGHT = 32  
BORDER = 5

# Use for I2C.
i2c = board.I2C()  # uses board.SCL and board.SDA
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)  # Removed reset


# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# font = ImageFont.load_default(30)  # Number is the font size

# Documentation:  https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

text = "CMD 10"
# draw.text((0,0), text, font=font,fill=1,)  # First parameter is position of text, 
#                                            # Second paramter is the text to be displayed
#                                            # Third is Font to be used
#                                            # Forth is the color:   0 is black, 1 is blue


draw.text((0,0), "TEST", font=ImageFont.load_default(30), fill=1)  
                                           # First parameter is position of text, 
                                           # Second paramter is the text to be displayed
                                           # Third is Font to be used
                                           # Forth is the color:   0 is black, 1 is blue


# Display image
oled.image(image)
oled.show()

