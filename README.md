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
1. [Credits](#credits)


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


#### Adding Email JS 

Adding this functionality to a website was covered in the Interactive Frontend Development module of the course. Those few videos were a great help. Firstly you have to be registered to this service then you will be able to link it with an existing email address. The official EmailJS documentation is also crucial to understand what has to be done in order to get everything in working order. You can find the documentation [here](https://www.emailjs.com/docs/introduction/how-does-emailjs-work/).

### **Version Control**

I used Git for version control and uploading the project to GitHub.
My GitHub repository for this project is accessible [here](https://petracili.github.io/MS2/).

# <a name="Testing"></a> Testing
### Testing write-up

HTML code validated on - https://validator.w3.org/

CSS code validated on - https://jigsaw.w3.org/css-validator/

- Upon sending a message through the contact form, the site visitor will receive an automated email response to the email address they have provided previously in the form. I Tested this functionality on my email accounts. The right is the email provided while filling the form. This has got the automated message after clicking send.

<img src="assets/readme/testing.PNG" />

A member of Code Institute Anna Greaves has mentioned this handy tool in her ["How to README.md"](https://www.youtube.com/watch?v=7BteidgLAyM&feature=youtu.be&ab_channel=CodeInstitute) online webinar.

### Deployment

 1. On GitHub, navigate to your site's repository.
 2. Under your repository name, click **Settings**.
 3. Under "GitHub Pages", use the **None** or **Branch** drop-down menu and select a publishing source.
 4. Optionally, use the drop-down menu to select a folder for your publishing source.
 5. Click **Save**.

### Cloning this repository

If you'd like to see and work on my code locally feel free to clone the repository. When you clone a repository, you copy the repository from GitHub to your local machine. 
1. On GitHub, navigate to the main page of the repository.
2. Above the list of files, click **Code**.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click . To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click **Use SSH**, then click . To clone a repository using GitHub CLI, click **Use GitHub CLI**, then click .
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type `git clone`, and then paste the URL you copied earlier.

   ```shell
   $ git clone gh repo clone petracili/MS3
   ```

7. Press **Enter** to create your local clone.

GitHub documentation on cloning repository includes other methods to using the console. You can read more [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### Credits

***Antonio Rodrigez*** - My mentor at Code Institute - for general feedback and guidance, special guidance on DataBase

***Matt Rudge*** - Lecturer/Developer at Code Institute - for the [template](https://github.com/Code-Institute-Org/gitpod-full-template) used with GitPod IDE for developing this project, and the lecture on Email JS

***Anna Greaves*** - Developer at Code Institute - for the ["How to README.md"](https://www.youtube.com/watch?v=7BteidgLAyM&feature=youtu.be&ab_channel=CodeInstitute) webinar
