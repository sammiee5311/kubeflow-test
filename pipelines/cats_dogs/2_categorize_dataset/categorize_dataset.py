import argparse
import json
import logging
import os

import pandas as pd
from tensorflow.python.lib.io import file_io


def categorize_dataset(logger, source_dir, df_filename="file_categories_df.csv", filename="/categories_data.json"):

    os.makedirs(source_dir, exist_ok=True)

    logger.info("Reading image dataset.")
    filenames = [file for file in os.listdir(source_dir) if file.endswith(".jpg")]
    categories = []

    for filename in filenames:
        category = filename.split(".")[0]
        categories.append(category)

    logger.info("Creating a dataframe file.")
    df = pd.DataFrame({"filename": filenames, "category": categories})
    df["category"] = df["category"].astype("str")

    categories = df.category.unique()
    categories = {i: category for i, category in enumerate(categories)}

    logger.info("Converting and saving dataframe to a json file")

    with file_io.FileIO(filename, "w") as f:
        json.dump(categories, f)

    logger.info(categories)


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument("--data_directory", type=str, help="Input data directory")

    argument_parser.add_argument("--logger", type=str, help="Input logger")

    args = argument_parser.parse_args()

    data_directory = args.data_directory
    logger = args.logger

    ## Testing Logging System ##
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO)
    log = logging.getLogger("test")
    ############################

    categorize_dataset(log, data_directory)
