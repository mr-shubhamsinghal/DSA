import datetime, os, sys, logging


class log:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        result = self.func(*args, **kwargs)
        func_name = self.func.__name__
        end = datetime.datetime.now()

        message = """
                    Function : {}
                    Execution Time : {}
                    Address : {}
                    Memory : {} Bytes
                    Date : {}
                    """.format(func_name, end-start, self.func.__name__,
                               sys.getsizeof(self.func), start)
        
        cwd = os.getcwd()
        folder = "Logs"
        newPath = os.path.join(cwd, folder)
        try:
            os.mkdir(newPath)
        except:
            logging.basicConfig(filename='{}/log.log'.format(newPath))
            logging.debug(message)
        return result


class Meta(type):
    
    def __call__(cls, *args, **kwargs):
        instance = super(Meta, cls).__call__(*args, **kwargs)
        return instance

    def __init__(cls, name, base, attr):
        super(Meta, cls).__init__(name, base, attr)

class Test(metaclass=Meta):

    @log
    def methodA():
        print("Method A")
        return '1111'

if __name__ == "__main__":
    obj = Test()
    obj.methodA()