import logging
import os

logger = logging.getLogger(__name__)


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation = ',.!?:;'
    page = text[start:start + size]
    actual_size = size

    if page[-1] in punctuation and text[size] not in punctuation:
        actual_size = len(page)

    if page[-1] in punctuation and text[size] in punctuation:
        for i, x in enumerate(page[:-1][::-1]):
            if x not in punctuation:
                page = page[:size - (i + 1)]
                actual_size = len(page)
                break

    for i, x in enumerate(page[::-1]):
        if x in punctuation:
            page = page[:actual_size - i]
            actual_size = len(page)
            break
    return page, actual_size



def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()

    size = 1050
    start = 0
    book = {}
    num_page = 1
    while start < len(text):
        page, actual_size = _get_part_text(text, start, size)
        book[num_page] = page.lstrip()
        num_page += 1
        start += actual_size

    return book
