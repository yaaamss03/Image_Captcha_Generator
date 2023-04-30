# Importing modules
from captcha.image import ImageCaptcha

# Creating an image object
image = ImageCaptcha(width = 280, height = 90)

# Image captcha text
captcha_text = 'Yamini'

# generating the image
data = image.generate(captcha_text)

# writing the image on the given file and saving it
image.write(captcha_text, 'CAPTCHA.png')
