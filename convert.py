import pathlib
import urllib.parse

import pandas

lists = {file.stem: pandas.read_csv(file) for file in pathlib.Path("test-lists/lists").iterdir() if
         "LEGEND" not in file.stem and not file.is_dir()}

output_dir = pathlib.Path("output")
if not output_dir.exists():
    output_dir.mkdir()

with open("output/citizenlablist.txt", "w") as output:
    for key, item in lists.items():
        output.write(f"#{key}\n")
        output.writelines(item["url"].apply(lambda
                                                url: f"{urllib.parse.urlparse(url).hostname}\n").drop_duplicates())
