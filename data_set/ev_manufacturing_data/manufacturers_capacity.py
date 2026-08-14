manufacturers_capacity = ('''
240 MWh
120000 packs
1000 MWh
20 GWh
12.5 GWh
5 GWh
1500 mwh
10 GWh
20 GWh
500 mwh
5 GWh
288 MWh
400 MWh
50000 packs
1 GWh
155000 packs
100 MWh
200 MWh
1500 MWh
400 MWh
200 MWh
140 MWh
400 MWh
500 MWh
250 MWh
750 MWh
100 MWh
350 MWh
''')
manufacturers_capacity = manufacturers_capacity.strip().split('\n')
ev_manufacturers_capacity = [float(x) for x in manufacturers_capacity]
