from multiprocessing.spawn import import_main_path
from flask import Flask, redirect, render_template, send_file, send_from_directory, url_for

app = Flask(__name__)
#Redirect default route to the profile page route
@app.route("/")
def index():
    return redirect(url_for('profile'))
#Display profile_page file who is in the template folder
@app.route("/profile")
def profile():
    return render_template('profile_page.html')
#Define the icon of the site
@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static","favicon.ico","assets/icon/icon2.png")
#Customize the error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found_page.html'), 404
if __name__ == "__main__":
    app.run("localhost",port=5000,debug=True)