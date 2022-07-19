from flask import *
import random
from word_list import word_list

app = Flask("__name__")
app.secret_key = "saheedwqere3464ghfkuj90"

word = ''
def gen_word():
	word = random.choice(word_list).upper()
	return word
	

@app.route("/play", methods = ["POST", "GET"])
def page():
	if request.method == "POST":
		if 'word' in session:
			word = session['word']
		else:
			word = gen_word()

		if "answer" in session and "answer2" in session and "answer3" in session and "answer4" in session and "answer5" in session:
			if request.form["answer"] in word_list and len(request.form["answer"])==5:
				answer6 = request.form["answer"]
				session["answer6"] = answer6
				answer6 = session["answer6"].upper()

				answer=session["answer"].upper()
				answer2 = session["answer2"].upper()
				answer3=session["answer3"].upper()
				answer4 = session["answer4"].upper()
				answer5 = session["answer5"].upper()
				return render_template("index.html", answer= answer,
				 answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5, answer6=answer6, word=word)
			else:
				answer=session["answer"].upper()
				answer2 = session["answer2"].upper()
				answer3 = session["answer3"].upper()
				answer4 = session["answer4"].upper()
				answer5 = session["answer5"].upper()
				flash("Invalid word", "danger")
				return render_template("index.html", answer= answer, answer2=answer2,
				 answer3=answer3, answer4=answer4, answer5=answer5, word=word)

		elif "answer" in session and "answer2" in session and "answer3" in session and "answer4" in session:
			if request.form["answer"] in word_list and len(request.form["answer"])==5:
				answer5 = request.form["answer"]
				session["answer5"] = answer5
				answer5 = session["answer5"].upper()

				answer=session["answer"].upper()
				answer2 = session["answer2"].upper()
				answer3=session["answer3"].upper()
				answer4 = session["answer4"].upper()
				return render_template("index.html", answer= answer,
				 answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5, word=word)
			else:
				answer=session["answer"].upper()
				answer2 = session["answer2"].upper()
				answer3 = session["answer3"].upper()
				answer4 = session["answer4"].upper()
				flash("Invalid word", "danger")
				return render_template("index.html", answer= answer, answer2=answer2,
				 answer3=answer3, answer4=answer4, word=word)

		elif "answer" in session and "answer2" in session and "answer3" in session:
			if request.form["answer"] in word_list and len(request.form["answer"])==5:
				answer4 = request.form["answer"]
				session["answer4"] = answer4
				answer4 = session["answer4"].upper()

				answer=session["answer"].upper()
				answer2 = session["answer2"].upper()
				answer3=session["answer3"].upper()
				return render_template("index.html", answer= answer,
				 answer2=answer2, answer3=answer3, answer4=answer4, word=word)
			else:
				answer=session["answer"].upper()
				answer2 = session["answer2"].upper()
				answer3 = session["answer3"].upper()
				flash("Invalid word", "danger")
				return render_template("index.html", answer= answer, answer2=answer2, answer3=answer3, word=word)

		elif "answer" in session and "answer2" in session:
			if request.form["answer"] in word_list and len(request.form["answer"])==5:
				answer3 = request.form["answer"]
				session["answer3"] = answer3
				answer3 = session["answer3"].upper()

				answer=session["answer"].upper()
				answer2 = session["answer2"].upper()

				return render_template("index.html", answer= answer, answer2=answer2, answer3=answer3, word=word)
			else:
				answer=session["answer"].upper()
				answer2 = session["answer2"].upper()
				flash("Invalid word", "danger")
				return render_template("index.html", answer= answer, answer2=answer2, word=word)

		elif "answer" in session:
			if request.form["answer"] in word_list and len(request.form["answer"])==5:
				answer2 = request.form["answer"]
				session["answer2"] = answer2
				answer2 = session["answer2"].upper()

				answer=session["answer"].upper()
				return render_template("index.html", answer=answer, answer2=answer2, word=word)
			else:
				answer=session["answer"].upper()
				flash("Invalid word", "danger")
				return render_template("index.html", answer=answer, word=word)

		else:
			if request.form["answer"] in word_list and len(request.form["answer"])==5:
				answer = request.form["answer"]
				session["answer"] = answer
				answer = session["answer"].upper()

				return render_template("index.html", answer=answer, word=word)
			else:
				flash("Invalid word", "danger")
				return render_template("index.html", word=word)

	else:
		word = gen_word()
		session['word'] = word
		return render_template("index.html", word=word)

@app.route("/")
def again():
	session.clear()
	return redirect(url_for("page"))

if __name__ == "__main__":
	app.run(port=2222, debug=True)
 