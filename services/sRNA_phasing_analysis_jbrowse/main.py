import re
import json

import services.common.tools


def fail(message):
    # This is a simple failure message generator for generic ADAMA adapters
    # It will eventually be replaced with a system-wide fail function
    return 'text/plaintext; charset=ISO-8859-1', message


def search(args):
    chr = args['chr']
    start = args['start']
    end = args['end']

    chr_pat = re.compile(r'^Chr')
    chrnum = re.sub(chr_pat, '', chr)
    chrnum = 6 if chrnum == 'C' \
            else 7 if chrnum == 'M' \
            else chrnum

    r, data = services.common.tools.do_request(
        'at_sRNA', 'PAinfo.php', generic=True, list='phasing_analysis',
        chrnum=chrnum, win_beg=start)

    if r.ok:
        return r.headers['Content-Type'], \
                services.common.tools.sendJBrowse(data['phasing_analysis'], \
                start=start, end=end)
    else:
        return fail(r.text)


def list():
    return 'application/json', json.dumps(dict())
