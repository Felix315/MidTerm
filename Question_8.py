# Write a function that checks if the passed parameter is a valid URL or not.
# Please also explain your reasoning. Use only the concepts that we learned in class
def is_valid_url(url):
    """
    Checks if the given parameter is a valid URL based on basic rules.

    :param url: The input string to check.
    :return: True if it's a valid URL, False otherwise.
    """
    # Check if it starts with "http://", "https://", or "www."
    if not (url.startswith("http://") or url.startswith("https://") or url.startswith("www.")):
        return False

    # Check if it contains at least one dot "." (domain part)
    if "." not in url:
        return False

    # Check if it contains spaces (invalid in URLs)
    if " " in url:
        return False

    # If all conditions are met, it is a valid URL
    return True

print(is_valid_url("https://google.com"))
print(is_valid_url("https:// site.com"))