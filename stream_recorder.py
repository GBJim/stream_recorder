import argparse
from subprocess import check_output, call
import os
import youtube_dl


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Youtube Live Stream Recorder')
    parser.add_argument('--url', dest='url', help='The URL of the Youtube lie stream video', type=str)
    parser.add_argument('--output', dest='output', help='The file of the output ts', type=str)
    parser.add_argument('--times', dest='times',default= 100, help='How many times of attemption to downlaod the stream', type=int)

    args = parser.parse_args()
    return args



if __name__ == "__main__":

    video_quality = "best"

    args = parse_args()
    print(args.output)
    output_folder = args.output

    if not os.path.exists(output_folder):
        print("Generating the folder for the recorded live stream")
        os.makedirs(output_folder)

    for i in range(args.times):
        #postprocessors =  [{'-loglevel': 'panic','key': 'FFmpegE xtractAudio','preferredcodec': 'mp3', 'preferredquality': '192', }]
        #output_path = os.path.join(output_folder, "{}_{}.ts".format(args.output, i+1))
        #ydl_opts = {"download":False,"simulate":True,"forceurl":True, "format":'best', "download_archive": output_path, 'postprocessors':postprocessors}

        #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            #ydl.download([args.url])

        command = ["sh", "download.sh",args.url]
        print(" ".join(command))
        call(command)

        with open("tmp_url.txt") as f:
            tmp_url = f.read().replace('\n', '')




        print(tmp_url)

        output_path = os.path.join(output_folder, "{}_{}.ts".format(args.output, i+1))
        command = ["ffmpeg", "-i", tmp_url, "-c", "copy", output_path ]
        print(" ".join(command))
        call(command)
