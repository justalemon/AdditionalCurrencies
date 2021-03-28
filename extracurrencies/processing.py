import json
import sys

from .sii import from_dict


def process_files(sources, output, stype, sname, extra={}):
    """
    Processes the contents of the file(s).
    """
    # Make a dict and load the source content
    content = {}
    for source in sources:
        with open(source) as file:
            content.update(json.load(file))
    content.update(extra)
    # Now, save the SII content
    sii_str = from_dict(content, stype, sname)
    with open("build/" + sys.argv[1] + output, "w", encoding="utf-8") as file:
        file.write(sii_str)
