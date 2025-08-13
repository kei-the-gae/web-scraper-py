import sys
from crawl import crawl_page


def main():
    args = sys.argv
    if len(args) < 2:
        print("no website provided")
        sys.exit(1)
    if len(args) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = args[1]

    print(f"starting crawl of: {base_url}...")

    try:
        pages = crawl_page(base_url)
    except Exception as err:
        print(f"Error fetching HTML from {base_url}: {str(err)}")
        sys.exit(1)

    print(pages)

    sys.exit(0)


if __name__ == "__main__":
    main()
