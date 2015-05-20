import json

import services.common.tools


def search(args):
    print json.dumps({'x': services.common.tools.foo()})

