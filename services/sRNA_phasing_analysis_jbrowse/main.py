import re
import json

import services.common.tools


def fail(message):
    # This is a simple failure message generator for generic ADAMA adapters
    # It will eventually be replaced with a system-wide fail function
    return 'text/plaintext; charset=ISO-8859-1', message


def search(args):
    q = args['q']
    chrom, start, end, strand = args['chr'], args['start'], \
            args['end'], args['strand']
    scale, basesPerBin, basesPerSpan = args['scale'], \
            args['basesPerBin'], args['basesPerSpan']

    phase_len = args.get('phase_len', 21)

    if start >= end:
        raise Exception('End coordinate must be greater than start')

    chr_pat = re.compile(r'^Chr')
    chrnum = re.sub(chr_pat, '', chrom)
    chrnum = 6 if chrnum == 'C' \
            else 7 if chrnum == 'M' \
            else chrnum

    strand = 'w' if strand == '+' else 'c'

    out = dict()
    if q == 'features':
        r, data = services.common.tools.do_request(
            'at_sRNA', 'PAinfo.php', generic=True, list='phasing_analysis',
            chrnum=chrnum, win_beg=start, strand=strand, phase_len=phase_len)

        if r.ok:
            return r.headers['Content-Type'], \
                    services.common.tools.sendJBrowse(data['phasing_analysis'], \
                    start=start, end=end)
        else:
            return fail(r.text)
    elif q == 'globalStats':
        out = { 'scoreMin': -1000, 'scoreMax': 1000 }

    return 'application/json', json.dumps(out)


def list(args):
    r, data = services.common.tools.do_request(
        'at_sRNA', 'json.php', generic=True, list='chromosome')

    if r.ok:
        return r.headers['Content-Type'], json.dumps(data['chromosome'])
    else:
        return fail(r.text)
