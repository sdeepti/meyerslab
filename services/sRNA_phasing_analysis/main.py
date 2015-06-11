import json

import services.common.tools

def search(args):
    chrnum = args['chrnum']
    start = args['start']
    length = args['length']
    strand = args['strand']
    
    data = services.common.tools.do_request(
        'at_sRNA', 'PAinfo.php', list='phasing_analysis',
        chrnum=chrnum, win_beg=start, strand=strand, length=length)
    services.common.tools.sendList(data['phasing_analysis'])


def list(args):
    raise Exception('not implemented yet')
