import json

import services.common.tools

def search(args):
    data = services.common.tools.do_request(
        'at_sRNA', 'json.php', list='linked-sites')

    services.common.tools.send(data['linked-sites'])

def list(args):
    raise Exception('not implemented yet')
