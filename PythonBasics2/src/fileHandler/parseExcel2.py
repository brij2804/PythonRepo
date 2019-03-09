import logging
from datetime import datetime
from src.logger.decorator import log_file

def get_timestamp():
    timeformatted = str(datetime.utcnow())
    semiformatted = timeformatted.replace("-", "_")
    almostformatted = semiformatted.replace(":", "_")
    formatted = almostformatted.replace(".", "_")
    withspacegoaway = formatted.replace(" ", "_")
    formattedstripped = withspacegoaway.strip()
    return formattedstripped


def mainfunc(logger,dummyname):
    logger.debug(" debug message from mainfunc"+dummyname)
    logger.info(" info message from mainfunc"+dummyname)
    logger.warning("warning message from mainfunc"+dummyname)
    logger.error(" error message from mainfunc"+dummyname)
    logger.critical("critical message from mainfunc"+dummyname)
    function1(logger,dummyname)


def function1(logger,dummyname):
    logger.debug(" debug message from function1"+dummyname)
    logger.info(" info message from function1"+dummyname)
    logger.warning("warning message from function1"+dummyname)
    logger.error(" error message from function1"+dummyname)
    logger.critical("critical message from function1"+dummyname)
    func1_1(logger,dummyname)
    func1_2(logger,dummyname)
    func1_3(logger,dummyname)

def func1_1(logger,dummyname):
    logger.debug(" debug message from func1_1"+dummyname)
    logger.info(" info message from func1_1"+dummyname)
    logger.warning("warning message from func1_1"+dummyname)
    logger.error(" error message from func1_1"+dummyname)
    logger.critical("critical message from func1_1"+dummyname)

def func1_2(logger,dummyname):
    logger.debug(" debug message from func1_2"+dummyname)
    logger.info(" info message from func1_2"+dummyname)
    logger.warning("warning message from func1_2"+dummyname)
    logger.error(" error message from func1_2"+dummyname)
    logger.critical("critical message from func1_2"+dummyname)

def func1_3(logger,dummyname):
    logger.debug(" debug message from func1_3"+dummyname)
    logger.info(" info message from func1_3"+dummyname)
    logger.warning("warning message from func1_3"+dummyname)
    logger.error(" error message from func1_3"+dummyname)
    logger.critical("critical message from func1_3"+dummyname)

def main():
    i = 1
    while i < 7:
        timestamp = get_timestamp()
        filename = "../logs/" + timestamp + ".log"
        print(filename)
        i += 1
        logger = log_file(timestamp, filename)
        mainfunc(logger,filename)
        #handler = logging.FileHandler(filename)
        #logger.removeHandler(handler)


if __name__ == '__main__':
    main()