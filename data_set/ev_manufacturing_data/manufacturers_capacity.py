manufacturers_capacity = ('''
240
5000
1000
20000
12500
5000
1500
10000
20000
500
5000
288
400
1000
1000
7000
100
200
1500
400
200
140
400
500
250
750
100
350 
''')
manufacturers_capacity = manufacturers_capacity.strip().split('\n')
ev_manufacturers_capacity = [int(x) for x in manufacturers_capacity]
