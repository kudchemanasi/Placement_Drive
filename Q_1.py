import logging
logging.basicConfig(filename="example.txt", level=logging.DEBUG, filemode='w')

class file:
    def __int__(self, filename):
        logging.info('Creating file instance variable')
        self.file = filename
    def read(self):
        logging.info("executing read method")
        try:
            file = open("example.txt", "rt")
            # read file contents to string
            data = file.read()
            data = data.replace('placement', 'screening')
            file.close()
        except FileNotFoundError as e:
            logging.error("Error occured while opening the file")
            logging.exception(f"Error is {e}")
    def write(self):
        logging.info("executing read method")
        try:
            file = open("example.txt", "wt")
            file.write(data)
            file.close()
        except FileNotFoundError as e:
            logging.error("Something went wrong")





