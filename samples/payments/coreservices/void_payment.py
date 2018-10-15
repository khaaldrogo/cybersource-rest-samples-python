from cybersource_rest_client_python import *
import json


def void_a_payment():
    try:
        id = "5390887513376089703002"
        request = VoidPaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference.code = "test_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        void_obj = VoidApi()
        void_obj.void_payment(message_body, id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_payment()
