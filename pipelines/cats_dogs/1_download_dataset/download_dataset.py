import argparse
import logging
import os
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


def download_dataset(
    logger, directory="content", dataset_url="http://iguazio-sample-data.s3.amazonaws.com/catsndogs.zip"
):
    """Download and extract dataset"""

    os.makedirs(directory, exist_ok=True)

    logger.info("Downloading dataset")

    http = urlopen(dataset_url)
    dataset = ZipFile(BytesIO(http.read()))

    logger.info("Extracting dataset")

    dataset.extractall(directory)
    dataset.close()

    logger.info(f"extracted to {directory}")


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument("--data_url", type=str, help="Input data url")

    argument_parser.add_argument("--data_directory", type=str, help="Input data directory")

    argument_parser.add_argument("--logger", type=str, help="Input logger")

    args = argument_parser.parse_args()

    dataset_url = args.data_url
    data_directory = args.data_directory
    logger = args.logger

    ## Testing Logging System ##
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
    log = logging.getLogger("test")
    ############################

    download_dataset(log, data_directory, dataset_url)
