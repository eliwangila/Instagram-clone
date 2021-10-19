## Instagram

## Author
- Created by **Eli Wangila** on 19/10/2021

## Description
This is an Instagramclone where;

Users would like to:

1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

## Behaviour Driven Development (BDD)

| Behaviour | Input | Output |
| :-----------------| :-----------------: | ------------------: |
| Admin Authentication | On demand | Access Admin dashboard |
| User Authentication | On demand,Verify emails before proceeding | Access Admin dashboard |
| Display all images with comments and likes | Home page | Clickable links to open any images in a model |
| Display single images on model | On click | All details should be viewed |
| To add an image | Through Admin dashboard and homepage | Click on add and upload respectively |
| To edit image | Through Admin dashboard | Redirected to the image form details and editing happens |
| To delete an image | Through Admin dashboard | click on image object and confirm by delete button |
| To search | Enter text in search bar | Users can search by username |
| View other users profiles via story menu bar | Click username on stories navigation | Users can view all images posted by any user |
| Comment on images | Add comments below respectively image | Users can add comments on any image |
| Like images | Add likes to an image | Users can add likes to images they like |

## Setup | Installation Requirements

1. python-3.8.12
2. virtualenv
3. requirements.txt
4. django 3.2.8

## Cloning

* Open Terminal {Ctrl+Alt+T}

```
https://github.com/eliwangila/Instagram-clone.git
```
```
$cd instagram-clone
```

* open based on the text editor you have.

## Running the Application

* Creating the virtual environment

 ```
$ pip install --user pipenv
```

```
$ pipenv shell
```

$ curl https://bootstrap.pypa.io/get-pip.py | python

* Install Django Dependencies

```
$ pip install -r requirements.txt
```

## Setup Database

* Setting up your Database 

```
Name:
User:
Password:

```
## Now migrate

```
$ python manage.py makemigrations
```

```
$python manage.py migrate
```

* To run the application, in your terminal:

$ python manage.py runserver

## Technology used

* django3.2.8 and postgresql
* HTML5
* CSS
* Bootsrap
* python3.8.12

## Known Bugs

- Functionality for follow and unfollow , notyet fully implemented.
## Contact  Information

 Feel free to contact me incase of any issue or questions, ideas and concern towards the same.

- Reach out to me via EMAIL:[ekirapaeli254@gmsil.com]()
## Lisence
 - MIT Lisence:
 - Copyright (c) 2021 **Eli Wangila**