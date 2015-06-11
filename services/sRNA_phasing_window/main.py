import json

import services.common.tools

def search(args):
    chromosome = args['chromosome']
    start = args['start']
    strand = args['strand']
    phase_len = args.get('phase_len', 21)

    data = services.common.tools.do_request(
        'at_sRNA', 'PAinfo.php', list='phasing_window',
        chrnum=chromosome, win_beg=start, strand=strand, phase_len=phase_len)

    services.common.tools.send(data['phasing_window'])

def list(args):
    raise Exception('not implemented yet')
