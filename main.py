from flask import Flask, render_template, request

app = Flask(__name__)

# temporary in-memory storage (later you can connect Google Sheets or a database)
submissions = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        class_name = request.form['class_name']
        section = request.form['section']
        team_name = request.form['team_name']
        members = request.form['members']
        model = request.form['model']

        # Save in memory
        submissions.append({
            'class': class_name,
            'section': section,
            'team_name': team_name,
            'members': members,
            'model': model
        })
        return f"<h2>✅ Data submitted successfully for {class_name}{section}!</h2><a href='/'>Go Back</a>"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
