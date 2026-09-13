sorting_hub_longitude = ('''
79.08503025
77.39075707
77.1907167
77.10773924
75.27976129
72.24363535
86.83710711
85.99653835
77.59370913
78.13714551
79.38580108
82.32751183
84.02596695
83.35903182
91.38242124
75.25090403
''')
sorting_hub_longitude = sorting_hub_longitude.strip().split('\n')
ev_sorting_hub_longitude = [float(x) for x in sorting_hub_longitude]
