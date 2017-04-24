#Author: RyQ
#Date: 2017.04.15

import numpy as np
import scipy as sp

import sys

def setup():
    '''
    Set Default Encoding to utf-8. Escaping from the encoding error of python shell.
    '''
    reload(sys)
    sys.setdefaultencoding('utf-8')

def read_data(filename,delimiter,content_type):
    '''
    Read data from csv file.
    '''
    lines = np.loadtxt(filename,delimiter=delimiter,dtype='str')
    data = lines.astype(content_type)
    return data

filename = 'Hot100.csv'
delimiter = ','
content_type = 'str'
filename1 = 'album.csv'
filename2 = 'artist.csv'
filename3 = 'social.csv'
setup()
data = read_data(filename, delimiter, content_type)
album_data = read_data(filename1, delimiter, content_type)
artist_data = read_data(filename2, delimiter, content_type)
social_data = read_data(filename3, delimiter, content_type)
print len(data[:,0])
label = []
album = []
artist = []
social = []
for i in range((len(data[:,0])/100)-1):
#for i in range(2):
    chart = range(i*100,(i+1)*100)
    chart1 = range((i+1)*100,(i+2)*100)
    chart2 = range((i+1)*50,(i+2)*50)
    chart3 = range((i+1)*200,(i+2)*200)

    data_new = data[chart]
    data_old = data[chart1]
    song_list = data_new[:,1].tolist()

    artist_old = artist_data[chart1]
    artist_list = artist_old[:,1].tolist()

    social_old = social_data[chart2]
    social_list = social_old[:,1].tolist()

    album_old = album_data[chart3]
    album_list = album_old[:,5].tolist()
    
    for row in data_old:
        if row[1] in song_list:
            temp = int(row[0])-int(data_new[song_list.index(row[1])][0])
            if temp>=0:
                label.append(1)
            else: 
                label.append(-1)
        else:
            label.append(-1)

        if row[5] in artist_list:
            temp = int(artist_old[artist_list.index(row[5])][0])
            artist.append(temp)
        else:
            artist.append(120)

        if row[5] in social_list:
            temp = int(social_old[social_list.index(row[5])][0])
            social.append(temp)
        else:
            social.append(120)

        if row[5] in album_list:
            temp = int(album_old[np.min(album_list.index(row[5]))][0])
            album.append(temp)
        else:
            album.append(250)

print len(label)
print len(artist)
print len(social)
print len(album)
np.savetxt('label.csv',label)
np.savetxt('artist_attr.csv',artist)
np.savetxt('social_attr.csv',social)
np.savetxt('album_attr.csv',album)
