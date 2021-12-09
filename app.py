from flask import Flask, render_template, request


from forms import ContactForm
import pandas as pd

app = Flask(__name__)
app.secret_key = 'secretKey'


@app.route('/home')
def home():
    return render_template ('index.html')


@app.route('/recipes')
def recipes():
    return render_template ('recipes.html')

@app.route('/tips')
def tips():
    return render_template ('tips.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/accessibility')
def accessibility():
    return render_template ('accessibility.html')


@app.route('/recipe')
def recipe():
    return render_template ('recipe.html')


@app.route('/croquetas')
def croquetas():
    return render_template ('croquetas.html')

@app.route('/cupcakes')
def cupcakes():
    return render_template ('cupcakes.html')

@app.route('/toast')
def toast():
    return render_template ('toast.html')

@app.route('/paella')
def paella():
    return render_template ('paella.html')

@app.route('/chococake')
def chococake():
    return render_template ('chococake.html')

@app.route('/chickensalad')
def chickensalad():
    return render_template ('chickensalad.html')







@app.route('/contact', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    # here, if the request type is a POST we get the data on contact
    #forms and save them else we return the contact forms html page
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)
	

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
