import argparse
import logging
import time
from unittest import result

import numpy as np
from setup_logging import setup_logger


logger = logging.getLogger(__name__)


def load_data(in_file: str) -> np.array:
    """データをファイルから読み込む"""
    data = np.load(in_file)
    logger.info("loaded data from %s", in_file)
    return data

def calculate_double(
    input_data: np.array,
) -> np.ndarray:
    """行列の各要素を2倍する"""
    result = input_data * 2
    time.sleep(10)
    return result


def save_data(
    out_file: str, data: np.ndarray
) -> None:
    """データをファイルに保存する"""
    np.save(out_file, data)
    logger.info("saved result to %s", out_file)


def process(args) -> None:
    logger.info("calculate double start")
    input_data = load_data(args.in_file)
    result = calculate_double(input_data)
    logger.debug("double result: %s", result)
    save_data(args.out_file, result)
    logger.info("calculate double finish")


if __name__ == "__main__":
    # コマンドラインパラメータの登録
    setup_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--in_file",
        type=str,
        help="入力ファイル",
    )
    parser.add_argument(
        "-o",
        "--out_file",
        type=str,
        help="出力ファイル"
    )
    args = parser.parse_args()
    process(args)