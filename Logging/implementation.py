import logging


logging.basicConfig(filename='Details.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)


def cal_reverse():
    try:
        number = int(input("Enter the Number:"))
        reverse_number = 0
        while number > 0:
            remainder = number % 10
            reverse_number = reverse_number*10 + remainder
            number = int(number/10)
        logger.info(f"Reverse of a Number is {reverse_number}")
        print(f"Reverse of a Number is {reverse_number}")
    except Exception as ex:
        logger.exception(ex.args[0])


def update_list():
    mylist = [2, 5, 7, 10]
    mylist.append(25)
    logger.info("List Updated")


