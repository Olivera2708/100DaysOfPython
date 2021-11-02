from flask import Flask, render_template, request
import requests
from post import Post
import smtplib

EMAIL = ""
PASSWORD = ""

response = requests.get("https://api.npoint.io/88c2c1f644ef334058be")
posts = response.json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["date"], post["author"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route('/index.html')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route('/post.html/<int:index>')
def post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_mail(name, email, phone, message):
    email_message = f"Subject:New MEssage\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMEssage: {message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, email, email_message)

if __name__ == "__main__":
    app.run(debug=True)