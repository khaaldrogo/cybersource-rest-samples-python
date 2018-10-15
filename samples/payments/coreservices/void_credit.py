from cybersource_rest_client_python import *
import json


def void_a_credit():
    try:
        id = "5390885491926778303003"
        request = VoidCreditRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "test_void"
        request.client_reference_information = client_reference.__dict__
        message_body = json.dumps(request.__dict__)
        void_obj = VoidApi()
        void_obj.void_credit(message_body, id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    void_a_credit()
