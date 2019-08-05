import requests

from app.common import reg_find_one


def convert_datetime(text):
    item = reg_find_one('(.*?)T(.*?)Z', text, [])
    return ' '.join(item)


def get_latest_release(user, repo, **kwargs):
    url = 'https://api.github.com/repos/%s/%s/releases/latest' % (user, repo)

    resp = requests.get(url, **kwargs)
    resp_data = resp.json()  # type: dict

    release = {
        'html_url': resp_data['html_url'],
        'created_at': convert_datetime(resp_data['published_at']),
        'published_at': convert_datetime(resp_data['published_at']),
        'tag_name': resp_data['tag_name'],
        'name': resp_data['name'],
        'body': resp_data['body'],
        'assets': [],
    }

    for asset in resp_data['assets']:
        release['assets'].append({
            'name': asset['name'],
            'size': asset['size'],
            'created_at': convert_datetime(asset['created_at']),
            'updated_at': convert_datetime(asset['updated_at']),
            'browser_download_url': asset['browser_download_url'],
        })

    return release
