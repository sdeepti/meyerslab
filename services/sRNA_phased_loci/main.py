import json

import services.common.tools

def search(args):
    rminput = args.get('regulatory_mechanism', 'phasi')

    data = services.common.tools.do_request(
        'at_sRNA', 'loci_list.php', regulatory_mechanism=rminput)

    for dataRow in data['phasiRNAs']:
        if dataRow['chromosome']  == 6:
            dataRow['chromosome'] = 'chrM'
        elif dataRow['chromosome']  == 7:
            dataRow['chromosome'] = 'chrC'
        else:
            dataRow['chromosome'] = 'chr' + `dataRow['chromosome']`

    services.common.tools.send(data['phasiRNAs'])

def list(args):
    raise Exception('not implemented yet')
