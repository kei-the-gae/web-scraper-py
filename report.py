def print_report(pages, base_url):
    print("=============================")
    print(f"REPORT for {base_url}")
    print("=============================")

    sorted_pages = sort_pages(pages)
    for url, count in sorted_pages:
        print(f"Found {count} internal links to {url}")


def sort_pages(pages):
    # Convert the dictionary to a list of [url, count] pairs
    pages_list = list(pages.items())

    # Sort the list by count (highest first), then by URL (alphabetically)
    pages_list.sort(key=lambda x: (-x[1], x[0]))

    return pages_list
