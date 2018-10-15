from cybersource_rest_client_python import *
import json

def tokenize_card():
    tokenize_card = TokenizeRequest()
    card_info = Paymentsflexv1tokensCardInfo()
    tokenize_card.key_id = "073mAPQxysmv277FH9HvrKNOeziUcheF"

    card_info.card_expiration_year = "2031"
    card_info.card_number = "5555555555554444"
    card_info.card_type = "002"
    card_info.card_expiration_month = "03"
    tokenize_card.card_info = card_info.__dict__

    message_body = json.dumps(tokenize_card.__dict__)

    tokenize_obj = TokenizationApi()
    tokenize_obj.tokenize(tokenize_request=message_body)




if __name__ == "__main__":
    tokenize_card()
