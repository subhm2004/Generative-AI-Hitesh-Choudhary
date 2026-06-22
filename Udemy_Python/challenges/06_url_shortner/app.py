# =============================================================================
# FILE    : app.py
# TOPIC   : URL Shortener Web App (Flask — lambi URL ko chhoti link banana)
# FOLDER  : challenges/06_url_shortner/
# CHALLENGE DAY : URL Shortener Challenge
# =============================================================================
#
# Jaise bit.ly — lambi website URL ko chhoti link mein badalte hain.
# Flask = Python web framework; models.py = database operations.

from flask import Flask, request, redirect, render_template
# Flask = web app banane ki library
# request = user ne kya bheja (form data, etc.)
# redirect = user ko doosri URL par bhejna
# render_template = HTML page dikhana

import random
import string  # ascii_letters + digits = random short code ke liye

# models.py se database functions import — alag file mein rakha clean code ke liye
from models import (
    init_db, 
    insert_url, 
    get_url, 
    get_all_urls, 
    increment_visit_count, 
    delete_url_by_code
    )

# Flask app object — yeh poori web application hai
app = Flask(__name__)

# App start hote hi database table create karo (agar nahi hai)
init_db()


def generate_short_code(length=6):
    """
    Random short code banata hai — jaise 'aB3xY9'
    length=6 matlab 6 characters; letters + numbers mix
    """
    # random.choices() list se random pick karta hai, k baar — join se string ban jati hai
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# @app.route = URL path define karta hai — "/" = homepage
# methods=['GET', 'POST'] = page dekhna (GET) ya form submit (POST) dono allow
@app.route("/", methods=['GET', 'POST'])
def index():
    """
    Homepage — URL submit karo ya saari shortened links ki list dekho.
    """
    if request.method == 'POST':
        # User ne form submit kiya — form se 'url' field ki value lo
        orginal_url = request.form['url']
        # Naya random short code banao
        short_code = generate_short_code()
        # Database mein save karo
        insert_url(orginal_url, short_code)
        # Redirect homepage par — form dubara submit na ho (POST-redirect-GET pattern)
        return redirect("/")

    # GET request — saari URLs database se lao aur HTML template ko bhejo
    all_urls = get_all_urls()
    return render_template('index.html', all_urls=all_urls)


@app.route("/about")
def about():
    """Simple about page — plain text return"""
    return 'this is an amazing course on python - Udemy'


# <short_code> = dynamic part — jaise /aB3xY9
# Jab koi short link open kare, original URL par redirect
@app.route('/<short_code>')
def redirect_url(short_code):
    """
    Short code se original URL dhundho aur user ko wahan bhej do.
    Visit count bhi badhao — kitni baar link khuli.
    """
    url_data = get_url(short_code)
    if url_data:
        # Link mili — visit count +1
        increment_visit_count(short_code)
        # url_data[1] = original_url column (tuple ka index 1)
        return redirect(url_data[1])

    # Short code database mein nahi — 404 error page
    return render_template('404.html'), 404


# POST se delete — form/button se short link hatao
@app.route('/delete/<short_code>', methods=['POST'])
def delete_url(short_code):
    """Database se URL entry delete karo aur homepage par wapas jao"""
    delete_url_by_code(short_code)
    return redirect("/")


# Sirf tab chale jab directly python app.py run karo (development server)
if __name__ == '__main__':
    app.run(
        debug=True,       # debug=True = errors detail mein, auto-reload on code change
        host='0.0.0.0',   # Sab network interfaces par suno — local network se bhi access
        port=8000         # Browser mein http://localhost:8000
        )
