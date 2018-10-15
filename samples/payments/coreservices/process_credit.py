from cybersource_rest_client_python import *
import json


def process_a_credit():
    try:
        id = "5341592743826535303527"
        request = CreateCreditRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC50171_3"
        request.client_reference_information = client_reference.__dict__
    
        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "200"
        amount_details.currency = "usd"
        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "US"
        bill_to.first_name = "Test"
        bill_to.last_name = "test"
        bill_to.address1 = "test"
        bill_to.phone_number = "9999999999"
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.administrative_area = "MI"
        bill_to.email = "test@cybs.com"
        order_information.amount_details = amount_details.__dict__
        order_information.bill_to = bill_to.__dict__
    
        payment_information = V2paymentsPaymentInformation()
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "03"
        card_information.expiration_year = "2031"
        card_information.type = "001"
        card_information.number = "4111111111111111"
        payment_information.card = card_information.__dict__
        request.order_information = order_information.__dict__
        request.payment_information=payment_information.__dict__
        message_body = json.dumps(request.__dict__)
    
        credit_obj=CreditApi()
        credit_obj.create_credit(message_body)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    process_a_credit()
