from cybersource_rest_client_python import *

def retrieve_a_refund():
    try:
        refund_obj = RefundApi()
        refund_obj.get_refund("5335504389516958903526")
    except Exception as e:
        print(e)


if __name__ == "__main__":
     retrieve_a_refund()