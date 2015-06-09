import json

import services.common.tools


def fail(message):
    # This is a simple failure message generator for generic ADAMA adapters
    # It will eventually be replaced with a system-wide fail function
    return 'text/plaintext; charset=ISO-8859-1', message


def search(args):
    chrnum = args['chr']
    start = args['start']

    r, data = services.common.tools.do_request(
        'at_sRNA', 'PAinfo.php', generic=True, list='phasing_analysis',
        chrnum=chrnum, win_beg=start)

    if r.ok:
        return r.headers['Content-Type'], \
                services.common.tools.sendJBrowse(data['phasing_analysis'])
    else:
        return fail(r.text)


def list(args):
    raise Exception('not implemented yet')
