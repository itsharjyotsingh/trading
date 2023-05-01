import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def doCall(username,password,startTime, endTime):
    driver = webdriver.Edge(executable_path="C:\DRIVERS\edgedriver\msedgedriver.exe")
    driver.get("https://algotest.in/")
    driver.maximize_window()

    # we will click on login button in the top right corner of navbar
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/nav/button[1]").click()

    # we will enter the username and password
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/form/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/form/div[2]/div/input").send_keys(password)

    # we will click on the login button
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/form/button").click()

    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[2]/ul/li").click()

    # we will store the result in a variable
    time.sleep(4)

    # time change
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/div[1]/div/div/input").send_keys(startTime)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div[1]/div/div/input").send_keys(endTime)

    # we will change the value of input box
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/input").clear()
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/input").send_keys("15")

    # we will change the value of input box
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/input").clear()
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div[3]/div/input").send_keys("15")

    # we will start backtest
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[2]/button[4]").click()
    # dont close the window after the execution
    time.sleep(100)


# we will create a loop which will start from 09:16 to 14:29
# for loop in python

def write_times_to_file():
    # Set the start time to 09:16
    hour = 9
    minute = 16

    # Open the file for writing
    with open("times.txt", "w") as f:
        # Loop through all the times from 09:16 to 14:29
        while hour <= 14:
            # Get the current time as a string
            time_str = f"{hour:02d}:{minute:02d}"

            # Write the current time to the file
            f.write(time_str + "\n")

            # Increment the minute by 1
            minute += 1

            # If the minute reaches 60, reset it to 0 and increment the hour by 1
            if minute == 60:
                minute = 0
                hour += 1

            # If the hour reaches 15, break out of the loop
            if hour == 15:
                break




write_times_to_file()

# how to put output in a text file


# input_values = [("7896907179", "SamsungS9+","0916","1529"),("7896907179", "SamsungS9+","0922","1520"),("7896907179", "SamsungS9+","0925","1320")]

# threads = []

# for input_value in input_values:
#     th = threading.Thread(target=doCall, args=input_value)
#     threads.append(th)

# for th in threads:
#     th.start()

# for th in threads:
#     th.join()

# time.sleep(10)