# -*- coding: utf-8 -*-

import FIDL.decompiler_utils as du


callz = du.find_all_calls_to(f_name='GetProcAddress', ea=here())
for co in callz:
    # The *second* argument of ``GetProcAddress`` is the API name
    api_name = co.args[1].val

    # double check :)
    if not du.is_asg(co.node):
        continue

    lhs = co.node.x
    if du.is_global_var(lhs):
        g_addr = du.value_of_global(lhs)
        new_name = "g_ptr_{}".format(api_name)
        MakeName(g_addr, new_name)
