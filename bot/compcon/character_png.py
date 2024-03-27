# We use imgkit to generate a png from html
import imgkit

# Generate PNG from HTML content
def generate_png(html_content):
    options = {
        "format": "png",
        "quiet": ""
    }
    return imgkit.from_string(html_content, False, options=options) 
