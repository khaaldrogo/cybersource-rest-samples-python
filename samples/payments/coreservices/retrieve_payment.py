from cybersource_rest_client_python import *

def retrieve_a_payment():
    try:
        # Calling Report Subscription
        payment_obj = PaymentApi()
        payment_obj.get_payment("5390861131586587803001")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    retrieve_a_payment()