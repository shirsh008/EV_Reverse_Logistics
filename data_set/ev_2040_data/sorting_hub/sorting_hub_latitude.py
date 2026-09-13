sorting_hub_latitude = ('''
21.17815544
23.47015891
28.48146333
28.79350456
20.02744194
22.75691598
24.85408053
23.69474218
12.95177349
11.69021496
26.09119305
21.58203135
24.97982232
26.65606841
26.37053567
12.8531237
''')
sorting_hub_latitude = sorting_hub_latitude.strip().split('\n')
ev_sorting_hub_latitude = [float(x) for x in sorting_hub_latitude]
