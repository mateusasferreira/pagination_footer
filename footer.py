def create_pagination_footer(
    current_page, total_pages, boundaries, around
):
    if current_page > total_pages:
        raise ValueError("current_page must not exceed total_pages")
    
    pages = []

    for new_page in range(1, min(boundaries, total_pages) + 1):
        pages.append(str(new_page))

    left_boundary_length = boundaries + 1
    
    if left_boundary_length < current_page - around:
        pages.append('...')

    around_start = max(left_boundary_length, current_page - around)
    around_end = min(total_pages - boundaries, current_page + around)

    for new_page in range(around_start, around_end + 1):
        pages.append(str(new_page))

    if total_pages - boundaries > max(current_page + around, left_boundary_length):
        pages.append('...')

    right_boundary_length = total_pages + 1
    right_boundary_start = max(
        around_end + 1, total_pages - boundaries + 1, left_boundary_length
    )
    
    if right_boundary_start > total_pages and total_pages > current_page:
        right_boundary_start = total_pages

    if right_boundary_start and right_boundary_length > around_end + 1:
        for new_page in range(right_boundary_start, right_boundary_length):
            pages.append(str(new_page))

    result = " ".join(pages)

    print(result)

    return result 
