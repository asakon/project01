import argparse
import logging
import time

import numpy as np
from setup_logging import setup_logger


logger = logging.getLogger(__name__)


def make_kuku() -> np.ndarray:
    """巨大な掛け算九九表を作成します"""
    a = np.arange(1, 100)
    result = np.outer(a, a)
    time.sleep(1)
    return result


def save_data(
    out_file: str, data: np.ndarray
) -> None:
    """データをファイルに保存する"""
    np.save(out_file, data)
    logger.info("saved result to %s", out_file)


def process(args) -> None:
    logger.info("make kuku start")
    result = make_kuku()
    logger.debug("kuku result: %s", result)
    save_data(args.out_file, result)
    logger.info("make kuku finish")


if __name__ == "__main__":
    # コマンドラインパラメータの登録
    setup_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--out_file",
        type=str,
        help="出力ファイル",
    )
    args = parser.parse_args()
    process(args)
