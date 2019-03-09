import logging
from datetime import datetime
from src.logger.decorator import log_file



def calling_func1():
    filename = "../logs/newfile1.log"
    logger = log_file("first_logger",filename)
    # Test messages
    logger.debug(" debug message from func1")
    logger.info(" info message from func1")
    logger.warning("warning message from func1")
    logger.error(" error message from func1")
    logger.critical("critical message from func1")

def calling_func2():
    filename = "../logs/newfile2.log"
    logger= log_file("second_logger",filename)
    # Test messages
    logger.debug(" debug message from func2")
    logger.info(" info message from func2")
    logger.warning("warning message from func2")
    logger.error(" error message from func2")
    logger.critical("critical message from func2")

def main():
    calling_func1()
    calling_func2()

if __name__ == '__main__':
    main()