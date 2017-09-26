init_velo = 0
time = int(input('Time = '))
distance = int(input('Distance = '))
speed_limit = 60
x = int(input('Acceleration = '))
v = init_velo + x*time
a = init_velo + 1/2*x*time**2

for i in range(0,time + 1):
    x = init_velo*i + 1/2*x*i**2
    print('Duration' + str(i) + ':' + int(x/10)*'*')

if v > speed_limit:
    print('The person went over the speed limit,' + 'Max speed was' + str(v) + 'm/s')
else :
    print('The person did not go over the speed limit,' + 'Max speed was' + str(v) + 'm/s')

if a >=distance:
    print('The person reached the destination,' + 'Reached' + str(a) +'m')
else:
    print('The person did not reached the destination,' + 'Reached' + str(a) + 'm')
