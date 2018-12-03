
# coding: utf-8

# In[3]:

def timestamp2sec(timestamp):
    import datetime
    import time
    x = time.strptime(timestamp,'%H:%M:%S')
    output = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
    
    return output
    


# In[4]:

import os
import csv

directory = os.path.join("./twitch_marker_input/")
out_directory = './premiere_marker_output/'

for root,dirs,files in os.walk(directory):
    
    for file in files:
        print file
        
        if file.endswith(".csv"):
            f=open(directory+file, 'r')
            

            with open(out_directory+file[:-4]+'_converted.csv','wb') as outfile:
                #header
                outfile.write('Screenlight Premiere Pro Marker Export 1.0\n')
                outfile.write('Name:,Time:,Duration:,Marker Color:,Comment:\n')                
                

                #  perform calculation
                reader = csv.reader(f)

                for row in reader:

                    timestamp = row[0]
                    commentor = row[1]
                    comment = row[3].decode('utf-8').encode('euc-kr')

                    output_name = commentor
                    outfile.write(output_name)
                    outfile.write(',')

                    #=(MID(C2;1;2)*3600)+(MID(C2;4;2)*60)+MID(C2;7;2)+(MID(C2;10;2)/25)
                    #timestamp to sec
                    output_time=timestamp2sec(timestamp)
                    outfile.write(str(output_time))
                    outfile.write(',')

                    output_duration = '0' #todo : make this vary
                    outfile.write(output_duration)
                    outfile.write(',')
                    output_marker_color = '#718637'
                    outfile.write(output_marker_color)
                    outfile.write(',')
                    output_comment = comment
                    outfile.write(output_comment)

                    
                    outfile.write('\n')
                print 'csv file done'

print 'all done'

f.close()


# In[2]:




# In[ ]:



