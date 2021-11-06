<h1 aligin="center">KingBull the Bulldog</h1>

Code Institute Diploma in Full-Stack Software Development Project 3

##### <u>Project name:</u>KingBull the Bulldog

<img src="assets/readme/homepage.PNG" />

### View the live project: https://aqueous-basin-06126.herokuapp.com/

## Contents
1. [Summary](#summary)
1. [UX](#ux)
    1. [Strategy](#strategy)
    1. [Scope](#scope)
    1. [Structure](#structure)
    1. [Skeleton](#skeleton)
    1. [Surface](#surface)
1. [Features](#features)
    1. [Features left to implement](#left-to)
1. [Testing](#testing)
1. [Deployment](#deployment)
    1. [Github Pages](#github)
1. [Credits](#credits)


# <a name="summary"></a> Summary
This is page is created to help new owners how bread need to look and what is best for them.

It provides a database of pictures of different dogs which can be searched, viewed, added to, removed from and edited.


# <a name="ux"></a> UX
## <a name="Strategy"></a> Strategy
### **New site user's goals:**
* As a new site user, I want to be able to browse and search for dog 
* As a new site user, I want to be able to understand the intent of the page
* As a new site user, I want I want to understand easily how to navigate the page and access the facilities provided
### **Returning user's goals**
* As a returning site user, I want to be able to log in
* As a returning site user, I want to be able to view my dog
* As a returning site user, I want to be able to edit and delete my dog
* As a returning site user, I want to be able to add new dog
### **Site owner'as goals:**
* As a site owner, I want dogs added via the site to be stored in the correct format in the database
* As a site owner, I want to be able to see who has added each dog

## <a name="scope"></a> Scope
**Functional requirements:**
#### For ease of use:
* Navigation bar which is simple and easy to navigate
* A search Function
#### To ensure the database is up to date and editable:
* Function to add a dog
* Function to delete a dog


**Content requirements:**
#### To ensure the site is visually appealing and to draw the user's eye:
* Images of adolt dog and puppy
* Clear, crisp colours which do not detract from or make the text unreadable

### For usability
* For the time commitment to be clear as this is often a factor in a dog choice

## <a name="structure"></a> Structure
**Interaction design:**
* User friendly interface to ensure usability and to encourage the user to return
* Responsive and visible links which change on hover to provide user feedback as they navigate the site

**Information Architecture:**
* Navigation bar at the top of the page
* Footer at the bottom of the page - sticky to the bottom so it is only visible when the bottom of the page is reached
* Responsive navigation bar - adjusting for mobile for ease of use
* Responsive images to ensure they fit within the designated spaces, no matter what device is being used or the size of the screen
* All features appropriate size and responsive for mobile and desktop viewing
* All information is appropriate and relative to the subject and not misleading or hard to find

-----------------

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

#### **Colors scheme and typography**

 I have used the Noto Sans from Google Fonts. I have chosen the Noto Sans because it's handwriting calligraphy style for the title. Every other visible text is using Noto Sans.

 The site heavily relies on imagery so I wanted to find a balance between colors. I chose a light pink and white that is soothing and encourages creativity, which I think is a great choice for a page that focuses on a peopel's best friends.


-----------------

#### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


#### Frameworks, Libraries & Programs Used

- Google Maps Marker Clusterer
- Git Version Control 
- GitHub - to host the repository and the live site
- [Bootstrap](https://getbootstrap.com/) 
- [Email JS](https://www.emailjs.com/) - for making the contact form alive
- [FontAwesome](https://fontawesome.com/) - for the icons used
- [W3Schools Online Web Tutorials](https://www.w3schools.com) - for easier handling of codes
- [Animate.css](https://animate.style/) - for animating element on the landing page 
- [Google Fonts:](https://fonts.google.com/) - for font on webpage
- [HTML Color Codes:](https://htmlcolorcodes.com/) - for color codes and names
- Code Institute - for reminder of how the element is used
- [Grammarly](https://www.grammarly.com) - to correct grammar
- [MongoDB](https://en.wikipedia.org/wiki/MongoDB) - te create database and conect with gitpod
- [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
- [Materialize](https://materializecss.com/about.html)


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
