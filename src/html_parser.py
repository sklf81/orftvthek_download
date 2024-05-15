from html.parser import HTMLParser
import json


class  TVTHEKParser(HTMLParser):
    tag = 0
    attrs = 0
    start = 0
    end = 0
    
    def handle_starttag(self, tag, attrs): 
        self.tag = tag
        self.attrs = attrs
        self.start = self.getpos()[0]
        
        return
    
    def getTag(self):
        return self.tag
    
    def getAttrs(self):
        return self.attrs
    
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    def handle_endtag(self, tag):
        self.end = self.getpos()[0]
        return
    
    def handle_data(self, data):
        return
    
    def handle_comment(self, data):
        return
    
    def handle_entityref(self, name):
        return
    
    def handle_charref(self, name):
        return
    
    def handle_decl(self, data):
        return

"""
def getM3U8Link(string, parameters):

    Parser = TVTHEKParser()

    sliced = string
    
    for element in parameters["data_jsb_html_hierachy"]:
        #ref_tag, ref_attrs, _start, _end = Parser.feed(element)
        Parser.feed(element)
        ref_tag = Parser.getTag()
        ref_attrs = Parser.getAttrs()
        
        tag, attrs, start, end = "", "", 0, 0
        
        while True:
            sliced = string[start:]
            Parser.feed(sliced)
            tag = Parser.getTag()
            attrs = Parser.getAttrs()
            start = Parser.getStart()
            end = Parser.getEnd()

            if tag == ref_tag and attrs == ref_attrs:
                sliced = string[start:end]
                break

    
    return sliced
"""

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
    

