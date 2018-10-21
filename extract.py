import re
import requests
from bs4 import BeautifulSoup

PMs = {
'howard': "<prime-minister>Howard, John</prime-minister>",
'rudd': "<prime-minister>Rudd, Kevin</prime-minister>",
'gillard': "<prime-minister>Gillard, Julia</prime-minister>",
'abbott': "<prime-minister>Abbott, Tony</prime-minister>",
'turnbull': "<prime-minister>Turnbull, Malcolm</prime-minister>",
}


interview = "<release-type>Interview</release-type>"
transcript = "<release-type>Transcript</release-type>"
transcriptId = 9960


def extract(text):
    for name in PMs:
        if PMs[name] in text and (interview in text or transcript in text):
            txt = open(name + '_raw_text_v1.txt', 'a+', encoding='utf-8')
            txt.write(raw)
            txt.close()

    re1 = re.findall(r'(((?<=PM:).*?))(?!PM:)\b[A-Z][A-Z]+\b', text, flags=re.DOTALL) #for Rudd
    re2 = re.findall(r'((?<=PRIME MINISTER:).*?)(?!PRIME)(?!MINISTER)\b[A-Z][A-Z]+\b', text, flags=re.DOTALL) # for Howard
    re3 = re.findall(r'((?<=PM:).*?)(?!PM)\b[A-Z][A-Z]+\b', text, flags=re.DOTALL) #for Gillard
    
    for content in [re1, re2, re3]:
        if content:
            txt = open(name + '_clean_text_v1.txt', 'a+', encoding='utf-8')
            txt.write(raw)
            txt.close()
            

while transcriptId <= 11928:
    url = "https://pmtranscripts.pmc.gov.au/query?transcript=" + str(transcriptId)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    output = response.read().decode("utf-8")
    soup = BeautifulSoup(output, "lxml")
    raw = soup.getText()
    extract(raw)
    transcriptId += 1


























