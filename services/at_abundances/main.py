import json

import services.common.tools


def search(args):
    # 'gene' parameter is guarantee to be there because we requested
    # validation by Adama and we declared it to be mandatory
    gene = args['gene']
    # 'model' parameter was declared optional
    # Assume value '1' if not given.
    model = args.get('model', '1')

    data = services.common.tools.do_request(
        'at_sRNA', 'abundances.php', featureName=gene, model=model)
    services.common.tools.send(data['abundance_data'])


def list(args):
    raise Exception('not implemented yet')
