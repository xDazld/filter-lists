import pathlib

import pandas


def main():
    redirect_list = pandas.read_json(
        "https://raw.githubusercontent.com/KevinPayravi/indie-wiki-buddy/refs"
        "/heads/main/data/sitesEN.json").convert_dtypes()
    # Build rules using a list comprehension instead of nested loops
    rules = [f"{origin['origin_base_url']}^$dnsrewrite={row['destination_base_url']}\n" for _, row
        in redirect_list.iterrows() for origin in row["origins"]]
    output_dir = pathlib.Path("output")
    if not output_dir.exists():
        output_dir.mkdir()
    with open("output/indiewiki.txt", "w") as f:
        f.writelines(rules)


if __name__ == "__main__":
    main()
