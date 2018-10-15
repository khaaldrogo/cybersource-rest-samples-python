from cybersource_rest_client_python import *

def retrieve_a_capture():
    try:
        # Calling Report Subscription
        credit_obj = CreditApi()
        credit_obj.get_credit("5332036920866055004101")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    retrieve_a_capture()

