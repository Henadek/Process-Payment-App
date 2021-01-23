from datetime import datetime
from api_engine import *
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# YOUR_DOMAIN = 'http://localhost:5000'



# prevent cached responses
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response


@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/getamount", methods=["POST"])
def _getAmount():
    _getAmount.amount = int(request.form['amount'])
    if request.method == "POST":
        if _getAmount.amount in range(21,501):
            return redirect(url_for('expensivePayment'))
        elif _getAmount.amount in range(1,21):
            return redirect(url_for('cheapPayment'))
        elif _getAmount.amount > 500:
            return redirect(url_for('premiumPayment'))
        else:
            return redirect(url_for('landing'))
    return render_template("landing.html")





@app.route("/cheapPayment")
def cheapPayment():
    amount = _getAmount.amount
    return render_template("cheapPayment.html", amount = amount)




@app.route('/stripe-gateway', methods=['POST'])
def stripe():
    CheapPaymentGateway()
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'gbp',
                        'unit_amount': _getAmount.amount*100,
                        'product_data': {
                            'name': 'Card Payment',
                            'images': ['https://www.pngitem.com/pimgs/m/13-130963_payment-method-png-transparent-images-payment-methods-icons.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            # success_url=YOUR_DOMAIN + '/success.html',
            # cancel_url=YOUR_DOMAIN + '/cancel.html',
            success_url=url_for('success'),
            cancel_url=url_for('failed'),


        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403



@app.route("/square-gateway")
def premiumPayment():
    # PremiumPaymentGateway()
    return render_template("under_construction.html")





@app.route("/paypal-gateway")
def expensivePayment():
    ExpensivePaymentGateway()
    client_token = ExpensivePaymentGateway.client_token
    return render_template("expensivePayment.html", client_token = client_token)
   	
# this applies only for the ExpensivePaymentGateway
@app.route("/getnonce", methods=["POST"])
def _create_purchase():
    nonce_from_the_client = request.form["payload_nonce"]
    CreditCardNumber = request.form['credit_card']
    CardHolder = request.form['card_holder']
    ExpirationDate = request.form['exp_date']
    SecurityCode = request.form['cvv']
    device_id = request.form['device_id'][0]
    print(f'This is the data:\n{request.form}')
    result = ExpensivePaymentGateway.gateway.transaction.sale({
"amount": str(_getAmount.amount),
"payment_method_nonce": nonce_from_the_client,
"device_data": device_id,
"options": {
    "submit_for_settlement": True
}
})
    if result.is_success:
        print('Payment is processed: 200 OK')
        return redirect(url_for('success'))
        # print (result.transaction)
    else:
        return redirect(url_for('failed'))

    return redirect(url_for('landing'))






@app.route("/success")
def success():
    amount = _getAmount.amount
    return render_template("payment_success.html", amount = amount)


@app.route("/failed")
def failed():
    return render_template("payment_failed.html")









#run app
if __name__ == "__main__":
    app.run(debug=True)


    	
