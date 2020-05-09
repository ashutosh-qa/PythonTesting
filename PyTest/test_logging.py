import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)
    # Here logger object is responsible to log everything
    # __name__ this will generate test case name

    fileHandler = logging.FileHandler('logfile.log')
    # fileHandler has knowledge of the log file

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #fileHandler Object

    logger.setLevel(logging.INFO)  # So logs will print only from Info level
    logger.debug("This is for debug details")
    logger.info("This is for Information statement")
    logger.warning("This is for warning statement")
    logger.error("THis is to highlight major error")
    logger.critical("This is where TCs failing")