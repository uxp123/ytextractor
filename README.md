# Hack Week @2017 - YT Extractor

This Python script will take in a JSON file with YouTube video URLs and timestamps and will extract the main video and cut the videos to create the clips.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python version 2.7.10 (Tested on)
* Have [ffmpeg](http://www.renevolution.com/ffmpeg/2013/03/16/how-to-install-ffmpeg-on-mac-os-x.html) installed
* Dependant on youtube-dl (Install through `pip install requirements.txt`)

Note: If youtube-dl fails, then you should get the most updated version of youtube-dl and not the one in the `requirements.txt`.

### Installing

Clone the project and change directories.

```
git clone git@github.com:JohnnyJohnAndTheFunkyBunch/ytextractor.git
```

Create virtual environment and activate it

```
virtualenv ytextractor
source ytextractor/bin/activate
```

Install the necesssary packages

```
pip install -r requirements.txt
```
## Running the tests
There is an `example.json` file that can be used to test the program. To run the program enter the following:

```
python ytextractor.py example.json
```

If there were no errors and the video folder looks like this:

```
videos/
├── Fox_Snow_Dive_-_Yellowstone_-_BBC_Two
│   ├── clip1.mp4
│   ├── clip2.mp4
│   ├── clip3.mp4
│   ├── clip4.mp4
│   └── main.mp4
└── Lee_Sunbin_-_FILA_Dance
    ├── clip1.mp4
    └── main.mp4
```
Then you're gucci.

## Documentation
Very simple to use the only argument you can give it, is the name of the JSON file with the information. Each video will contain it's own folder with the title of the video. Inside the folder will be a `main.mp4` video which is the full video and `clipX.mp4` videos which will be the clips.

All of this will be in the `videos` folder.

### How to run

Feed it a JSON file

```
python ytextractor.py myjsonfile.json
```


### JSON File

Here is an example of a JSON file:
```json
{
    "data": [
        {
            "clips": [
                {
                    "start": "00:00:03",
                    "length": "00:00:07"
                },
                {
                    "start": "00:00:08",
                    "length": "00:00:03"
                },
                {
                    "start": "00:00:10",
                    "length": "00:00:10"
                },
                {
                    "start": "00:00:15",
                    "length": "00:00:02"
                }
            ],
            "video_url": "https://www.youtube.com/watch?v=dP15zlyra3c"
        },
        {
            "clips": [
                {
                    "start": "00:00:02",
                    "length": "00:00:30"
                }
            ],
            "video_url": "https://www.youtube.com/watch?v=YeGWmq6ahUw"
        }
    ]
}
```
#### data

The `data` key contains all an array of all video objects. A video object contains `clips` and `video_url`.

#### video_url
The `video_url` is the standard YouTube URL of the video
#### clips
`clips` is an array of `start` and `length` values that determines which clips to extract from the video
#### start
`start` should be a string of the format `00:00:00` that determines the start of your clip.
#### length
`length` should be a string of the format `00:00:00` that determines the length of your clip. Hence if you want to get a clip from 00:00:03 to 00:00:10 then your `start` would be `00:00:03` and your `length` would be `00:00:07`.
