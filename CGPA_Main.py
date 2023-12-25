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

"""def calculate_CGPA(image_path):
    import cv2
    import pytesseract

    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to get a binary image
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(binary)

    points = 0
    credit_hours = 0

    for line in text.split('\n'):
        if 'CREDITS' in line:
            credit_hours += int(line.split()[0])

        if 'GRADE' in line:
            grade = line.split()[0]
            if grade == '0':
                points += 10
            elif grade == 'A+':
                points += 9
            elif grade == 'A':
                points += 8
            elif grade == 'B+':
                points += 7
            elif grade == 'B':
                points += 6
            elif grade == 'C':
                points += 5

    if credit_hours != 0:
        CGPA = points / credit_hours
    else:
        CGPA = 0

    return CGPA

image_path = 'ImagePath''
CGPA = calculate_CGPA(image_path)
print(f'Your CGPA is: {CGPA}')"""