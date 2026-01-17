from flask import Flask, render_template

app = Flask(__name__)

# Fake blog data (we'll replace this with a database later)
POSTS = [
    {
        "title": "Shark Attack",
        "slug": "shark-attack",   #this is the url address 
         "excerpt": "A calm swim, a sudden shadow, and a lesson in reading the ocean...",
        "image": "images/thumbs/shark.jpg",  # put image in static/thumbs/
        "content": "When I was a baby I got eaten by a shark.\n\n I lived.",
    },
    {
        "title": "My friend the Octopus",
        "slug": "my-friend-the-octopus",
        "excerpt": "An unexpected companion in the shallows and a surprisingly curious gaze.",
        "image": "images/thumbs/octopus.jpg",
        "content": "I made friends with an Octopus.\n\nPerfect.",
    },
]


@app.route("/")
def landing():
    return render_template("landing.html", posts=POSTS)

# This can be used when enough blogs are made and render it necessary to have a seperate list page not just the landing page
# @app.route("/blog")
# def blog():
#     return render_template("blog.html", posts=POSTS)


@app.route("/blog/<slug>")
def blog_post(slug):
    post = next((p for p in POSTS if p["slug"] == slug), None)
    if not post:
        return "You Got Inked!", 404

    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(host ="0.0.0.0", debug=True)
    #app.run(debug=True)
