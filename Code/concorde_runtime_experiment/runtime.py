import os

CONCORDE_DIR='~/Documents/Concorde/Concorde_build/'
MAX_NODE_SIZE = 1500
STEP = 10

out = open('results.csv', 'w+')

print('node_size,seconds')
out.write('node_size,seconds\n')

for i in range(100, MAX_NODE_SIZE+1, STEP):
	for j in range(10):
		f = os.popen(CONCORDE_DIR + 'TSP/concorde -k ' + str(i))
		lines = f.read().splitlines()

		time = lines[-1].split(' ')[3]

		print(str(i) + ',' + time)
		out.write(str(i) + ',' + time + '\n')

out.close()
