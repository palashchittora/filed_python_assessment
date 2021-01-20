# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return "Welcome to the App"
#
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, DateTimeField, DecimalField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class PaymentForm(Form):
    # name = TextField('Name:', validators=[validators.DataRequired()])
    # email = TextField('Email:', validators=[validators.DataRequired(), validators.Length(min=6, max=35)])
    # password = TextField('Password:', validators=[validators.DataRequired(), validators.Length(min=3, max=35)])

    CreditCardNumber =TextField('Credit Card number: ', validators=[validators.DataRequired(), validators.Length(min=16, max=16)])
    CardHolder = TextField('Card holder: ', validators=[validators.DataRequired()])
    ExpirationDate =DateTimeField('Expiration Date: ', validators=[validators.DataRequired()])
    SecurityCode =TextField('Security code: ', validators=[validators.Length(min=3, max=3)])
    Amount =DecimalField('Amount: ', validators=[validators.DataRequired(), validators.NumberRange(min=0)])

    @app.route("/", methods=['GET', 'POST'])
    def paymentform():
        form = PaymentForm(request.form)

        print(form.errors)
        if request.method == 'POST':
            # name=request.form['name']
            # password=request.form['password']
            # email=request.form['email']
            # print (name, " ", email, " ", password)

            CreditCardNumber=request.form['CreditCardNumber']
            CardHolder=request.form['CardHolder']
            ExpirationDate=request.form['ExpirationDate']
            SecurityCode=request.form['SecurityCode']
            Amount=request.form['Amount']
            print(CreditCardNumber," ",CardHolder," ",ExpirationDate," ",SecurityCode," ",Amount)

        if form.validate():
        # Save the comment here.
            flash('Thanks for registration ' + CardHolder)
        else:
            flash('Error: Enter required fields.')

        return render_template('paymentform.html', form=form)

    # @app.route("/success", methods=['POST'])
    # def processpayment():


if __name__ == '__main__':
     app.run(debug=True)
