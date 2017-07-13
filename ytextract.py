from __future__ import unicode_literals 
import youtube_dl 

import json
import subprocess
import os
import re
import sys

OUTPUT_FOLDER = 'videos/'

def load_json(filename):
    with open(filename) as data_file:    
        data = json.load(data_file)
    return data

def download_video(url):
    ydl_opts = {}
    video_title = "misc"
    # get info of video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
        # extracting info
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get("url", None)
        video_id = info_dict.get("id", None)
        video_title = info_dict.get('title', None)
        video_title = video_title.replace(" ", "_")
        video_title = video_title.replace("/", "_")
        # setting next ydl option
        file_path = OUTPUT_FOLDER + video_title + "/main_" + video_id +".mp4"
        ydl_opts = {
            'outtmpl': file_path,
            'format' : 'mp4'
            
        }

    # download video
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
        directory = os.path.dirname(file_path)
        print directory
        if not os.path.exists(directory):
            os.makedirs(directory)
        ydl.download([url])

    return file_path

# filepath: string start: string, length: string
# Example: cut_video(filepath, '00:00:03', '00:00:07', 'cut.mp4')
def cut_video(filepath, start, length, outputname):
    directory = os.path.dirname(filepath)
    directory = re.escape(directory)
    filepath = re.escape(filepath)
    subprocess.check_output('ffmpeg -y -i ' + filepath + ' -ss ' + start + ' -t ' + length + ' -async 1 '+ directory + '/' + outputname, shell=True)

# dictionary of url and clips
def extract_all(data):
    for video in data['data']:
        clips = video['clips'] 
        if len(clips) == 0:
            continue
        video_url = video['video_url']
        file_path = download_video(video_url)
        i = 1
        for clip in clips:
            cut_video(file_path, clip['start'], clip['length'], 'clip' + '_' + clip['start'] + '.mp4')
            i += 1

if __name__ == '__main__':
    json_file = str(sys.argv[1])
    data = load_json(json_file)
    extract_all(data)

    """
    json_example = {'data': [
        {'video_url':'https://www.youtube.com/watch?v=dP15zlyra3c', 'clips': [
            {'start':'00:00:03','length':'00:00:07'},
            {'start':'00:00:08','length':'00:00:03'},
            {'start':'00:00:10','length':'00:00:10'},
            {'start':'00:00:15','length':'00:00:02'}
        ]},
        {'video_url':'https://www.youtube.com/watch?v=Amq-qlqbjYA', 'clips': [
            {'start':'00:00:02','length':'00:01:00'}
        ]},
    ]}
    print json.dumps(json_example, indent=4, separators=(',', ': '), ensure_ascii=False)
    """
    
