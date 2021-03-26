# The Chariot Code

The code for a team called "The Chariot". Do not steal please


### Folder structure

```
NAMEOFPROGRAMMER:
      /.
      /..
      /binarydecoder # or whatever the program is called
          /.
          /..
          /*.py
```

Then, notes go in the "notes" directory

More can be added as see fit 

### How to git

Afraid of messing up? I created a branch called "tutorial" that can be all willy nily with commits and the like to get prepared for uploading to the branch main

To switch inbetween the two, use the following command
```bash
git checkout tutorial # mess around here
# OR 
git checkout main # this is where the serious coders lie
```

To get the latest information
```bash
git pull -ff-only origin BRANCH # main or tutorial. Whichever branch needs to be updated 
```

To add to the code in the command line,
```bash
cd ~/SOMEWHERE-RESPONSIBLE-TO-DOWNLOAD-THE-CODE/
git clone https://github.com/KevOub/the-chariot-code.git
cd the-chariot-code
ls # check your name is not present in the repo yet
mkdir YOURNAME
cd YOURNAME
mkdir binarydecoder # the first program, for example
cd binarydecoder
cp WHEREVER-YOUR-CODE-IS/*.py . # copies all of your python files to the current directory
git status # should see your modifications
cd ../.. # go up two levels (or however deep you went) to the root directory of this repository
# this is the git command line stuff
git config --global --edit # sets the username and the email associated with your github account
git add .
git commit -m "Hello World" # whatever your message should be
git push origin main # this should ask for your login info. If it ran correctly, it should tell you so
# github will then update with your hardwork
```

Fancy public/private key so you do not need to login to `git push`
https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh

You *can* do the above stuff in github like so.

1) Find the green button that says code
2) To the right of that, there should be an add file. Select "Create New File"
3) According to this stack overflow [answer](https://stackoverflow.com/questions/12258399/how-do-i-create-a-folder-in-a-github-repository), you just add DIRECTORY/main.py to create a directory with main.py inside
4) So, when creating YOURNAME you have to create a full path to a python file for all the folders to work  [I.E., /YOURNAME/binarydecoder/main.py creates the YOURNAME and binary decoder files]
5) The large text box with the lines is where your code goes
6) The text box below it is the commit message
7) When you are done with all the above for uploading a file, click the green "Commit Changes"
