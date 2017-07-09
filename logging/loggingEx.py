import logging
import otherMod2

def main():
    logger=logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    fh=logging.FileHandler("new_snake.log")
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)

    logger.info("Program started")
    result=otherMod2.add(3,5)
    logger.info("Done")


if __name__ == '__main__':
    main()