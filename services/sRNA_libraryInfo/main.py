import json

import services.common.tools

def search(args):
    data = services.common.tools.do_request(
        'at_sRNA', 'library_info.php', list='library_info')

    services.common.tools.send(data['library_info'])

def list(args):
    raise Exception('not implemented yet')
