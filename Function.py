def buyer(url):
    from selenium import webdriver as wd
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver import ActionChains
    from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
    import time
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from twilio.rest import Client
    from twilio.base.exceptions import TwilioRestException


    email =  #email
    password = #password
    securityCode =  #credit_card_security_code


    toNumber =  #phone number
    fromNumber = #twilio phone number
    accountSid =  #acct Sid
    authToken =  #auth token
    client = Client(accountSid, authToken)

    def __init__(self, email, password, securityCode):
        self.email = email
        self.password = password
        self.securityCode = securityCode
    
        
    def checkoutInstructionsBESTBUY(email, password, securityCode):   
        wd.get("https://www.bestbuy.com/cart")
        try:
            wd.find_element(By.XPATH, "//*[@class='btn btn-lg btn-block btn-primary']").click()  
            print(2)
        except(NoSuchElementException, TimeoutException):
            pass  
        time.sleep(1)
        
        WebDriverWait(wd, 2).until(EC.presence_of_element_located((By.ID, 'fld-e')))
        print("logging in")
        
        emailInput = wd.find_element(By.ID,'fld-e')   
        type(emailInput)
        emailInput.send_keys(email)
        acctpassword = wd.find_element(By.XPATH,'//*[@id="fld-p1"]')   
        type(acctpassword)
        acctpassword.send_keys(password)
        signin = wd.find_element(By.CLASS_NAME ,"c-button-icon-leading")
        print("Logged in")
        signin.click()
    
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cvv"]')))
        
        security_code_input = wd.find_element(By.XPATH,'//*[@id="cvv"]')
        type(security_code_input)  
        security_code_input.send_keys(securityCode)
        print("cvv is in")
        wd.find_element(By.XPATH, "//*[@class='btn btn-lg btn-block btn-primary button__fast-track']").click()
        print("bought!!") 
        
    def CheckBuyButton():
        print("test")
        check = False
        while not check:    
            if(wd.find_element(By.CLASS_NAME,"add-to-cart-button").is_enabled()):
                addToCartBtn = wd.find_element(By.CLASS_NAME, "add-to-cart-button")
                check = True
            else:
                wd.refresh()        
        try:
             client.messages.create(to=toNumber, from_=fromNumber,
             body=f'Product is in Stock!!')
        except (NameError, TwilioRestException):
             pass
        print("in stock")
        addToCartBtn.click()  
         
  
    #options = Options()
    #options.add_argument("headless")
    wd = wd.Chrome(ChromeDriverManager().install())#,options = options)
    wd.get(url)  
    CheckBuyButton()
    checkoutInstructionsBESTBUY(email, password, securityCode)
    
