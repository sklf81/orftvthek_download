from html_retriever import retrieveHTML
#from parser import getM3U8Link
from html_parser import getM3U8Link
import json
import ffmpeg

#Parse-parameters
parameters = {
    "data_jsb_html_hierachy": ['<main class="main"',
                               '<div class="mod_player html5"',
                               '<div class="player_viewport "',
                               '<div class="jsb_ jsb_VideoPlaylist"',
                               'data-jsb='],
    #Indicator of which data_jsb element is the right one (there is only one with a certain property)
    "delivery" : "hls",
    #The delivery protocol must be hsl
    "quality_string" : "Sehr hoch"
    #The desired quality
    }

def downloadAsMP4(url, output_name):   
    string = retrieveHTML(url)
    
    stream_url = getM3U8Link(string, parameters)
    
    #With FFMPEG download video-stream and save it in the donwloads-folder
    ffmpeg.input(stream_url)\
    .output(str(output_name)+".mp4")\
    .run()
    
    return stream_url


"""
Anmerkungen:
    Funktioniert nicht bei Sendungen mit Jugendschutz
"""