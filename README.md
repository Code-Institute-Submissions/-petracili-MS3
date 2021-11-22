<h1 aligin="center">KingBull the Bulldog</h1>

Code Institute Diploma in Full-Stack Software Development Project 3

##### <u>Project name:</u>KingBull the Bulldog

<img src="assets/readme/display.PNG" />

You can find the live site [here](https://aqueous-basin-06126.herokuapp.com/)

## Contents
+ [User Experience](#user-experience)
  + [User Stories](#user-stories)
  + [Design](#design)
    + [Overall Feel](#overall-feel)
    + [Colour Scheme](#colour-scheme)
    + [Imagery](#imagery)
+ [Wireframes](#wireframes)
+ [Features](#features)
  + [Current Features](#current-features)
  + [Possible Future Features](#possible-future-features)1. [Testing](#testing)
+ [Database](#database)
+ [Technologies Used](#technologies-used)
  + [Languages](#languages)
    1. [Github Pages](#github)
+ [Testing](#testing)
+ [Deployment](#deployment)
  + [Deployment through GitHub Pages](#deployment-through-gitHub-pages)
  + [Forking the Repository](#forking-the-repository)
  + [Cloning Project](#cloning-project)
+ [Credits](#credits)
  + [Content](#content)
  + [Media](#media)
  + [Acknowledgements](#acknowledgements)


# User Experience
## User Stories
### As a casual user: 
+ I want to be able to view dog without having to register and account. 
+ I want to be able to search for specific dog. 
+ I want to be able to search for dog that have a specific name,nationaliti and gender.
+ I want to have the option to register an account if I want to delete or edit your dog. 
### As a returning user: 
+ I want to be able to log into my account.
+ I want to be able to upload a dog. 
+ I want to be able to add a dog.
+ I want to have ease of access to any dog that I have already uploaded.
+ I want to  be able to edit or delete any dog that I have already uploaded.
### As the site owner/admin:
+ I want to be able to add new collections to the site.
+ I want the new collection to be added to the appropriate site areas.
+ I want to be able to delete any collections.

## Design
### Overall Feel

For this project I wanted to have a light colors, the reason for choosing colors is that English bulldogs with their appearance look very scary but their personality is the opposite of appearance and are known if very gentle dogs regardless of their ugly past. 

### Colour Scheme

Because the overall theme is light pink, I wanted to go with Materialize color palet because we already use that library. I found the perfect colour scheme in a [Materialize: Documentation](https://materializecss.com/color.html).

### Imagery

Imagery is an important part of the user experience. Any user that uploads dog has to accompany it with an image. And when browsing the adolt dog and puppy, this image is the main selling point of the dog so it's the prominent feature of the dog card. 

Another visual element is the banners on the dig and puppy pages. One some of them, a dog image was best. But for others, a visual element that evoked a feeling was more appropriate. If this site were going into full dog info, the site owner/admin would be in charge of this. 

Lastly is the light color. It ties into the nice personality od that personality of a particular breed.

In situation where pictures was to big kvalitet I was using [TinyPNG](https://tinypng.com/).

#### **Wireframing**

###### Home Page 

<img src="assets/readme/first.PNG" />

> Navigation bar at the top of the page,big Logo on the middle and small text below the logo.
> The home page has a few parts with text. About the Breed, History and Important info around circular images of bread.
> And Footer part on the end with icon for different social network.

--------------------------

###### Champion Page 

<img src="assets/readme/CHAMPION.PNG">

> Champion part has same navigation, logo and smala text under logo.
> The difference is that this page has 6 pictures of dogs. Each dog have a description below pictured.

--------------------------

###### Puppy Page 

<img src="assets/readme/PUPPY.PNG">

> Pupppy part has same navigation, logo and smala text under logo.
> The difference is that this page has 6 pictures of puppy. Each dog have a description below pictured.

---------------------------

###### Contact Page 

<img src="assets/readme/contact.PNG">

> Contact Page have form for send email.

---------------------------
# Features
## Current Features
### **Navigation menu displayed across all pages**

The navigation menu will help the user move easily across all pages. For the chempion pages, there is a dropdown menu in which all of those pages are held. This stops the navigation from becoming too cluttered. 

The navigation buttons update depending on whether a user is logged in, and whether that user is the admin:

| Nav Link              |Not logged in  |Logged in as user|Logged in as admin
|:-------------         |:------------- |:------------- |:------------- |
|Logo(back to home)     |&#9989;        |&#9989;        |&#9989;
|Champion               |&#9989;        |&#9989;        |&#9989;
|Pupy                   |&#9989;        |&#9989;        |&#9989;
|Manage Your Dog        |&#10060;       |&#9989;        |&#9989;
|Account                |&#10060;       |&#9989;        |&#9989;
|Log Out                |&#10060;       |&#9989;        |&#9989;
|Register               |&#9989;        |&#10060;       |&#10060;
|Log In                 |&#9989;        |&#10060;       |&#10060;

-----------------

### **All dogs accessible to users who don't want to make an account**

As someone who doesn't particularly like to sign up to websites that I don't plan on adding to but like to view, I wanted to to contact breeders for buy puppy or breed his bulldog they are have first contact us and then we will contanat them with breeders. I chose such content because of the better privacy of users and growers.  

### **Users can search for dog and puppy based on either key words**

Searching by name,nationality or gender is an important feature for any dog or puppy website so that was something that I wanted to include. But people who are familiar with that breed in general might be looking for a specific dog based on name so this was also included in the search criteria.

### **Pagination on chempion or puppy pages**

At the moment, the database is relatively small. But if this were site that was going into full production, the champion and puppy list would be much more extensive. As a result, the number of chempion or puppy displyed to the user could become overwhelming very quickly. I've not limited to number of chempion or puppy, reason of that is where people can contact different breeders and in that way they can learn more about the breed and also exchange experiences with other breeders of this breed of dogs.

### **User account management**

Anyone is able to make an account through the 'Register' page. They have to choose a username and a password. Measures have been put in place so that the user cannot choose a username that is already taken and they cannot use just whitespace.

Once their account is made, they will be able to log in an out when needed. 

### **User dog management**

A registered user is able to upload chempion or puppy to the site. Once they have chempion or puppy that they have added, all chempion or puppy management can be done from their account page. This includes editing a deleting. I decided to keep these features exclusive to the account page rather than accessible on the chempion or puppy or collections pages. I like the uniformity of this. 

  + **Uploading**: when uploading, there are form validations in place that the user needs to adhere to. The two most important are: 
    + The user cannot leave any inputs blank
    + The user cannot use just whitespace. 

  + **Editing**: the user will have to go into the edit page through the chempion or puppy, make the necessary changes and confirm them at the bottom of the page. The user also has the option to cancel all changes. These steps assure that the user cannot do any of this by mistake. 

  + **Deleting**: there is a confirmation modal in place to assure the user doesn't accidentally delete the chempion or puppy. 

  ### **Chempion or puppy Images**

When uploading a chempion or puppy, the user needs to add an image alongside the chempion or puppy information. This image will be used on both the chempion or puppy card and on the full chempion or puppy page. But because the image is added via a url, there are some people who wither don't was to go to the rounds of finding one, or they simply can't on their device. iOS doesn't allow the user to copy an image url in the same way most android do. Because of that I have added a placeholder image url that the user can use in place of their own. It's a stylish image that was found on [Unsplash](https://unsplash.com/) that looks good with the overall feel of the site. 

### **Adding to chempion or puppy**

When uploading a chempion or puppy, the user is required to add their chempion or puppy to at least one collection(chempion or puppy). This allows the user to feel like they're adding to the community in a more thoughtful way. This also takes the responsibility of curating the collections off the owner/admin. 

### **Admin 'Collections' management**

Only the admin can manage the collections pages. This includes adding, editing and deleting. The site has been designed so that the admin only has to use the collections management page to create a new collection at this will automatically be updated on the carousel. Any edits or deletions to collections will also apply to those elements. 

## Possible Future Features
+ A rating system that allows users to rate each others chempion or puppy. 
  + This could lead to sorting by top-rated chempion or puppy.
+ Ability to 'save' chempion or puppy to a users own account to refer back to.
+ Ability to upload a saved image to their chempion or puppy rather than relying on a URL.
+ Users ability to update username. 
+ Users ability to delete their account. 
  + This could allow the user to either leave their chempion or puppy on the site or delete them along with the account 
+ Admin controlled 'featured' chempion or puppy


---
---

# Database
## Categories
Belowe you can see categories for puppy:

| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |used in *puppy* array
|img                    |string         |url for the carousel image
|dob                    |string         |used for puppy date of birth
|first                  |string         |used for name of puppy
|gender                 |string         |used for gender 
|hair_color             |string         |used for color 
|last                   |string         |used for last name of puppy
|nationality            |string         |used for nationality of puppy


| Key                   |Value type     |Desc           |
|:-------------         |:------------- |:------------- |
|_id                    |ObjectId       |used in *chempion* array
|img                    |string         |url for the carousel image
|text                   |string         |used for name of chempion
|titule                 |string         |used for titule of chempion



# Technologies Used
## Languages
+ [HTML5](https://en.wikipedia.org/wiki/HTML5)
+ [CSS3](https://en.wikipedia.org/wiki/CSS)
+ [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+ [Python3](https://www.python.org/)

## Frameworks and Libraries
+ [Flask](https://flask.palletsprojects.com/en/1.1.x/)
+ [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
+ [Pip3](https://pip.pypa.io/en/stable/)
+ [dnspython](https://www.dnspython.org/)
+ [jQuery](https://jquery.com/)
+ [Flask Paginate](https://pythonhosted.org/Flask-paginate/)
+ [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
+ [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
+ [Materialize](https://materializecss.com/).
+ [FontAwesome](https://fontawesome.com/)
+ [Google Fonts](https://fonts.google.com/) 

## All Others
+ [Heroku](https://www.heroku.com/) used to deploy live site
+ [MongoDB](https://www.mongodb.com/) used to host database information.
+ [GitHub](https://github.com/) used to host repository.
+ [GitPod](https://www.gitpod.io/) used to develop project and organise version 
+ [Balsamiq](https://balsamiq.com/) used to create wireframes.
+ [CloudConvert](https://cloudconvert.com/) to convert all images to .webp format.
+ [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance review.
+ [Responsinator](https://www.responsinator.com/) used to check site was responsive on different screen sizes.
+ [Am I Responsive](http://ami.responsivedesign.is/) used to generate README intro image.
+ [Autoprefixer](https://autoprefixer.github.io/) used to make CSS cross-browser compatible.
+ [favicon.io](https://favicon.io/) used to create a site favicon.
+ [TinyPNG](https://tinypng.com/) used to host images.

---
---
# Testing
Due to the size of the testing section, I have created a separate document for it. You can find it [here](https://github.com/petracili/MS3/blob/master/TESTING.md). 

---
---
# Deployment

## Heroku Deployment
This project was deployed through Heroku using the following steps:

### Requirements and Procfile
Heroku needs to know which technologies are being used and any requirements, so I created files to let it know. Before creating the Heroku app, create these files using the following steps in GitPod: 
+ In the GitPod terminal, type ```pip3 freeze --local > requirements.txt``` to create your requirements file.
+ In the GitPod terminal, type ```echo web: python run.py > Procfile``` to create your Procfile.
+ The Procfile needs to contain the following line: ```web: python app.py``` and make sure there is no additional blank line after it. 
+ Push these files to your repository.

### Environmentals File

Create and env.py file using the following information:

```
import os
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", " *unique secret key* ")
os.environ.setdefault("MONGO_URI", " *unique uri from mongo.db * ")
os.environ.setdefault("MONGO_DB", " *database name* ")
```

Because this contains sensitive information, this needs to be added to the '.gitignore' file. 

### Creating Heroku App
+ Log into Heroku
+ Select 'Create New App' from your dashboard
+ Choose an app name (if there has been an app made with that name, you will be informed and will need to choose an alternative)
+ Select the appropriate region based on your location
+ Click 'Create App'
### Connecting to GitHub
+ From the dashboard, click the 'Deploy' tab towards the top of the screen
+ From here, locate 'Deployment Method' and choose 'GitHub'
+ From the search bar newly appeared, locate your repository by name
+ When you have located the correct repository, click 'Connect'
+ DO NOT CLICK 'ENABLE AUTOMATIC DEPLOYMENT': This can cause unexpected errors before configuration. We'll come back to this
+ Click the 'Settings' tab towards the top of the page
+ Locate the 'Config Vars' and click 'Reveal Config Vars'
+ Use the following keys and values which must match the key/value pairs in your env.py file:

| Key           | Value               |
| ------------- |:--------------------|
| IP            | 0.0.0.0             |
| PORT          | 5000                |
| SECRET_KEY    |*Secure secret key*  |
| MONGO_URI     |mongodb+srv://root:*PASSWORD*@myfirstcluster.dr4g1.mongodb.net/myFirstDB?retryWrites=true&w=majority |
| MONGO_DBNAME  |myFirstDB            |
|               |                     |

+ Go back to the 'Deploy' tab and you can now click 'Enable Automatic Deployment'
+ Underneath, locate 'Manual Deploy'; choose the master branch and click 'Deploy Branch'
+ Once the app is built (it may take a few minutes), click 'Open App' from the top of the page

## Forking the Repository
+ Log in to GitHub and locate the GitHub Repository
+ At the top of the Repository above the "Settings" Button on the menu, locate the "Fork" Button.
+ You will have a copy of the original repository in your GitHub account.
+ You will now be able to make changes to the new version and keep the original safe. 
## Making a Local Clone
+ Log into GitHub.
+ Locate the repository.
+ Click the 'Code' dropdown above the file list.
+ Copy the URL for the repository.
+ Open Git Bash on your device.
+ Change the current working directory to the location where you want the cloned directory.
+ Type ```git clone``` in the CLI and then paste the URL you copied earlier. This is what it should look like:
  + ```$ git clone https://github.com/petracili/MS3```
+ Press Enter to create your local clone.

**NB:** In order to work with a clone of this project, you will need to create the env.py file using your own variables and create a MongoDB database matching the one documented in the [Database section](#database) of this doc. 

You will also need to install all of the packages listed in the requirements file you can use the following command in the terminal ```pip install -r requirements.txt``` which will do it for you. 

---
---

# Credits
## Code

+ REGEX pattern for form input validation taken from this [Stack Overflow post](https://stackoverflow.com/questions/13766015/is-it-possible-to-configure-a-required-field-to-ignore-white-space).

+ The HTML back button was taken from this [W3Schools page](https://www.w3schools.com/jsref/met_his_back.asp).

+ I used [this Stack Overflow post](https://stackoverflow.com/questions/50394358/materializecss-vertically-offset-dropdown-menu-content/50395102) to adjust the placement of the nav bar dropdown.

+ This code for [materialize slider autoplay](https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay) was taken directly (also credited in in js file).

+ My own neon text css classes taken from [this article](https://css-tricks.com/how-to-create-neon-text-with-css/) and re-worked for my neon boxes (also credited in in css file).

+ [This demo](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) was used to understand how to incorperate flask pagination into my pre existing code.

+ [This Stack Overflow post](https://stackoverflow.com/questions/27992413/how-do-i-calculate-the-offsets-for-pagination/27992616) helped me gain more of an understanding of pagination offset.

+ [This Stack Overflow post](https://stackoverflow.com/questions/27980121/pylint-warning-possible-unbalanced-tuple-unpacking-with-sequence) helped with the Pylint warning that I was getting and provided the comment to override it.

+ I used the code in this [W3Schools post](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp) to create the scroll-to-top button.

+ I took the JS code from this [Stack Overflow post](https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay) for the carousel autoplay functionality.

### Test Dog

+ I searched for certain dogs with the help of a breeder I know privately, and in a conversation with him I checked the validity of the pedigree of a certain dog.


#### Adding Email JS 

Adding this functionality to a website was covered in the Interactive Frontend Development module of the course. Those few videos were a great help. Firstly you have to be registered to this service then you will be able to link it with an existing email address. The official EmailJS documentation is also crucial to understand what has to be done in order to get everything in working order. You can find the documentation [here](https://www.emailjs.com/docs/introduction/how-does-emailjs-work/).

# <a name="Testing"></a> Testing
### Testing write-up

HTML code validated on - https://validator.w3.org/

CSS code validated on - https://jigsaw.w3.org/css-validator/

- Upon sending a message through the contact form, the site visitor will receive an automated email response to the email address they have provided previously in the form. I Tested this functionality on my email accounts. The right is the email provided while filling the form. This has got the automated message after clicking send.

<img src="assets/readme/testing.PNG" />

A member of Code Institute Anna Greaves has mentioned this handy tool in her ["How to README.md"](https://www.youtube.com/watch?v=7BteidgLAyM&feature=youtu.be&ab_channel=CodeInstitute) online webinar.




### Credits

***Antonio Rodrigez*** - My mentor at Code Institute - for general feedback and guidance, special guidance on DataBase

***Matt Rudge*** - Lecturer/Developer at Code Institute - for the [template](https://github.com/Code-Institute-Org/gitpod-full-template) used with GitPod IDE for developing this project, and the lecture on Email JS

***Anna Greaves*** - Developer at Code Institute - for the ["How to README.md"](https://www.youtube.com/watch?v=7BteidgLAyM&feature=youtu.be&ab_channel=CodeInstitute) webinar
