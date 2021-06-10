import requests
from bs4 import BeautifulSoup
import smtplib
import time
url = "https://www.amazon.in/Universal-Cardiod-Shotgun-Microphone-Camcorder/dp/B06XWH97X8/ref=pd_lpo_267_t_2/258-2975344-7342147?_encoding=UTF8&pd_rd_i=B06XWH97X8&pd_rd_r=11c5d36c-02cd-41fa-872d-231cd3d0ebf5&pd_rd_w=0flh9&pd_rd_wg=81LIC&pf_rd_p=381a0cfc-e204-4c65-93f2-a892ca3da5ad&pf_rd_r=HB9MPT762XJK83CFX3K1&psc=1&refRID=HB9MPT762XJK83CFX3K1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

def check_price():
        page=requests.get(url,headers=headers)
        soup=BeautifulSoup(page.content,'html.parser')
        title=soup.find(id="productTitle").get_text()
        price=soup.find(id="priceblock_ourprice").get_text().strip();
        new_price=float(price.replace(",","").replace("₹","").strip())

        print(title.strip());
        print(new_price);
        if(new_price < 1700.00):
           send_email()
        if(new_price>1700.00):
            send_email()

def send_email():
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('jainpriyam2001@gmail.com','cevbpoirhmzcqbtq')

        subject =' WOW! price fell down'
        body='check the amamzon link https://www.amazon.in/Universal-Cardiod-Shotgun-Microphone-Camcorder/dp/B06XWH97X8/ref=pd_lpo_267_t_2/258-2975344-7342147?_encoding=UTF8&pd_rd_i=B06XWH97X8&pd_rd_r=11c5d36c-02cd-41fa-872d-231cd3d0ebf5&pd_rd_w=0flh9&pd_rd_wg=81LIC&pf_rd_p=381a0cfc-e204-4c65-93f2-a892ca3da5ad&pf_rd_r=HB9MPT762XJK83CFX3K1&psc=1&refRID=HB9MPT762XJK83CFX3K1' 
        
        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'jainpriyam2001@gmail.com',
            'jillambros21@gmail.com',
             msg
        )
        print('HEY EMAIL HAS BEEN SENT!')

        server.quit()
while(True):
     check_price()
     time.sleep(3600)


