# Cinemaniac Film Reviews | Portfolio Project 4 Full-Stack Toolkit

[Live Site](https://cinemaniac-blog.herokuapp.com/)

Cinemaniac is a movie review blog, for the movie lovers out there. Users come to read the reviews, create their accounts and join the community.
Come in and enjoy top-notch reviews of your favourite movies, drop a like or join a discussion about a movie or two.

![image of responsiveness](/media/img/responsive.jpg)

## User Stories

- As a Site User I can view all the posts so that I can pick one that I am interested in

- As a Site Admin I can add, read, edit and delete comment so that I have more creative control

- As a Site User I can leave comments on a post so that I can be involved in the conversation

- As a Site Admin I can safe posts as draft posts so that I can finish writing them later on

- As a Site User I can edit or delete my comments so that I have more freedom incase something was not meant to be posted

- As an Admin I can create, read, update and delete posts/reviews so that I can manage my own blog content

- As a Site User I can like or unlike a post so that I can interact with the content

- As a Site Admin I can add, read, edit and delete comment so that I have more creative control

- As a Site User I can register an account so that I can comment and like to feel a part of the community

- As a site user/admin or bystander I can view comments on an individual post so that I can read the conversation

- As a Site user/Admin or bystander I can view the number of likes on each post so that I can see which one is the most popular

- As a Site User I can click on a post so that I can read the full review

- As a Site User I can view a paginated list of reviews so that I can select which review I want to read

## UX

### Strategy

The target audience:

- 15+ years
- People with a love for film
- Community loving people
- Critics

Users look for good, honest reviews and a beautiful website to read them on. They want to be able to leave a comment on the review
but also give their own opinion on the movie. They also want to be able to leave a like if possible. That will make them feel included.

### Design

The Cinemaniac website have been designed by eye but also by sketches. It has been designed to be easily navigated, easily managed and beautiful.

### Databases:
PostgreSQL is used in this project and is hosted on [ElephantSQL](https://www.elephantsql.com/), which is providing the database url.

There is only one app for this project, called "blog" and it contains core functionality and the models.
The databases in the blog app consists of:

- Post, wich allows the admin to create update and delete the websites movie reviews and manipulate the database that way.
- Comment, which allows both admin and users to create their own comments on certain posts. The comments are saved to the database.

## Planning

For this project, I used my imagination and a sketchbook to paint up what I wanted the site to look like. And this is what my beautiful sketches look like:

Sketch for mobile landing page:

![sketch of mobile landing page](/media/img/sketch-landing.jpg)

Sketch for mobile post view:

![sketch for mobile post view](/media/img/sketch-mobile.jpg)

Sketch for desktop post view:

![sketch for desktop page view](/media/img/sketch-desktop.jpg)

## This is the results and features

### The Navbar

![navbar](/media/img/nav-bar.jpg)


Easily navigated navbar and it contains:
- brand/logo (takes you to home page)
- home button (takes you to home page)
- register button (takes to the registration page)

![navbar](/media/img/register.jpg)

- login button (takes you to the login page)

![navbar](/media/img/sign-in.jpg)

- for movie night button (Takes you to a form that sends you an email with movie suggestions)

![navbar](/media/img/movie-night.jpg)

For users that are logged in, the register and logout button are replaced with:
- Logout button (takes you to the signout page)

![navbar](/media/img/sign-out.jpg)





### Main window

The landing page consists of a inticing title that says "Your Film Review Blog", followed by the posts.
the page is very inviting and easy to look at. 

![landing page](/media/img/landing-page.jpg)

If you click on one of the posts it takes you to the post detail view.

![post detail](/media/img/post-detail.jpg)

On the bottom page of the post detail view you can see the comment section:
- comment section when unliked and not commented on

![comment section](/media/img/comment-section.jpg)

- when commented on and liked

![commented and liked](/media/img/comment-liked.jpg)

- footer which contains the links to social medias, Github, Linkedin and more

![footer image](/media/img/footer.jpg)

### Reasoning

My reasoning for this design was to make it look as inviting as possible, yet beautiful. And I think I capture that by using the background together with the gradient color as I did.
It makes you feel like you are in a movie environment. Cozy, warm and interesting.
The fonts I used for this project are Bangers and Gudea

## CRUD
- A registered user of the website can **C**reate, **R**ead, **U**pdate and **D**elete their own comments. And of course they can also read every other comment as well. but only edit or delete their own.

## Testing

I have tested responsiveness on the following devices and had family and friends test it for me as well:

Mobiles:

- Samsung Galaxy s21
- iPhone 13 pro
- iPhone 11
- Samsung Galaxy s22
- Samsung Galaxy a2
- Google Nexus

Browsers:

- Chrome
- Safari
- Opera
- Firefox
- Microsoft Edge

### Manual Testing

I wrote some automatic tests, the best I could but it could only cover about 50% of the content. So I did some manual testing to test the functions to see if there where any bugs.

Manual tests:

- You can't sign up unless you fill in all the forms. And when signed up, you are redirected to the home page and an alert comes up and closes after a couple of seconds (passed)

![signup](/media/img/register1.jpg)

![alert](/media/img/alert.jpg)

- You can't Log in unless you fill in all the forms. And when logged in, you are redirected to the home page and an alert comes up and closes after a couple of seconds (passed)

![signin](/media/img/sign-in1.jpg)

![alert](/media/img/alert.jpg)

- An alert comes up and closes after a couple of seconds after you've logged out (passed)

![logout](/media/img/logout.jpg)

- You can't comment unless you are logged in (passed)

![unaut-comment image](/media/img/unauth-comment.jpg)

- You can't sign up for movie suggestions if you're not logged in. (passed)

![unauth movie night image](/media/img/movie-night1.jpg)

- When Logged in, you can sign up for movie night, but not without filling in the form and only then will it send you an email.

![auth movie night image](/media/img/movie-night2.jpg)

![auth movie night image](/media/img/movie-night3.jpg)

- When logged in, you can comment, delete and edit comment. end an alert pops up when sucessful (passed)

![delete comment image](/media/img/delete-comment.jpg)

![delete comment image](/media/img/delete-comment1.jpg)

![edit comment image](/media/img/edit-comment.jpg)

![edit comment image](/media/img/edit-comment1.jpg)

### Validator Testing

I checked my code on the on the following sites:
- My CSS code on [Jigsaw](https://jigsaw.w3.org/css-validator/#validate_by_input) and it passed.
- My HTML code on [W3](https://validator.w3.org/) and it passed.
- My JavaScript code on [BeautifyTools](https://beautifytools.com/javascript-validator.php) and it passed.
- Also ran my Python code through Code Institute own [PEP8](https://pep8ci.herokuapp.com/) and it passed.

## Fixed and Unfixed bugs

Fixed:
- A bug where my form page for movie night was not rendering. I discovered my changing the url path to 'contact' instead of 'suggestions' (which I had), it worked.

Unfixed:
- A bug where after editing a comment, you are not redirected to the post view. And if you update the page, your comment is edited again. I tried to find a solution for this but was unsuccessful.
- The email form used by Javascript on the movie_suggestions url has a bug, where anything can be filled out and it will send an email. I did not have time to fix this, cause of my deadline. But I will in the future.

## Technologies I've used:

- I used Python to write my functions and models

- Django is the framework used to build project and its apps

- Cloudinary has been used to store my images and static files

- Crispyforms has been used to easily display forms

- Github Has been to store and plan project

- Gitpod my choice of IDE

- PostgreSQL Database

- Pep8 has been used for formatting and error-checking python-code

- JavaScript for the Email form

## Features left to implement

- Redirect of view after editing comment
- liking and commenting on others comments
- sorting movie reviews by genre, most likes, newest etc
- add a profile

## Deployment

The site was deployed using Heroku, following the steps offered by Codeinstitute.

Heroku:

- Create an account with Heroku
- Create a new app whilst logged in
- Add Buildpacks 'Python' and 'NodeJS'
- Connect your GitHub repository via "Connect to GitHub"
- Set up your config vars.
- Enable either "Automatic Deploys" or do it manually.
- Using Cloudinary and how to set it up can be read here, as well as in the above document. [here](https://devcenter.heroku.com/articles/cloudinary)

## Credits

- Credits to [Hero Patterns](https://heropatterns.com/) for supplying the free-to-use background
- Credits to [WallpaperAccess](https://wallpaperaccess.com/) for the post images. (They are free to use as long as there is no revenue gained from using them)
- To [TinyPNG](https://tinypng.com/) for compressing the images I've used.
- To my mentor Antonio for helping me understand certain things about Django.
- To the [Django documentation](https://docs.djangoproject.com/en/4.1/) for being my go-to during this project.
- To [IGN Nordic](https://nordic.ign.com/) for the film reviews (copy/paste)
- To [EmailJS](https://www.emailjs.com/) for the Javascript to send emails to users.

















