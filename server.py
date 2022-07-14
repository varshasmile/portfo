from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
	return render_template("index.html")

# @app.route('/generic.html')
# def generic():
# 	return render_template("generic.html")

# @app.route('/elements.html')
# def elements():
# 	return render_template("elements.html")

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open("database.txt", mode='a') as database:
		name = data['name']
		email = data['email']
		message = data['message']
		file = database.write(f'\n{name}, {email}, {message}')

def write_to_csv(data):
	with open("database.csv", mode='a', newline='') as database2:
		name = data['name']
		email = data['email']
		message = data['message']
		csv_write = csv.writer(database2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_write.writerow([name,email,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_file(data)
    	write_to_csv(data)
    	return 'form submitted!!!!'
    else:
    	return 'something went wrong, Try again!'

if __name__ == "__main__":
    app.run(debug=True)