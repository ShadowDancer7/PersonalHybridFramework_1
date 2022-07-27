import logging

class LogGenerator:
    def generateLog():
        logger = logging.getLogger('test_opencartResourcesMenuDropDown')
        logger.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('.\\Logs\\automation.log')
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    

        return logger


    