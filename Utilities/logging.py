import logging

class LogGen:

    @staticmethod
    def loggenerate():
        logger = logging.getLogger("names")
        logger.setLevel(logging.DEBUG)
        filehandle = logging.FileHandler("C:\\Users\\ASUS\\PycharmProjects\\Ecommerce\\Logs\\logs.log")
        format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filehandle.setFormatter(format)
        logger.addHandler(filehandle)

        return logger






# import logging
#
# class LogGen:
#
#     @staticmethod
#     def loggenerate():
#         logger = logging.getLogger("my_logger")
#         logger.setLevel(logging.DEBUG)
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#
#         file_handler = logging.FileHandler(r'C:\Users\ASUS\PycharmProjects\pythonProject3\Utilities\logs.log')
#         file_handler.setLevel(logging.INFO)  # Set the level of the file handler
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)
#
#         # Log a message to test the logger
#         # logger.info("info111111")
#
#         # Verify the handlers of the logger
#         # print(logger.handlers)
#
#         return logger