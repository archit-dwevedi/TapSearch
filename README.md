# TapSearch
TapChief &lt;> Coding Challenge for Tech Internship

You are to build a simple program called TapSearch that achieves these objectives.
 - It takes in multiple paragraphs of text, assigns a unique ID To each paragraph and stores the words to paragraph mappings on an inverted index. This is similar to what elasticsearch does. This paragraph can also be referred to as a ‘document’
 - Given a word to search for, it lists out the top 10 paragraphs in which the word is present


Few points to consider
- Tokenize to words by splitting at whitespace
- Convert all words to lowercase
- Index these words against the documents they are from
- Generate a unique ID for every document that is index
- A paragraph is defined by two newline characters


# Installation

Follow the Steps as Given Below for Ubuntu 

- sudo apt-get install python3-pip (Install PiP)
- sudo pip3 install virtualenv (Installing Virtual Environment)
- virtualenv venv (Creating New Virtual Environment "venv")
- cd venv (Changing Directory to Newly Created Virtual Environment)
- source bin/activate (Activating the Virtual Environment)
- sudo pip3 install django (Installing Django using PIP)
- git clone https://github.com/arch888/TapSearch (Cloning the Repo)
- cd TapSearch (Chaging Directory to TapSearch)
- pip3 install -r requirements.txt (Installing all the Requirements)
- python3 manage.py migrate (Migrating the Database)
- python3 manage.py runserver (Running Local Server)

For Intallation on Windows follow the Tutorial
 - https://docs.djangoproject.com/en/2.2/howto/windows/

# Usage

You can Upload the Text for Searching of the Words in Text Format (From the Text Field)
From the File Field with multiple Files 

You can clear the DataBase which is given on the homepage.

You can Search for the Words in the letter by letter and also by word.

Sample Images of the Project can be found here.
https://drive.google.com/open?id=1hwe9fVAcxCdiYEBhMxC4QRKmRk6Kta3Y


# Website is Hosted at  - https://bit.ly/TapSearch
