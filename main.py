# -*- coding: UTF-8 -*-

import hashlib, platform, random, string, time, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class FakeNameGenerator():
    def __init__(self):
        self.html = ""

    def GenerateIdenity(self):
        self.html = requests.get("https://www.fakenamegenerator.com/", headers={
                                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}).text
        self.name = {"completename": self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0], "first": self.html.split('<div class="address">')[
            1].split('<h3>')[1].split('</h3>')[0].split(" ")[0], "last": self.html.split('<div class="address">')[1].split('<h3>')[1].split('</h3>')[0].split(" ")[-1]}

        addy = self.html.split('<div class="adr">')[1].split("                                        ")[
            1].split("                                        </div>")[0]
        addynum = addy.split(" ")[0]
        streetlist = self.html.split('<div class="adr">')[1].split("                                        ")[
            1].split("                                        </div>")[0].split("<br />")[:1][0].split(" ")[1:]
        street = ""

        province = addy.split('<br />')[1].split(",")[0]
        ZIP = addy.split(", ")[1].split('   ')[0]
        for i in streetlist:
            street = street + " " + i
        self.addy = {"addynum": addynum,
                     "street": street[1:], "province": province, "zip": ZIP}

        self.SSN = self.html.split(
            'tal"><dt>SSN</dt><dd>')[1].split(' <div class="adtl">')[0]
        self.phone = self.html.split(
            "<dt>Phone</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.phoneprefix = "+" + \
            self.html.split(
                "<dt>Country code</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        birthday = "+" + \
            self.html.split(
                "<dt>Birthday</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        Month = birthday.split(" ")[0].replace("+", "")
        Day = birthday.split(" ")[1].replace(",", "")
        Year = birthday.split(" ")[-1]
        self.birthday = {"Day": Day, "Month": Month, "Year": Year}
        self.age = self.html.split(
            "<dt>Age</dt>")[1].split(" years old</dd>")[0].split("<dd>")[1]
        self.tropicalzodiac = self.html.split(
            "<dt>Tropical zodiac</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.email = self.html.split(
            '<dt>Email Address</dt>')[1].split('<dd>')[1].split('        ')[0]
        self.username = self.html.split(
            "<dt>Username</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.password = self.html.split(
            "<dt>Password</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.website = self.html.split(
            "<dt>Website</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.useragent = self.html.split(
            "<dt>Browser user agent</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.cardtype = self.html.split(
            '<h3 class="hh3">Finance</h3>')[1].split('<dt>')[1].split('</dt>')[0]
        self.exp = self.html.split(
            "<dt>Expires</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        try:
            self.CVC = self.html.split(
                "<dt>CVC2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        except:
            self.CVC = self.html.split(
                "<dt>CVV2</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.company = self.html.split(
            "<dt>Company</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.job = self.html.split(
            "<dt>Occupation</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.height = self.html.split(
            "<dt>Height</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.weight = self.html.split(
            "<dt>Weight</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.bloodtype = self.html.split(
            "<dt>Blood type</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.UPSTrackingnum = self.html.split(
            "<dt>UPS tracking number</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.MoneyGram = self.html.split(
            "<dt>MoneyGram MTCN</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.WesternUnion = self.html.split(
            "<dt>Western Union MTCN</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.favcolor = self.html.split(
            "<dt>Favorite color</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.car = self.html.split(
            "<dt>Vehicle</dt>")[1].split("</dd>")[0].split("<dd>")[1]
        self.GUID = self.html.split(
            "<dt>GUID</dt>")[1].split("</dd>")[0].split("<dd>")[1]

def randomSSN(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def createOpenCCC(email, use_captcha):
    try:
        config = open("captcha.txt", "r+").readlines()
        captcha = config[0]
        captcha, _ = captcha.split("\n")
    except:
        pass

    driver = webdriver.Firefox(executable_path=geckopath)

    driver.get(
        "https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/render.uP?pP_execution=e1s2")

    datafake = FakeNameGenerator()
    datafake.GenerateIdenity()

    first = datafake.name["first"]
    last = datafake.name["last"]
    number = datafake.phone
    ssn = str(str(datafake.SSN) + str(randomSSN())).replace("X", "")
    street = datafake.addy["addynum"] + " " + datafake.addy["street"]
    city = datafake.addy["province"]
    zipcode = datafake.addy["zip"]

    pw = datafake.password
    name = datafake.username + randomSSN()

    ssnlol = ssn

    register_button = driver.find_element_by_id("accountFormSubmit")
    register_button.click()

    # Page 1

    first_name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )
    first_name.send_keys(first)

    no_middle_name = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "inputHasNoMiddleName"))
    )
    no_middle_name.click()

    last_name = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "inputLastName"))
    )
    last_name.send_keys(last)

    prev_name = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "hasOtherNameNo"))
    )
    prev_name.click()

    preffered_name = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "hasPreferredNameNo"))
    )
    preffered_name.click()

    month_one = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputBirthDateMonth option[value="3"]'))
    )
    month_one.click()

    day_one = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputBirthDateDay option[value="7"]'))
    )
    day_one.click()

    year_one = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputBirthDateYear'))
    )
    year_one.send_keys("1994")

    month_two = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputBirthDateMonthConfirm option[value="3"]'))
    )
    month_two.click()

    day_two = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputBirthDateDayConfirm option[value="7"]'))
    )
    day_two.click()

    year_two = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputBirthDateYearConfirm'))
    )
    year_two.send_keys("1994")

    select_ssn = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, '-have-ssn-yes'))
    )
    select_ssn.click()

    input_ssn = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, '-ssn-input1'))
    )
    input_ssn.send_keys(ssnlol)

    input_ssn_confirm = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, '-ssn-input2'))
    )
    input_ssn_confirm.send_keys(ssnlol)

    page_one_submit = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'accountFormSubmit'))
    )
    page_one_submit.click()

    print("\n\n[*] Page 1/3 Done!")

    # Page 2

    input_email = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputEmail'))
    )
    input_email.send_keys(email)

    input_emailconfirm = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputEmailConfirm'))
    )
    input_emailconfirm.send_keys(email)

    input_phone = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSmsPhone'))
    )
    input_phone.send_keys(number)

    input_street = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputStreetAddress1'))
    )
    input_street.send_keys(street)

    input_city = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputCity'))
    )
    input_city.send_keys(city)

    input_state = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputState option[value="CA"]'))
    )
    input_state.click()

    input_zipcode = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPostalCode'))
    )
    input_zipcode.send_keys(zipcode)

    page_two_submit = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'accountFormSubmit'))
    )
    page_two_submit.click()

    try:
        driver.find_element_by_id("inputUserId").send_keys(name)
    except:
        driver.find_element_by_id("messageFooterLabel").click()
        driver.find_element_by_id("inputAddressValidationOverride").click()
        driver.find_element_by_id("accountFormSubmit").click()

    print("\n\n[*] Page 2/3 Done!")

    # Page 3

    input_userid = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputUserId'))
    )
    input_userid.send_keys(name)

    input_pass = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPasswd'))
    )
    input_pass.send_keys(pw)

    input_passconf = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPasswdConfirm'))
    )
    input_passconf.send_keys(pw)

    input_pin = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPin'))
    )
    input_pin.send_keys("0420")

    input_pinconf = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputPinConfirm'))
    )
    input_pinconf.send_keys("0420")

    input_security1 = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion1 option[value="10"]'))
    )
    input_security1.click()
    input_answer1 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer1'))
    )
    input_answer1.send_keys("12")

    input_security2 = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion2 option[value="4"]'))
    )
    input_security2.click()
    input_answer2 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer2'))
    )
    input_answer2.send_keys("Josh")

    input_security3 = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#inputSecurityQuestion3 option[value="2"]'))
    )
    input_security3.click()
    input_answer3 = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer3'))
    )
    input_answer3.send_keys("Tesla 3")

    print("\n\n[*] Bypassing the Captcha!\n\n")

    if use_captcha == "1":

        url = "https://2captcha.com/in.php?key=" + captcha + \
            "&method=userrecaptcha&json=0&googlekey=6LeaXhITAAAAACiHR6YSn1YKAUrrTZTLtjxuwYx6&pageurl=https://www.openccc.net/uPortal/p/AccountCreation.ctf1/max/render.uP?pP_execution=e1s4"

        r = requests.get(url)

        _, moin = r.text.split("|")
        time.sleep(20)

        url2 = "https://2captcha.com/res.php?key=" + captcha + "&action=get&id=" + moin
        r = requests.get(url2)
        while "CAPCHA_NOT_READY" in r.text:

            url2 = "https://2captcha.com/res.php?key=" + captcha + "&action=get&id=" + moin
            r = requests.get(url2)
            print("[*] Waiting for 2Captcha\n\n")
            time.sleep(5)
        try:
            _, key = r.text.split("|")
        except:
            print(r.text)

        command = 'document.getElementById("g-recaptcha-response").innerHTML="' + \
            key + '";'
        driver.execute_script(
            "document.getElementsByName('captchaResponse')[0].setAttribute('type', 'shown');")
        driver.find_element_by_name("captchaResponse").send_keys(key)
        time.sleep(5)
        driver.execute_script(command)
    elif use_captcha == "2":
        print("Solve the captcha now!\n\n")
        try:
            element = driver.find_element_by_id("accountFormSubmit")
            driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            print("Failed to scroll")
        captcha_solved = "1"
        while captcha_solved == "1":
            captcha_solved = input("[Y]Solved?\n")
    else:
        print("Error")

    time.sleep(5)
    driver.find_element_by_id("accountFormSubmit").click()
    time.sleep(5)

    print("\n\n[*] Page 3/3 Done!")

    with open("result.txt", "a+") as file:
        file.write("Username: " + name + ", Password: " + pw + ", Email: " + email + ", First: " + first + ", Last: " + last + ", Number: " +
                   number + ", SSN: " + ssn + ", Street Address: " + street + ", City: " + city + ", Zipcode: " + zipcode)
        file.write("\n\n")

    print("\n\nSuccess! Check result.txt\n\n")

if platform.system() == "Windows":  # checking OS
    geckopath = "./geckodriver.exe"
else:
    geckopath = "./geckodriver"

print("""
OpenCCC Account
by Dz
""")

email = input("Enter your email: ")

use_captcha = input("\nWhich captcha service do you want to use?\n1. 2Captcha (Needs API Key) \n2. None (Manual)\n")
if use_captcha == "1":
    print("2Captcha!\n")
elif use_captcha == "2":
    print("Manually!\n")
else:
    print("Wrong Input!")
    time.sleep(5)
    exit()

def run(email, use_captcha):
    try:
        createOpenCCC(email, use_captcha)
    except Exception as E:
        open("error.txt", "a+").write(str(E)+"\n")
        print(E)

run(email, use_captcha)