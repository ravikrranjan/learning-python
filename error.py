
number = input('Type a number: ')
try:
    number = float(number)
    print('The number is : ', number)
except:
    print('Invalid number')

for i in range(10):
    print('Hello world')


try:
    inp = input()
    print('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print('Caught KeyboardInterrupt')
else:
    print('No exception occurred')

print('--end --')
