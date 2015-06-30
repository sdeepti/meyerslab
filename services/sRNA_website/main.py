import json

import services.common.tools

def search(args):
    data = services.common.tools.do_request(
        'at_sRNA', 'json.php', list='website')

    services.common.tools.send(data['website'])

def list(args):
    raise Exception('not implemented yet')

