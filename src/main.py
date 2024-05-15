import urllib.request
import json
import ffmpeg

def retrieveHTML(url):
    fp = urllib.request.urlopen(url)
    bytestream = fp.read()
    
    string = bytestream.decode("utf8")
    fp.close()
    
    return string

def getM3U8Link(string, parameters):
    
    sliced = string
    
    #slice html to the beginning of the JSON data
    for element in parameters["data_jsb_html_hierachy"]:
        element = element.replace("&quot;", '"')
        index = sliced.index(element)
        sliced = sliced[index:]
        
    index = sliced.index('{')
    sliced = sliced[index:]
    #Find the end of the JSON section
    index = sliced.index('">')
    sliced = sliced[:index]
    
    #Replace &quot with "
    sliced = sliced.replace("&quot;", '"')
    
    #Get it as dictionary
    data = json.loads(sliced)
    
    #get video sources from data
    video = data["selected_video"]
    sources = video["sources"]
    
    sel_src = 0
    #get the correct source
    for src in sources:
        if (src["quality_string"] == parameters["quality_string"]) and (src["delivery"] == parameters["delivery"]):
            sel_src = src
            break
        
    src_m3u8_url = sel_src["src"]
    return src_m3u8_url

def downloadAsMP4(url, output_name): 
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
    
    string = retrieveHTML(url)
    
    stream_url = getM3U8Link(string, parameters)
    
    #With FFMPEG download video-stream and save it in the donwloads-folder
    ffmpeg.input(stream_url)\
    .output(str(output_name)+".mp4")\
    .run()
    
    return stream_url