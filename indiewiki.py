import pathlib

import pandas


def main():
    redirect_data = pandas.read_json(
        "https://raw.githubusercontent.com/IndieWikiBuddy/indie-wiki-buddy/refs/heads/main/data/data.json", typ="series")
    if "sites" in redirect_data:
        redirect_list = pandas.DataFrame(redirect_data["sites"]).convert_dtypes()
    else:
        redirect_list = pandas.DataFrame(redirect_data.to_list()).convert_dtypes()
    rules = [
        f"{origin['origin_base_url']}^$dnsrewrite={row['destination_base_url'].partition('/')[0]}\n"
        for _, row
        in redirect_list.iterrows() for origin in row["origins"]]
    output_dir = pathlib.Path("output")
    if not output_dir.exists():
        output_dir.mkdir()
    with open("output/indiewiki.txt", "w") as f:
        f.writelines(rules)


if __name__ == "__main__":
    main()
