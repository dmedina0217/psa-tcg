import requests
from bs4 import BeautifulSoup


class psa_dna_web_scraper:
    psa_dna_url="https://www.psacard.com/cert/"

    def return_response(self,successful,message,data):
        response = dict()
        response['success']=successful
        response['message']=message
        response['data']=data
        return response

    def get_psa_dna_card_data(self,psa_cert_number):
        emptyerror = "empty psa certificate number"
        successM = "success in obtaining data from psa dna website"
        #check data
        if psa_cert_number == None:
            return self.return_response(False,emptyerror,"")
        else:
            psa_cert_number = str(psa_cert_number)
            if len(psa_cert_number) > 1:
                #scrap website using cert number
                url_to_use = self.psa_dna_url + str(psa_cert_number)
                #send request to psa dna website
                data_from_psa_dna_website = requests.get(url_to_use)
                if data_from_psa_dna_website.status_code == 200:
                    #'success in retrieving data from psa dna website'
                    soup = BeautifulSoup(data_from_psa_dna_website.text, 'html.parser')
                    title_list = []
                    values_list = []
                    #table titles
                    for t in  soup.find_all("td", class_="cert-grid-title"):
                        title_list.append(t.text.strip())
                    #table row data from website
                    for v in soup.find_all("td", class_="cert-grid-value"):
                        values_list.append(v.text.strip())
                    tuple_results = list(zip(title_list,values_list))
                    #modify response to True and add to data for return
                    return self.return_response(True,successM,tuple_results)
                else:
                    unsuccessfulM = "unable to get response from psa dna website"
                    return self.return_response(False,unsuccessfulM,data_from_psa_dna_website)
            else:
                return self.return_response(False,"input must be have a length greater than 1",psa_cert_number) 


    
# app = psa_dna_web_scraper()
# results = app.get_psa_dna_card_data(1234567)
# print(results)

    
# app = psa_dna_web_scraper()

# [print(app.get_psa_dna_card_data(i)) for i in range(0,123456)]
