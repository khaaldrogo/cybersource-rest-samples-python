from cybersource_rest_client_python import *
import json


def mastercard_securecode():
    try:
        request = CreatePaymentRequest()
        client_reference = V2paymentsClientReferenceInformation()
        client_reference._code = "TC45561-10"
        request.client_reference_information = client_reference.__dict__

        consumer_authentication = V2paymentsConsumerAuthenticationInformation()
        consumer_authentication.cavv = "EHuWW9PiBkWvqE5juRwDzAUFBAk="
        consumer_authentication.ucaf_collection_indicator = "0"
        consumer_authentication.ucaf_authentication_data = "lEmYpm61EduaVZjPG1/HsgkAAQc="
        consumer_authentication.eci_raw = "02"
        request.consumer_authentication_information = consumer_authentication.__dict__

        processing_info = V2paymentsProcessingInformation()
        processing_info.commerce_indicator = "spa"
        request.processing_information = processing_info.__dict__

        order_information = V2paymentsOrderInformation()
        amount_details = V2paymentsOrderInformationAmountDetails()
        amount_details.total_amount = "2016.05"
        amount_details.currency = "USD"
        order_information.amount_details = amount_details.__dict__

        bill_to = V2paymentsOrderInformationBillTo()
        bill_to.country = "SG"
        bill_to.first_name = "RTS"
        bill_to.last_name = "VDP"
        bill_to.phone_number = "999999999"
        bill_to.address2 = "test"
        bill_to.address1 = "201 S. Division St."
        bill_to.postal_code = "48104-2201"
        bill_to.locality = "Ann Arbor"
        bill_to.company = "Visa"
        bill_to.administrative_area = "MI"
        bill_to.email = "test@cybs.com"
        bill_to.district = "MI"
        bill_to.building_number = "123"
        order_information.bill_to = bill_to.__dict__

        payment_information = V2paymentsidrefundsPaymentInformation()
        card_information = V2paymentsPaymentInformationCard()
        card_information.expiration_month = "12"
        card_information.expiration_year = "2031"
        card_information.number = "5641821111166669"
        card_information.security_code = "123"
        card_information.type = "024"
        payment_information.card = card_information.__dict__
        request.payment_information = payment_information.__dict__
        request.order_information = order_information.__dict__

        message_body = json.dumps(request.__dict__)
        payment_obj = PaymentApi()
        payment_obj.create_payment(message_body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    mastercard_securecode()
