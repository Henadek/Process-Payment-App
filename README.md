# Process-Payment-App

### This is a Flask web app that makes payment with 3 different Payment Gateways:
  - Braintree's API (Allows PayPal and Other Credit/Debit Cards)
  - Stripe API
  - Square API
  
  Each of these gateways are called based on the amount of payment in GBP to be made.
  
  #### Braintree's API is called for amounts in the range of 21 - 500 pounds
  #### Stripe API is called for amounts in the range of 1 - 20 pounds
  #### Square API is called for amounts greater than 500 pounds
      Square Payment Gateway is still under construction
  
  
  For testing the payment, you can use any of the following Test Cards:
  - 5555555555554444 (for Mastercard)
  - 4111111111111111 (for Visa)
  - 371449635398431 (for American Express)
  
  You can choose any 3 digit value for the CVV and any date in the future for the Expiry Date.


### Instructions to install the app:
- Setup a python virtual environment
- Activate the venv
- Install the dependencies from requirements.txt file with pip like so;
  - python -m pip install requirements.txt
- Run the server with python app.py
