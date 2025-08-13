import sys
import asyncio
from crawl import crawl_site_async


async def main():
    args = sys.argv
    if len(args) < 2:
        print("no website provided")
        sys.exit(1)
    if len(args) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = args[1]

    print(f"Starting async crawl of: {base_url}")

    pages = await crawl_site_async(base_url)

    print(pages)

    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
