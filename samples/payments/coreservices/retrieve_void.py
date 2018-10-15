from cybersource_rest_client_python import *

def retrieve_a_void():
    try:
        void_obj = VoidApi()
        void_obj.get_void("5335528892726038303523")
    except Exception as e:
        print(e)


if __name__ == "__main__":
   retrieve_a_void()