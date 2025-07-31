#----------------------------------------------
#-------Flask Intro and your first page--------
#----------------------------------------------
#---Flask is Micro Framework built with python-
#----------------------------------------------

#--HTML
#--CSS
#--JavaScript

#----------------------------------------------
# Importing Flask class from flask modul
from flask import Flask,render_template

#give app name unique 
skills_app =Flask(__name__)


#distribution road route page
@skills_app.route("/")
def homepage():
    return "Hello Abd From Flask Framework"
@skills_app.route("/about")
def about():
    return "Hello Abd From Flask Framework about page"

#that mean Only run the following code if this file is being run directly, not imported as a module.



if __name__== '__main__':

    skills_app.run(debug=True,port=9000)




#----------------------------------------------
#-----------Flask Create HTML Files------------
#----------------------------------------------

#--Flask render_template function

#--render_template function is used to render HTML files
#--render_template function takes the name of the HTML file as an argument 
# 
#  
@skills_app.route("/")
def homepage():    
    return render_template('homepage.html',pagetitle="Homepage")

#--render_template function is used to render HTML files
@skills_app.route("/about")
def about():
    return  render_template('about.html',pagetitle="About")


if __name__== '__main__':

    skills_app.run(debug=True,port=9000)

              
#----------------------------------------------
#-----Flask =>Create &Extend HTML templates----
#----------------------------------------------

@skills_app.route("/")
def homepage():    
    return render_template('homepage.html',pagetitle="Homepage",test="Hello A" ,custom_css="home")

#--render_template function is used to render HTML files
@skills_app.route("/about")
def about():
    return  render_template('about.html',pagetitle="About",test="Hello B")


@skills_app.route("/add")
def add():
    return render_template('add.html',pagetitle="Add",test="Hello C", custom_css="add")
if __name__== '__main__':

    skills_app.run(debug=True,port=9000)



#----------------------------------------------
#---Flask => Skills Page Using Lists Data------
#----------------------------------------------

my_skills=[("HTML",80),("CSS",70),("JavaScript",60),("Python",90),("Flask",85),("c++",75),("Java",65),("SQL",80),("Git",70)]

@skills_app.route("/")
def homepage():    
    return render_template('homepage.html',pagetitle="Homepage",test="Hello A" ,custom_css="home")

#--render_template function is used to render HTML files
@skills_app.route("/about")
def about():
    return  render_template('about.html',pagetitle="About",test="Hello B")


@skills_app.route("/add")
def add():
    return render_template('add.html',pagetitle="Add",test="Hello C", custom_css="add")
@skills_app.route("/skills")
def skills():
    return render_template('skills.html',pagetitle="skills",skills=my_skills ,pagehead="my Skills ", description="This is my skills page", custom_css="skills")

if __name__== '__main__':

    skills_app.run(debug=True,port=9000)




#------------------------------------------------
#---Wep Scraping => control browser with selenium
# ------------------------------------------------
# contorl browser selenium for automated testing
# download file form internet selenium from https://pypi.org/project/selenium/ 
# Suptitle download and add on your movies [Many Modyles]
# get quote from website
# get gold currencies rate
# get News from website
#----------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# إعداد خيارات المتصفح
options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-blink-features=AutomationControlled')  # تحسين ضد كشف الروبوتات

# إعداد الخدمة
service = Service(ChromeDriverManager().install())

# إنشاء المتصفح
browser = webdriver.Chrome(service=service, options=options)

# فتح Google
browser.get("https://www.google.com/")
time.sleep(2)

# البحث عن Python
search_input = browser.find_element(By.NAME, "q")
search_input.send_keys("Python")
search_input.submit()
time.sleep(2)

# الدخول إلى أول نتيجة (غالباً تكون python.org)
first_result = browser.find_element(By.CSS_SELECTOR, "h3")
first_result.click()
time.sleep(2)

# الآن نحن في موقع https://www.python.org/
# نبحث عن نص يحتوي على أحدث إصدار

try:
    release_element = browser.find_element(By.CSS_SELECTOR, ".release-number a")
    latest_version = release_element.text.strip()
    print("🔶 latest_version:", latest_version)
except Exception as e:
    print("wrong:", e)

# إغلاق المتصفح (اختياري)
# browser.quit()
