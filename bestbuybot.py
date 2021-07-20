{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "05bf0f90",
   "metadata": {},
   "outputs": [
    {
     "ename": "NoSuchWindowException",
     "evalue": "Message: no such window: target window already closed\nfrom unknown error: web view not found\n  (Session info: chrome=91.0.4472.124)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNoSuchWindowException\u001b[0m                     Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-df8d0276d5cd>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     60\u001b[0m \u001b[0mwd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mitemURL\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     61\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 62\u001b[1;33m \u001b[0mCheckBuyButton\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     63\u001b[0m \u001b[0mcheckoutInstructionsBESTBUY\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0memail\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpassword\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msecurityCode\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     64\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-1-df8d0276d5cd>\u001b[0m in \u001b[0;36mCheckBuyButton\u001b[1;34m()\u001b[0m\n\u001b[0;32m     48\u001b[0m     \u001b[0mcheck\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mFalse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     49\u001b[0m     \u001b[1;32mwhile\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mcheck\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 50\u001b[1;33m         \u001b[1;32mif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mwd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element_by_class_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"add-to-cart-button\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_enabled\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     51\u001b[0m             \u001b[0maddToCartBtn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mwd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element_by_class_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"add-to-cart-button\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     52\u001b[0m             \u001b[0mcheck\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\.conda\\envs\\gpuBot\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mfind_element_by_class_name\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m    562\u001b[0m             \u001b[0melement\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element_by_class_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'foo'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    563\u001b[0m         \"\"\"\n\u001b[1;32m--> 564\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mby\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mCLASS_NAME\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    565\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    566\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_elements_by_class_name\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\.conda\\envs\\gpuBot\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[1;34m(self, by, value)\u001b[0m\n\u001b[0;32m    974\u001b[0m                 \u001b[0mby\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mCSS_SELECTOR\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    975\u001b[0m                 \u001b[0mvalue\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'[name=\"%s\"]'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 976\u001b[1;33m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[0m\u001b[0;32m    977\u001b[0m             \u001b[1;34m'using'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    978\u001b[0m             'value': value})['value']\n",
      "\u001b[1;32m~\\.conda\\envs\\gpuBot\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    320\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 321\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[0;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[1;32m~\\.conda\\envs\\gpuBot\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'alert'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'text'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    241\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 242\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    243\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    244\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNoSuchWindowException\u001b[0m: Message: no such window: target window already closed\nfrom unknown error: web view not found\n  (Session info: chrome=91.0.4472.124)\n"
     ]
    }
   ],
   "source": [
    "    from selenium import webdriver as wd\n",
    "    from selenium.webdriver import ActionChains\n",
    "    from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException\n",
    "    import chromedriver_binary\n",
    "    import time\n",
    "\n",
    "    email = \"\"#email\n",
    "    password = \"\"#password\n",
    "    securityCode =  \"\"#credit_card_security_code\n",
    "    itemURL = \"\"#Url of item you are tyring to buy\n",
    "    \n",
    "    def __init__(self, email, password, securityCode):\n",
    "        self.email = email\n",
    "        self.password = password\n",
    "        self.securityCode = securityCode\n",
    "\n",
    "    def bestbuyLogin(email, password):\n",
    "        emailInput = wd.find_element_by_xpath('//*[@id=\"fld-e\"]')   \n",
    "        type(emailInput)\n",
    "        emailInput.send_keys(email)\n",
    "        acctpassword = wd.find_element_by_xpath('//*[@id=\"fld-p1\"]')   \n",
    "        type(acctpassword)\n",
    "        acctpassword.send_keys(password)\n",
    "        signin = wd.find_element_by_class_name(\"c-button-icon-leading\")\n",
    "        signin.click()\n",
    "    \n",
    "        \n",
    "    def checkoutInstructionsBESTBUY(email, password, securityCode):   \n",
    "        wd.get(\"https://www.bestbuy.com/cart\")\n",
    "        try:\n",
    "            wd.find_element_by_xpath(\"//*[@class='btn btn-lg btn-block btn-primary']\").click()  \n",
    "            print(2)\n",
    "        except(NoSuchElementException, TimeoutException):\n",
    "            pass  \n",
    "        time.sleep(3)\n",
    "        bestbuyLogin(email, password)\n",
    "        time.sleep(3)\n",
    "        try:\n",
    "            security_code_input = wd.find_element_by_id(\"credit-card-cvv\")\n",
    "            type(security_code_input)\n",
    "            security_code_input.send_keys(securityCode)\n",
    "            wd.find_element_by_xpath(\"//*[@class='btn btn-lg btn-block btn-primary button__fast-track']\").click()\n",
    "        except(NoSuchElementException, TimeoutException):\n",
    "            pass\n",
    "        \n",
    "        \n",
    "    def CheckBuyButton():\n",
    "        check = False\n",
    "        while not check:    \n",
    "            if(wd.find_element_by_class_name(\"add-to-cart-button\").is_enabled()):\n",
    "                addToCartBtn = wd.find_element_by_class_name(\"add-to-cart-button\")\n",
    "                check = True\n",
    "            else:\n",
    "                wd.refresh()        \n",
    "        print(\"in stock\")\n",
    "        addToCartBtn.click()   \n",
    "\n",
    "    wd = wd.Chrome()\n",
    "    wd.get(itemURL)\n",
    "\n",
    "    CheckBuyButton()\n",
    "    checkoutInstructionsBESTBUY(email, password, securityCode)\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6b7d55d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
