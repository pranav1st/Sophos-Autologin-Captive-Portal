from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import winwifi
import time
import urllib
import os
import pymsgbox

def rescan():
    net_list=[]
    for i in winwifi.WinWiFi.scan():
        net_list.append(i.ssid)
    if("PESU-BOYS HOSTEL" in net_list):
        os.system('netsh wlan connect name="PESU-BOYS HOSTEL" ssid="PESU-BOYS HOSTEL" interface=Wi-Fi')
        print("Connected to PESU Boys Hostel!")
    elif("PESU LIB" in net_list):
        os.system('netsh wlan connect name="PESU LIB" ssid="PESU LIB" interface=Wi-Fi')
        print("Connected to PESU Library!")
    else:
        print("Network not found!")
    WebSrvice()

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def Maintain():
    while connect():
        print("No Issues!")
        time.sleep(120)
    rescan()

def WebSrvice(SRN,passwd):
    driver = webdriver.Chrome()
    options = Options()
    options.add_argument("headless")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options = options)
    driver.get('http://192.168.254.1:8090/httpclient.html')

    srn_box = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]')
    srn_box.send_keys(SRN)
    pass_box = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/input[2]')
    pass_box.send_keys(passwd)
    login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div[3]/a/div')
    login_button.click()
    Maintain()

def main():
    try:
        f = open("cred.csv")
        SRN,passwd=f.read().split(",")
        print(SRN,passwd)
        f.close()
    except:
        f = open("cred.csv","w")
        SRN = pymsgbox.prompt("Enter SRN")
        passwd = pymsgbox.password('Enter your password')
        f.write(SRN+","+passwd)
        f.close()
    WebSrvice(SRN,passwd)
    rescan()
main()
