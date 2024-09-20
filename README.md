# Footer Pagination Challenge

This is a challenge for creating a pagination footer represented as a string.

## Usage

```python
>>> from footer import create_pagination_footer
>>> create_pagination_footer()
>>> create_pagination_footer(current_page=4, total_pages=5, boundaries=2, around=2)
1 2 3 4 5
```

# Testing

```shell
python3 test.py
```
