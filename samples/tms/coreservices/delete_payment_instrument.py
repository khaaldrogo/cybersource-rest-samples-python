from cybersource_rest_client_python import *



def remove_payment_instruments():
    try:
        payment_instrument_obj = PaymentInstrumentApi()
        payment_instrument_obj.paymentinstruments_token_id_delete("93B32398-AD51-4CC2-A682-EA3E93614EB1", "72EC3E658278F10FE05340588D0A86AB")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    remove_payment_instruments()
