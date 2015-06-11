import json

import services.common.tools

def search(args):
    chromosome = args['chromosome']
    start = args['start']
    strand = args['strand']
    phase_len = args.get('phase_len', 21)

    words = chromosome.split();

    if words[1] == 'M':
       chrnum = 6
    elif words[1] == 'C':
       chrnum = 7
    else:
       chrnum = words[1]
  
    data = services.common.tools.do_request(
        'at_sRNA', 'PAinfo.php', list='phasing_window',
        chrnum=chrnum, win_beg=start, strand=strand, phase_len=phase_len)

    services.common.tools.send(data['phasing_window'])

def list(args):
    raise Exception('not implemented yet')
