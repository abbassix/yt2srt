def min_to_hour(minutes):
    minutes = int(minutes)  # we are reading from YouTube's text file
    hour = minutes // 60  # while YouTube uses just minutes, srt uses both hourse and minutes
    minute = minutes % 60
    return {'hour': str(hour), 'minute': str(minute)}  # we want them back in srt text file

def convert_to_srt(youtube_format):
    import re
    
    input_file = open(youtube_format, "r")  # read the YouTube's subtitle file
    raw = re.findall(r'(\d{2,3}):(\d{2})\n([^\n]+)', input_file.read())  # find the minutes, seconds and the content of the subtitle
    srt = ''
    for i, line in enumerate(raw):
        if i < len(raw) - 1:  # for the last line YouTube does not give any end time stamp, so there is no next line
            srt += str(i+1) + '\n'  # the index number of srt subtitle contents
            srt += min_to_hour(line[0])['hour'] + ':' + min_to_hour(line[0])['minute'] + ':' + str(line[1]) + ',000'  # starting time stamp
            srt += ' --> '
            srt += min_to_hour(raw[i+1][0])['hour'] + ':' + min_to_hour(raw[i+1][0])['minute'] + ':' + str(raw[i+1][1]) + ',000'  # ending time stamp
            srt += '\n' + str(line[2]) + '\n\n'  # the content of the subtitle
        else:
            None
            # last line of the YouTube's subtitle
    # write the transformed subtitle
    output_file = open(youtube_format[:-4] + '.srt', "w")  # remove the last four characters of the input file's name (i.e. '.txt') and add '.srt'
    output_file.write(srt)
    output_file.close()

    # what if two lines appear at the same time?
    # YouTube puts them at different lines but with the same time stamps.
    # but in srt we should put them under the same time stamps.