from yt_dlp.cookies import extract_cookies_from_browser, SUPPORTED_BROWSERS

HEADER='# Netscape HTTP Cookie File'

def fmt_bool(val: bool) -> str:
    return 'TRUE' if val else 'FALSE'

def fmt_str_or_none(val: str) -> str:
    return val if val is not None else ''

def format_cookie(cookie) -> str:
    name, value = cookie.name, cookie.value

    if value is None:
        name, value = '', name

    return f'{cookie.domain}\t{fmt_bool(cookie.domain.startswith("."))}\t{cookie.path}\t{fmt_bool(cookie.secure)}\t{fmt_str_or_none(cookie.expires)}\t{name}\t{value}'

def main() -> None:
    which_browser = input(f"Which browser do you have? ({', '.join(SUPPORTED_BROWSERS)}) ").lower()

    if which_browser not in SUPPORTED_BROWSERS:
        raise Exception("Your browser is not supported!")

    cookies = extract_cookies_from_browser(which_browser).get_cookies_for_url('https://www.youtube.com')

    with open('cookies.txt', 'w') as f:
        f.write(HEADER + '\n')
        for cookie in cookies:
            f.write(format_cookie(cookie) + '\n')

if __name__ == '__main__':
    main()