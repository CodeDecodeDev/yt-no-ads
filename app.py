from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main_page():
    if request.method == "POST":
        vid_url = request.form["URL"]
        if len(vid_url) == 28:
            vid_url_id = vid_url[17:]
        elif len(vid_url) == 43:
            vid_url_id = vid_url[32:]
        return redirect(url_for("video_page", vid_id = vid_url_id))
    else:
        return render_template("home.html")


@app.route("/<vid_id>")
def video_page(vid_id):
    return f"<iframe width=\"1280\" height=\"720\" src=\"https://www.youtube.com/embed/{vid_id}\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>"

if __name__ == "__main__":
    app.run(debug = True)