import json

import services.common.tools

def search(args):
    chrnum = args['chrnum']
    start = args['start']
    # default strand: w
    strand = args.get('strand', 'w')

    data = services.common.tools.do_request(
        'at_pare', 'PAinfo.php', list='phasing_window',
        chrnum=chrnum, win_beg=start, strand=strand)

    services.common.tools.send(data['phasing_window'])


def list(args):
    raise Exception('not implemented yet')
