import braintree
import stripe


class Payment:
	"""docstring for ProcessPayment"""
	def __init__(self, amount = 0):
		self.amount = amount

	def ProcessPayment(self, CreditCardNumber = '', CardHolder = '', ExpirationDate = '', SecurityCode = '', Amount = ''):
		'''CreditCardNumber (mandatory, string, it should be a valid credit card number)
		- CardHolder: (mandatory, string)
		- ExpirationDate (mandatory, DateTime, it cannot be in the past)
		- SecurityCode (optional, string, 3 digits)
		- Amount (mandatoy decimal, positive amount)'''
		CreditCardNumber = ''
		CardHolder = ''
		ExpirationDate = ''
		SecurityCode = ''
		self.amount = Amount

		if self.Amount in range(21,501):
			try:
				ExpensivePaymentGateway(Amount)
			except:
				CheapPaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount)
		elif self.Amount > 500:
			for trial in range(3):
				PremiumPaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount)
				if PremiumPaymentGateway() == 200: break


	def __str__(self):
		return "Hello from Payment"


# implement these APIs
 # - PremiumPaymentGateway
 # - ExpensivePaymentGateway
 # - CheapPaymentGateway

def PremiumPaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount):
	PremiumPaymentGateway.status = ''
	# implement Square Premium Api here



	if PremiumPaymentGateway.status == 200:
		return '200 OK'
	elif PremiumPaymentGateway.status == 400:
		return '400 bad request'
	else:
		return '500 internal server error'


def ExpensivePaymentGateway():
	# CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount
	ExpensivePaymentGateway.status = ''
	# implement PayPal Api from BrainTree

	# create a gateway instance
	ExpensivePaymentGateway.gateway = braintree.BraintreeGateway(
	    braintree.Configuration(
	        braintree.Environment.Sandbox,
	        merchant_id="nr9d8nwt7qhr8qnt",
	        public_key="pzpcxntbt8dy3ctt",
	        private_key="20ea55f4b4df01fddc1b70f937898124"
	    )
	)
	# generates client_token(authorization) and pass to your front-end
	ExpensivePaymentGateway.client_token = ExpensivePaymentGateway.gateway.client_token.generate()


	if ExpensivePaymentGateway.status == 200:
		return '200 OK'
	elif ExpensivePaymentGateway.status == 400:
		return '400 bad request'
	else:
		return '500 internal server error'


def CheapPaymentGateway():
	# implement Stripe Api
	stripe.api_key = 'sk_test_51ICX9HIJShQdB54vu4C3PnBO6GPbXi5Nq55PjVJb08FDiVdXXLL8kFfR7cK3NPROJSfKQDWtVoTHAmUgA6PvKoSy00fiSCXYW5'


# test = Payment()
# print(test)
