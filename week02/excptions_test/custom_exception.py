class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


userinput = input("Please a number: ")

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as err:
    print(err)
finally:
    del userinput
