import pathlib
import subprocess
import tempfile
import urllib.parse

import pandas


def main():
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(
            ["git", "clone", "--depth", "1", "https://github.com/citizenlab/test-lists.git",
             tmpdir], check=True)
        lists = pandas.concat(
            pandas.read_csv(file) for file in pathlib.Path(tmpdir, "lists").iterdir() if
            "LEGEND" not in file.stem and not file.is_dir())
        output_dir = pathlib.Path("output")
        if not output_dir.exists():
            output_dir.mkdir()
        with open("output/citizenlablist.txt", "w") as output:
            output.writelines(lists["url"].apply(lambda
                                                     url: f"{urllib.parse.urlparse(url).hostname}\n").drop_duplicates())


if __name__ == "__main__":
    main()
