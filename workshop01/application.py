from flask import Flask, render_template
from random import randint
application = Flask(__name__)

list_of_text = list()
list_of_text.append("Logic will get you from A to B. Imagination will take you everywhere.")
list_of_text.append("There are 10 kinds of people. Those who know binary and those who don't.")
list_of_text.append("There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies")
list_of_text.append("It's not that I'm so smart, it's just that I stay with problems longer.")
list_of_text.append("It is pitch dark. You are likely to be eaten by a grue.")
@application.route('/')
def homepage():
    text_to_display = list_of_text[randint(0, 4)]
    return render_template("index.html", dynamic_text = text_to_display)
if __name__ == "__main__":
    application.run(port=8000)