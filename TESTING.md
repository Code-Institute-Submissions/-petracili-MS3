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

<img src="static/readme/csstest2.PNG" />

![css validator results](static/readme/csstest2.PNG)

### **JavaScript**

I checked the script.js file using [JSHint](https://jshint.com/).

Same as on HTML Validation I have to chenck each js file. 

Only what coming is a few waring but I dont have error. 
<img src="static/readme/JStest2.png" />

![JS validator results](static/readme/JStest2.png)

### **Python**
I checked the app.py file using [PEP8 online](http://pep8online.com/)

The code passed all checks.

<img src="static/readme/pytest.PNG" />


---
---

## Manually Testing Functionality

I manually checked all of the browsers specified.

### **Registration**

For registration, you are not able to create an account if you don't fill the file correctly which means that you have to fill in your first name, last name and as well correct email address. When you registered correctly, the administrator can see your user name and ID on MongoDB.

<img src="test/registertest.PNG" />

<img src="test/registertest2.PNG" />

<img src="test/registertest3.PNG" />

<img src="test/registertest4.png" />

<img src="test/reg5.PNG" />

### **LogIn and LogOut**

<img src="test/login.PNG" />

As we can see you are not able to log in if you don't put the correct username and correct password.

<img src="test/logouttest.PNG" />

As we can see you are not able to log in if you don't put the correct username and correct password.

### **Chempion Test**

On the add champion page, you can add your adult dog you have a form in which you add a picture, the title of the dog and his description. When you add your dog you will receive a notification that your dog has been successfully added as well as title pictures and a description are required.

<img src=test/chempionaddtest.PNG" />

There is also the option to edit your champion, in this option you have the option to change the image, title and description of the dog. Also, only the account holder has the option to edit the dog.

<img src="test/editch.PNG" />

Also, the account holder is able to delete the dog, but before deleting it, he will receive a notification if he is sure that he wants to delete the dog.

<img src="test/chedelete2.PNG" />

<img src="test/chedelete.PNG" />

### **Puppy Test**

On the puppy page, we also have the option to add our puppies, with a few more options we have to fill out, picture, name, surname, hear-colour, date of birth and nationality or where the dog comes from. we are also able to edit puppies. as with the champion, we have the option of deleting that puppy, and only the account holder can do that.

<img src="test/addpuppytest2.PNG" />

<img src="test/pupyed.PNG" />

<img src="test/puppydelet.PNG" />

<img src="test/puppydelet2.PNG" />


### **Profile**

As we add champions or puppies, they will automatically appear on your profile, and you can also delete or edit them there.

<img src="test/profiletest.PNG" />

### **Search**

We are able to search champions or puppies by criteria (by name, nationality and gender).

<img src="test/srctest.PNG" />

### **Delete**

It is also possible to delete puppies or champions and when we press the delete button we get a notification if we are sure we want to delete the dog.

<img src="test/deletetest.PNG" />

<img src="test/delete2.PNG" />

<img src="test/chedelete.PNG" />

<img src="test/puppydelet.PNG" />

<img src="test/puppydelet2.PNG" />

### **Contact Us**

Page contact us servers so that the user can contact the administrator who will later connect him with the breeder, the idea is to maintain the privacy and security of breeders. While filling out the email form, enter first name last name and email is required as well, email is specified to be marked @

<img src="test/contest.PNG" />

<img src="test/testcon.PNG" />

<img src="test/conttest.PNG" />

<img src="test/contat3.PNG" />
























