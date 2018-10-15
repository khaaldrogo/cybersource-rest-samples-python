from cybersource_rest_client_python import *


def retrieve_payment_identifier():
    try:
        payment_instruments = PaymentInstrumentApi()
        payment_instruments.paymentinstruments_token_id_get("93B32398-AD51-4CC2-A682-EA3E93614EB1", "7501E647FA683692E05340588D0A131D")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    retrieve_payment_identifier()
