import scrap_hotel
import scrap_parc
from selenium import webdriver 
from cleanData import clean_data_hotel, clean_data_parc
    
url_hotel = ["https://www.tripadvisor.fr/Hotel_Review-g1182377-d262678-Reviews-Disney_Hotel_New_York_The_Art_of_Marvel-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_F.html",
             "https://www.tripadvisor.fr/Hotel_Review-g1182377-d262679-Reviews-Disney_Newport_Bay_Club-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262682-Reviews-Disney_Sequoia_Lodge-Coupvray_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g226865-d262686-Reviews-Disney_Hotel_Cheyenne-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262683-Reviews-Disney_Hotel_Santa_Fe-Coupvray_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g1221082-d564634-Reviews-Disney_Davy_Crockett_Ranch-Bailly_Romainvilliers_Seine_et_Marne_Ile_de_France.html"]

url_parc = ["https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
            "https://www.tripadvisor.fr/Attraction_Review-g226865-d285990-Reviews-Walt_Disney_Studios_Park-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"]

#Indiquer le driver présent sur la machine
driver = webdriver.Chrome("C:/Users/Sam/Documents/SISE/Text mining/Driver/chromedriver.exe")
#driver = webdriver.Chrome("C:/Documents/travail/LYON2\M2/text_mining/projet_disney/chromedriver.exe")

namesHotel = ["Hotel_New_York_The_Art_of_Marvel", "Disney_Newport_Bay_Club","Disney_Hotel_Cheyenne","Disney_Davy_Crockett_Ranch"]
namesParc  = ["Disneyland_Paris","Walt_Disney_Studios_Park"]

#scraping hotel 
compteurHotel = 0
for url in url_hotel:

    tab = scrap_hotel.scrapping_hotel(url,driver)
    tab = clean_data_hotel(tab)
    tab.to_csv(namesHotel[namesHotel] + ".csv")
    compteurHotel += 1

#scraping parc 
compteurParc = 0
for url in url_hotel:

    tab = scrap_parc.scrapping_parc(url,driver)
    tab = clean_data_parc(tab)
    tab.to_csv(namesHotel[compteurParc] + ".csv")
    compteurParc += 1
