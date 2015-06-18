import json

import services.common.tools

def search(args):
    rminput = args.get('regulatory_mechanism', 'phasi')

    data = services.common.tools.do_request(
        'at_sRNA', 'loci_list.php', regulatory_mechanism=rminput)

    services.common.tools.send(data['phasiRNAs'])

def list(args):
    raise Exception('not implemented yet')
