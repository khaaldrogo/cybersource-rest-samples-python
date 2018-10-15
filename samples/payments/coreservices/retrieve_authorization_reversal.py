from cybersource_rest_client_python import *


def retrieve_an_authorization():
    try:
        reversal_obj = ReversalApi()
        reversal_obj.get_auth_reversal("5335485520876949203528")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    retrieve_an_authorization()
