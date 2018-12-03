while artists:
    try:
        for i, artist in enumerate(artist_list[count]['artists']):
            for j in artist_list[count]['artists']['items']:
                if artist_list[count]['artists']['items']:
                    print(artist_list[count]['artists']['items'][counter]['name'], 
                  artist_list[count]['artists']['items'][counter]['popularity'])                            
                    counter +=1
                else:
                    break
                    counter = 0
                    count = 0
            if artist_list[count]['artists']:
                count +=1
                counter = 0
                next
            else:
                artist_list[count]['artists'] = None
                count +=1
                break
            break
    except IndexError:
        print('reached the end') #recursion of print statement notifying the end
        break #thus break the while loop.