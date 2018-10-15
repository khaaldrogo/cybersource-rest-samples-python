
from cybersource_rest_client_python import *

def remove_instrument_identifiers():
    try:

        instrument_identifier_obj = InstrumentIdentifierApi()
        instrument_identifier_obj.instrumentidentifiers_token_id_delete("93B32398-AD51-4CC2-A682-EA3E93614EB1", "7020000000000137654")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    remove_instrument_identifiers()
