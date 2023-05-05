import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import pandas as pd
from xlsxwriter import Workbook

lock = threading.RLock()

threadsToWrite = []

def doCall(startTime, endTime):
    with lock:
        # time.sleep(3)
        
        today = datetime.date.today()

        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[2]/ul/li").click()
        
        # we will store the result in a variable
        time.sleep(3)
        # time change
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/div[1]/div/div/input").send_keys(startTime)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div/input").send_keys(endTime)

        # we will change the value of input box
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/input").clear()
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/input").send_keys("20")

        # we will change the value of input box
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/input").clear()
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/input").send_keys("20")

        # we will start backtest
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/button[4]").click()

        time.sleep(10)

        days = ["all","monday","tuesday","wednesday","thursday","friday"]

        data = {}

        for day in days:

            # we will scroll till the element is visible
            changer = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[2]/div[2]/canvas")
            driver.execute_script("arguments[0].scrollIntoView();", changer)

            # time.sleep(5)

            if(day=="all"):
                data["In time"] = startTime
                data["Out time"] = endTime
                data["Strike Type"] = "ATM"
                data["Index"] = "Banknifty"
                data["Call Stop Loss"] = 20
                data["Put Stop Loss"] = 20
                # we will stringify the data
                data["End date"] = today
            elif(day=="monday"):
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[2]").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[3]").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[4]").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[5]").click()
            
            elif(day=="tuesday"):
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[2]").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[1]").click()
                
            elif(day=="wednesday"):
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[2]").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[3]").click()

            elif(day=="thursday"):
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[3]").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[4]").click()

            elif(day=="friday"):
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[4]").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[1]/div[1]/label[5]").click()

            profit2021 = driver.execute_script('return document.querySelector("#backtest-results > div > div:nth-child(3) > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(14) > p")')
            profit2022 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[2]/div/table/tbody/tr[2]/td[14]/p").text
            profit2023 = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[3]/div[2]/div/table/tbody/tr[3]/td[14]/p").text
            overAllProfit = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[1]/tbody/tr[1]/td[2]").text
            averageProfitPerTrade = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[1]/tbody/tr[3]/td[2]").text
            winper = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[1]/tbody/tr[4]/td[2]").text
            averageProfitOnWinningTrades = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[1]/tbody/tr[6]/td[2]").text
            averageLossOnLosingTrades = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[2]/tbody/tr[1]/td[2]").text
            maxProfitOnSingleTrade = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[2]/tbody/tr[2]/td[2]").text
            maxLossOnSingleTrade = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[2]/tbody/tr[3]/td[2]").text
            maxDrawdown = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[2]/tbody/tr[4]/td[2]").text
            daysOfMaxDrawdown = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[2]/tbody/tr[5]/td[2]").text
            rewardToRiskRatio = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[3]/tbody/tr[2]/td[2]").text
            expectancyRatio = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[5]/div/div[4]/div[2]/table[3]/tbody/tr[3]/td[2]").text

            profit2021_str = profit2021.get_property('innerText')
            profit2021_str = profit2021_str.replace('₹','').strip()
            profit2022_str = profit2022.replace('₹','').strip()
            profit2023_str = profit2023.replace('₹','').strip()
            overAllProfit_str = overAllProfit.replace('₹','').strip()
            averageProfitPerTrade_str = averageProfitPerTrade.replace('₹','').strip()
            winper_str = winper.replace('%','').strip()
            averageProfitOnWinningTrades_str = averageProfitOnWinningTrades.replace('₹','').strip()
            averageLossOnLosingTrades_str = averageLossOnLosingTrades.replace('₹','').strip()
            maxProfitOnSingleTrade_str = maxProfitOnSingleTrade.replace('₹','').strip()
            maxLossOnSingleTrade_str = maxLossOnSingleTrade.replace('₹','').strip()
            maxDrawdown_str = maxDrawdown.replace('₹','').strip()
            daysOfMaxDrawdown_str = daysOfMaxDrawdown
            rewardToRiskRatio_str = rewardToRiskRatio
            expectancyRatio_str = expectancyRatio

            data[day+" 2021 profit"] = profit2021_str
            data[day+" 2022 profit"] = profit2022_str
            data[day+" 2023 profit"] = profit2023_str
            data[day+" Overall profit"] = overAllProfit_str
            data[day+" Average profit per trade"] = averageProfitPerTrade_str
            data[day+" Win percentage"] = winper_str
            data[day+" Average profit on winning trades"] = averageProfitOnWinningTrades_str
            data[day+" Average loss on losing trades"] = averageLossOnLosingTrades_str
            data[day+" Max profit on single trade"] = maxProfitOnSingleTrade_str
            data[day+" Max loss on single trade"] = maxLossOnSingleTrade_str
            data[day+" Max drawdown"] = maxDrawdown_str
            data[day+" Days of max drawdown"] = daysOfMaxDrawdown_str
            data[day+" Reward to risk ratio"] = rewardToRiskRatio_str
            data[day+" Expectancy ratio"] = expectancyRatio_str

        thread = threading.Thread(target=append_to_excel, args=(data,))
        threadsToWrite.append(thread)

def write_times_to_file(data):
    with open("data.txt", "w") as f:
        f.write(data + "\n")

def putDataIntoFile(data):
    with open("data.txt", "a") as f:
        f.write(str(data) + "\n")

def process_data(data):
    data = data.split()

    doCall(data[0], data[1])

def read_file(filename):
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/nav/button[1]").click()

    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/form/div[1]/input").send_keys("")
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/form/div[2]/div/input").send_keys("")

    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/form/button").click()

    time.sleep(4)

        
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Split the lines into chunks of 20
    chunks = [lines[i:i+2] for i in range(0, len(lines), 2)]

    # Process each chunk in a separate thread
    for chunk in chunks:
        threads = []
        if(threadsToWrite.__len__() >= 5):
            for i in threadsToWrite:
                i.start()
                i.join()
            threadsToWrite.clear()
        for i in chunk:
            thread = threading.Thread(target=process_data, args=(i,))
            threads.append(thread)
        for th in threads:
            th.start()
        for th in threads:
            th.join()
    for i in threadsToWrite:
        i.start()
        i.join()
    threadsToWrite.clear()
        
import pandas as pd

def append_to_excel(data):
    df = pd.read_excel("example.xlsx", sheet_name="Sheet1")

    new_row = pd.DataFrame(data, index=[0])
    df = df._append(new_row, ignore_index=True)

    with pd.ExcelWriter("example.xlsx", engine="xlsxwriter") as writer:
        df.to_excel(writer, sheet_name="Sheet1", index=False)


driver = webdriver.Edge(executable_path="C:\DRIVERS\edgedriver\msedgedriver.exe")
driver.get("https://algotest.in/")
driver.maximize_window()

read_file("times.txt")

driver.close()
