from cybersource_rest_client_python import *

def retrieve_a_capture():
    try:
        # Calling Report Subscription
        capture_obj = CaptureApi()
        capture_obj.get_capture("5289697403596987704107")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    retrieve_a_capture()


