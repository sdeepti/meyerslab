import json
import urlparse

import requests


MEYERS_BASE_URL = 'https://mpss.udel.edu/web/php/pages/'


def do_request(site, endpoint, generic=False, **kwargs):
    """Perform a request to SITE and return JSON."""

    url = urlparse.urljoin(MEYERS_BASE_URL, endpoint)
    kwargs['SITE'] = site
    kwargs['format'] = 'json'
    response = requests.get(url, verify=False, params=kwargs)

    # Raise exception and abort if requests is not successful
    response.raise_for_status()

    data = None
    try:
        # Try to convert result to JSON
        # abort if not possible
        data = response.json()
    except ValueError:
        raise Exception('not a JSON object: {}'.format(response.text))

    if generic:
        return response, data

    return data


def sendJBrowse(data):
    """Display `data` in the format required by JBrowse.

    """
    content = { 'features' : [] }
    for elt in data:
        e = {
                'start' : elt['position'],
                'end' : elt['position'] + elt['length'],
                'score' : 0
            }
        for entry in elt['abundance_table']:
            accession, abundance = entry.items()[0]
            e['score'] += abundance

        if elt['strand'] == 'c':
            e['score'] = -abs(e['score'])

        content['features'].append(e)

    return json.dumps(content)


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
