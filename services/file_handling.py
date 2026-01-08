import logging
import os

logger = logging.getLogger(__name__)


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    pass
    # return page_text, page_size


def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    book = {}

    return book