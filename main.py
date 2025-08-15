import sys
import asyncio
from crawl import crawl_site_async
from report import print_report


async def main():
    args = sys.argv
    if len(args) < 4:
        print("usage python main.py <base_url> <max_concurrency> <max_pages>")
        sys.exit(1)
    if len(args) > 4:
        print("too many arguments provided")
        sys.exit(1)

    base_url = args[1]

    if not args[2].isdigit():
        print("max_concurrency must be an integer")
        sys.exit(1)
    if not args[3].isdigit():
        print("max_pages must be an integer")
        sys.exit(1)

    max_concurrency = int(args[2])
    max_pages = int(args[3])

    print(f"Starting async crawl of: {base_url}")

    pages = await crawl_site_async(base_url, max_concurrency, max_pages)

    print_report(pages, base_url)

    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
