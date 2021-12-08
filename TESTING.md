# Full Testing
## Contents
+ [Validator Testing](#validator-testing)
+ [Manually Testing Functionality](#manually-testing-functionality)
+ [Responsive Testing](#responsive-testing)
---
---

## Validator Testing
### **HTML**

 I checked all of the HTML pages using [W3C Markup Validation Service](https://validator.w3.org/)

 I check from the live site by right clicking each page, selecting View Page Source and running that generated code through the validator.

 All pages passed all checks. 


### **CSS**

I checked the CSS file using [W3C CSS Markup Validation Service](https://jigsaw.w3.org/css-validator/)


All pages passed all checks. 

![css validator results](static/readme/csstest2.PNG)

### **JavaScript**

I checked the script.js file using [JSHint](https://jshint.com/).

Same as on HTML Validation I have to chenck each js file. 

Only what coming is a few waring but I dont have error. 

![JS validator results](static/readme/JStest2.png)

### **Python**
I checked the app.py file using [PEP8 online](http://pep8online.com/)

The code passed all checks.

---
---

## Manually Testing Functionality

I manually checked all of the browsers specified.

### **Registration**

For registration, you are not able to create an account if you don't fill the file correctly which means that you have to fill in your first name, last name and as well correct email address. When you registered correctly, the administrator can see your user name and ID on MongoDB.

<img src="test/registertest.PNG" />

[Registration](static/readme/test/registertest2.PNG)

[Registration](static/readme/test/registertest3.PNG)

[Registration](static/readme/test/registertest4.png)

[Registration](static/readme/test/reg5.PNG).


### **LogIn and LogOut**

<img src="static/readme/test/login.PNG" />

As we can see you are not able to log in if you don't put the correct username and correct password.

<img src="static/readme/test/logouttest.PNG" />

As we can see you are not able to log in if you don't put the correct username and correct password.

### **Chempion Test**

On the add champion page, you can add your adult dog you have a form in which you add a picture, the title of the dog and his description. When you add your dog you will receive a notification that your dog has been successfully added as well as title pictures and a description are required.

<img src="static/readme/test/chempionaddtest.PNG" />

There is also the option to edit your champion, in this option you have the option to change the image, title and description of the dog. Also, only the account holder has the option to edit the dog.

<img src="static/readme/test/editch.PNG" />

Also, the account holder is able to delete the dog, but before deleting it, he will receive a notification if he is sure that he wants to delete the dog.

<img src="static/readme/test/chedelete2.PNG" />

<img src="static/readme/test/chedelete.PNG" />

### **Puppy Test**





















