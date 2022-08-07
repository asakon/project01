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


def calculate_sum(input_data: np.array) -> np.ndarray:
    """行列の全要素の合計を求める"""
    result = np.sum(input_data)
    time.sleep(3)
    return result


def save_data(out_file: str, data: int) -> None:
    """データをファイルに保存する"""
    with open(out_file, "w") as f:
        f.write(str(data) + "\n")
    logger.info("saved result to %s", out_file)

def process(args) -> None:
    logger.info("calculate sum start")
    input_data = load_data(args.in_file)
    result = calculate_sum(input_data)
    logger.debug("sum result: %s", result)
    save_data(args.out_file, result)
    logger.info("calculate sum finish")


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




