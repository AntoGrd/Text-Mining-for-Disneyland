import scrap_hotel
import scrap_parc
from selenium import webdriver 
    
    
url_hotel = ["https://www.tripadvisor.fr/Hotel_Review-g1182377-d262678-Reviews-Disney_Hotel_New_York_The_Art_of_Marvel-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_F.html",
             "https://www.tripadvisor.fr/Hotel_Review-g1182377-d262679-Reviews-Disney_Newport_Bay_Club-Chessy_Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262682-Reviews-Disney_Sequoia_Lodge-Coupvray_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g226865-d262686-Reviews-Disney_Hotel_Cheyenne-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g5599092-d262683-Reviews-Disney_Hotel_Santa_Fe-Coupvray_Seine_et_Marne_Ile_de_France.html",
             "https://www.tripadvisor.fr/Hotel_Review-g1221082-d564634-Reviews-Disney_Davy_Crockett_Ranch-Bailly_Romainvilliers_Seine_et_Marne_Ile_de_France.html"]

url_parc = ["https://www.tripadvisor.fr/Attraction_Review-g226865-d189258-Reviews-Disneyland_Paris-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
            "https://www.tripadvisor.fr/Attraction_Review-g226865-d285990-Reviews-Walt_Disney_Studios_Park-Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html"]


#Récupération des hotels :
nom_hotels=["hotel_marvel","hotel_newport","hotel_sequoia","hotel_sante_fe","hotel_davy_crockett"]
#boucle pour récupérer tous les hotels
#for i in len(url_hotel):
for i in range(1,6) :
    driver = webdriver.Chrome("C:/Documents/travail/LYON2\M2/text_mining/projet_disney/chromedriver.exe")
    #driver = webdriver.Chrome("C:/Users/Sam/Documents/SISE/Text mining/Driver/chromedriver.exe")
    tab=scrap_hotel.scrapping_hotel(url_hotel[i],driver)
    tab.to_csv(nom_hotels[i]+'.csv', index=False, encoding = 'utf-8-sig')
    
#Récupération parcs :
driver = webdriver.Chrome("C:/Documents/travail/LYON2\M2/text_mining/projet_disney/chromedriver.exe")
#driver = webdriver.Chrome("C:/Users/Sam/Documents/SISE/Text mining/Driver/chromedriver.exe")
tab=scrap_parc.scrapping_parc(url_parc[0],driver)
tab.to_csv('parc_disneyland_paris.csv', sep ='\t', index=False, encoding = 'utf-8-sig')

driver = webdriver.Chrome("C:/Documents/travail/LYON2\M2/text_mining/projet_disney/chromedriver.exe")
#driver = webdriver.Chrome("C:/Users/Sam/Documents/SISE/Text mining/Driver/chromedriver.exe")
tab=scrap_parc.scrapping_parc(url_parc[1],driver)
tab.to_csv('parc_walt_disney_studios.csv', sep ='\t', index=False, encoding = 'utf-8-sig')







