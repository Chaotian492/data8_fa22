OK_FORMAT = True
test = {   'name': 'q1_1',
    'points': [0, 0],
    'suites': [   {   'cases': [   {'code': ">>> # Check your column labels and spelling\n>>> p_pop.labels == ('time', 'population_total')\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Times should range from 1900 through 2020\n>>> all(p_pop.sort("time").column("time") == np.arange(1900, 2021))\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
