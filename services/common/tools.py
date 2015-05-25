import json
import urlparse

import requests


MEYERS_BASE_URL = 'https://mpss.udel.edu/web/php/pages/'


def do_request(site, endpoint, **kwargs):
    """Perform a request to SITE and return JSON."""

    url = urlparse.urljoin(MEYERS_BASE_URL, endpoint)
    kwargs['SITE'] = site
    kwargs['format'] = 'json'
    response = requests.get(url, verify=False, params=kwargs)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    try:
        # Try to convert result to JSON
        # abort if not possible
        return response.json()
    except ValueError:
        raise Exception('not a JSON object: {}'.format(response.text))


def sendList(data):
    """Display `data` in the format required by Adama.

    :type data: list

    """

    for elt in data:
        print json.dumps(elt)
        print '---'


def send(data):
    """Display `data` in the format required by Adama.

    """
    print json.dumps(data)
    print '---'
