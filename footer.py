def create_pagination_footer(
    current_page, total_pages, boundaries, around
):
    if current_page > total_pages:
        raise ValueError("current_page must not exceed total_pages")
    
    pages = ['1']

    for i in range(2, min(boundaries, total_pages) + 1):
        pages.append(str(i))
    
    if boundaries + 1 < current_page - around:
        pages.append('...')

    around_start = max(2, boundaries + 1, current_page - around)
    around_end = min(total_pages - boundaries, current_page + around)

    for i in range(around_start, around_end + 1):
        pages.append(str(i))
    
    if total_pages - boundaries > current_page + around:
        pages.append('...')

    limit_length = total_pages + 1
    start_total_padding = max(around_end + 1, total_pages - boundaries + 1)
    
    if start_total_padding > total_pages and total_pages > current_page:
        start_total_padding = total_pages

    if start_total_padding:
        for i in range(start_total_padding, limit_length):
            pages.append(str(i))

    result = " ".join(pages)

    print(result)

    return result 
