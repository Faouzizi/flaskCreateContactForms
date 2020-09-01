###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from forms import ContactForm
import pandas as pd

###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'dev fao football app'

###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
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

###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True)
