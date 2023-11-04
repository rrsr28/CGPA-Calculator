from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cgpa():
    if request.method == 'POST':
        n = int(request.form.get('subjects'))
        grades = [int(grade) for grade in request.form.getlist('grade')]
        credits = [int(credit) for credit in request.form.getlist('credit')]
        sumTotal = sum(grades[i] * credits[i] for i in range(n)) / sum(credits)
        return render_template('cgpa.html', cgpa=sumTotal)
    return render_template('cgpa.html')


if __name__ == "__main__":
    app.run(debug=True)