# Rosie Maguire - She Codes News Project
## About This Project
This project uses HTML, CSS and the Django framework. It is a news website that allows users to read news stories, and authors to create them.

## Prerequisites
- `python`
- `pip`
- unrestricted execution policy (Windows requirement)
## How To Run This Code
- Clone a copy of this repo to your local machine. This can be done in the command line by navigating to the desired directory, then running:

        git clone https://github.com/rosiemaguire/django-project-she-codes-news.git
- Once you have a local version of this repository, you'll need to set up your virtual environment:
    -  navigate to the folder that contains the `requirements.txt` file
    - If you're on a windows machine, run the command 
            
            . venv/Scripts/activate
    - If you're on a mac, run the command 
            
            source venv/bin/activate
    - Install the Django library: 
            
            python -m pip install -r requirements.txt
    - Check installation was successful: 
    
            python -m pip freeze
    - Change directory to where manage.py is located:
            
            cd she_codes_news
    - Make the inital migrations:
        
            python manage.py migrate
    - Load the template data for the news articles by running these two commands:
            
            python manage.py loaddata users
            python manage.py loaddata news
    - Now with everything set up, you'll just need to run the server!

            python manage.py runserver
    - Open http://localhost:8000/news to view and interact with the website
    - When you're finished press CTRL+C to quit the server
    - Deactivate the virtual environment by either using the command `deactivate` or terminate your terminal session.

## Database Schema
![My ERD]( she_codes_news\images\ERD.png )
## Project Features
- [X] Order stories by date
    ![Latest stories ordered by publication date](she_codes_news/images/127.0.0.1_8000_news_1.png)
- [X] Styled "new story" form
    ![Add Story Form](she_codes_news/images/127.0.0.1_8000_news_add-story_.png)
- [X] Story images
    ![Correct Image attached to full story view](she_codes_news/images/127.0.0.1_8000_news_1_.png)
- [X] Log-in/log-out
    ![Log In Screen](she_codes_news/images/127.0.0.1_8000_users_login_.png)
    ![Reset Password Screen](she_codes_news/images/127.0.0.1_8000_users_password_reset_.png)
- [X] "Account view" page
    ![Account View](she_codes_news/images/127.0.0.1_8000_users_2_.png)
- [X] "Create Account" page
    ![Create Account Page](she_codes_news/images/127.0.0.1_8000_users_create-account_.png)
- [X] View stories by author
    ![Search articles by author](she_codes_news/images/127.0.0.1_8000_news_search_.png)
- [X] "Log-in" button only visible when no user is logged in/"Log-out" button only visible when a user *is* logged in
    ![Log in button visible when no one logged in](she_codes_news/images/127.0.0.1_8000_news_.png)
- [X] "Create Story" functionality only available when user is logged in
    ![Write New Story in Nav bar when logged in](she_codes_news/images/127.0.0.1_8000_users_password_change_.png)
## Additional Features:
- [ ] Add categories to the stories and allow the user to search for stories by category.

- [ ] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).

- [ ] Add the ability to “favourite” stories and see a page with your favourite stories.

- [X] Our form for creating stories requires you to add the publication date, update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to showwhen the story was updated).
    ![Add Story Form](she_codes_news/images/127.0.0.1_8000_news_add-story_.png)
- [ ] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.

