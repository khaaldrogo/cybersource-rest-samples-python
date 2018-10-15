from cybersource_rest_client_python import *
import json

def refund_a_capture():
    try:
        id="5341592743826535303527"
        request = RefundCaptureRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "Testing-VDP-Payments-Refund"
        request.client_reference_information = client_reference.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "102.21"
        amount_details.currency = "USD"
    
        order_information.amount_details = amount_details.__dict__
    
        request.order_information = order_information.__dict__
    
        message_body = json.dumps(request.__dict__)
    
        refund_api=RefundApi()
        refund_api.refund_capture(message_body, id)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    refund_a_capture()
