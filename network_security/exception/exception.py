import sys
from network_security.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,err_msg,err_details:sys):
        self.err_msg = err_msg
        _,_,exc_tb = err_details.exc_info()

        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in python script name [{0}], line no. [{1}], error message [{2}]".format(self.file_name,self.line_no,self.err_msg)
    
# if __name__ == "__main__":
#     try:
#         logger.logging.info("Enter the try block")
#         a=1/0
#         print("This will not be printed", a)
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)
