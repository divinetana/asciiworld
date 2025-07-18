from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

# List all available fonts from pyfiglet
available_fonts = pyfiglet.FigletFont.getFonts()

# Format the font names: replace underscores with spaces and capitalize each word
formatted_fonts = [font.replace('_', ' ').title() for font in available_fonts]

@app.route("/", methods=["GET", "POST"])
def index():
    ascii_art = ""
    selected_font = "Graffiti"  # Default font (capitalized correctly)
    text_input = "Type Something"
    char_width = "10"
    char_height = "16"

    if request.method == "POST":
        text_input = request.form.get("text")
        selected_font = request.form.get("font", "Graffiti")

        # Ensure the font is in the correct format (capitalized)
        selected_font = selected_font.replace(' ', '_').lower()

        # Check if the selected font is available in pyfiglet
        if selected_font not in available_fonts:
            selected_font = 'slant'  # Fallback to a default font if it's not available

        # Generate ASCII art with the selected font
        ascii_art = pyfiglet.figlet_format(text_input, font=selected_font)

        char_width = request.form.get("charWidth", "10")
        char_height = request.form.get("charHeight", "16")

    return render_template("index.html", 
                           ascii_art=ascii_art, 
                           fonts=formatted_fonts,  # Use formatted fonts
                           text_input=text_input, 
                           selected_font=selected_font,
                           char_width=char_width, 
                           char_height=char_height)

@app.route("/preview", methods=["POST"])
def preview():
    text = request.form.get("text", "Type something")
    font = request.form.get("font", "Graffiti")

    # Ensure the font is in the correct format (capitalized)
    font = font.replace(' ', '_').lower()

    # Check if the selected font is available in pyfiglet
    if font not in available_fonts:
        font = 'slant'  # Fallback to default font

    # Generate ASCII art with the selected font
    ascii_art = pyfiglet.figlet_format(text, font=font)
    return ascii_art

if __name__ == "__main__":
    app.run(debug=True)
