def FiboPrint(indent=0):
#     dataout = open('dataout.txt', 'w')

    method = raw_input('What method should we choose: \'count\' or \'value\'? ')
    maxCount = int(raw_input('What value do you want to enter? Please enter an integer. '))
    
    if maxCount < 0:
        print 'Try entering a positive integer next time.'
        return

    count = 0
    val1 = 0
    val2 = 1

    if method.lower() == 'count':
#         dataout.write('The first ' + str(maxCount) + ' numbers in the Fibonacci Sequence:\r')
        print 'The first ' + str(maxCount) + ' numbers in the Fibonacci Sequence:'
        while count < maxCount:
#             dataout.write(str(val1) + '\r')
            for i in range(indent):
                print ' ',
            print val1
            val1, val2 = val1 + val2, val1
            count += 1

    elif method.lower() == 'value':
#         dataout.write('The numbers in the Fibonacci Sequence less than or equal to ' + str(maxCount) + ':\r')
        print 'The numbers in the Fibonacci Sequence less than or equal to ' + str(maxCount)
        while val1 <= maxCount:
#             dataout.write(str(val1) + '\r')
            for i in range(indent):
                print '',
            print '', val1
            val1, val2 = val1 + val2, val1
    else:
        print 'It seems you entered something wrong, try again and check your spelling.'

# Choose 'count' or 'value' for the second argument and it will act differently. 
FiboPrint()
