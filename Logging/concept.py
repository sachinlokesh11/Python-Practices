from implementation import logger
import implementation


def main():
    logger.info('Started')
    implementation.cal_reverse()
    implementation.update_list()
    logger.info('Finished')


if __name__ == "__main__":
    main()
