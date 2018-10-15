from cybersource_rest_client_python import *
import json


def capture_a_payment():
    try:
        id = "5390907670456293003006"
        request =CapturePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_3"

        request.client_reference_information = client_reference.__dict__

        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "102.21"
        amount_details.currency = "USD"
        order_information = V2paymentsOrderInformation()
        order_information.amount_details = amount_details.__dict__
        request.order_information = order_information.__dict__

        message_body = (json.dumps(request.__dict__))

        capture_obj = CaptureApi()
        capture_obj.capture_payment(message_body, id)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    capture_a_payment()
