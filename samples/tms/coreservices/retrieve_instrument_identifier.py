from cybersource_rest_client_python import *

def retrieve_instrument_identifier():
    try:
        instrument_identifier=InstrumentIdentifierApi()
        instrument_identifier.instrumentidentifiers_token_id_get("93B32398-AD51-4CC2-A682-EA3E93614EB1","7020000000000137654")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    retrieve_instrument_identifier()
