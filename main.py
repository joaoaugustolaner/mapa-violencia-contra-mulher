from bs4 import BeautifulSoup
import httpx
import os



print("Starting downloads ... \n\n")
page_html = httpx.get("https://www.ssp.rs.gov.br/indicadores-da-violencia-contra-a-mulher")

soup = BeautifulSoup(page_html.text, "html.parser")
soup_links = soup.find(class_= 'artigo__texto')
soup_urls = soup_links.find_all('a')
os.system('mkdir ../data')
base = "https://www.ssp.rs.gov.br/"

count = 0
for url in soup_urls:
    
    command = f'wget -O $HOME/dev/personal/mvp_ssp/data/{count}.xlsx {base+url["href"]}'
    count+=1
    os.system(command)
    

print("Download succesfully finished!")
