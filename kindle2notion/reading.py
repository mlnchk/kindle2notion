from pathlib import Path


def read_raw_clippings(clippings_file_path: Path) -> str:
    try:
        with open(clippings_file_path, "r", encoding="utf-8-sig") as raw_clippings_file:
            raw_clippings_text = raw_clippings_file.read()
        raw_clippings_text = raw_clippings_text.replace(u"\ufeff", "")
        # Use UTF-8 instead of ASCII - supports all Unicode characters including Russian
        raw_clippings_text_decoded = raw_clippings_text.encode("utf-8").decode("utf-8")
    except UnicodeEncodeError as e:
        print(e)

    return raw_clippings_text_decoded
