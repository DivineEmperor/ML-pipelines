import sys

def error_message_detail(error,error_detail:sys):
    _,_,tb = error_detail.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    line_number = tb.tb_lineno
    error = str(error)
    error_message = f"Error: {error} in {file_name} at line {line_number} "

    return error_message


class CustomException(Exception):
    def __init__(self, message,error_detail:sys):
        self.message = message
        super().__init__(self.message)
        self.error_detail = error_message_detail(self.message,error_detail)

    def __str__(self):
        return self.error_detail

    