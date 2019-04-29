import sys
import operator


if len(sys.argv) > 2:
    zip = sys.argv[1]
    month = sys.argv[2]

    #redefine arguments
    zip = 191015
    month = 31

    i = 0
    while i <= 99999:
            id = str(i)
            while len(id) < 5:
                id = str('0' + id);

            pre_track = str(zip) + str(month) + id
            
            #calculation of checksumm
            nechet = map(int, pre_track[0::2])
            sum_nechet =  sum(nechet)
            
            chet = map(int, pre_track[1::2])
            sum_chet =  sum(chet)
            
            checksumm = 10 - (((3 * sum_nechet) + sum_chet) % 10)
            if checksumm == 10:
                checksumm = 0;
            
            track = pre_track + str(checksumm)
            
            print track
            #print "\n"
            
            i+=1;
    
    


else: print "Usage: ",sys.argv[0]," <ZIP (6digits)> <Month (2digits)>"


