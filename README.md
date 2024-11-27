Welcome to the Chat Application, a Python WebScoket project by Grant Copeland!

First, you need to clone down the project using this command here:

    git clone git@github.com:gcland/Chat_Application-Mod15-Mini-Project.git

Next, enter the following commands into the terminal:

    python3 -m venv myenv
    source myenv/bin/activate
    pip install flask flask-socketio

Then, make sure your interpretter is in the virtual environment we just created:

> cmd + shift + p (mac)
> 	-> select virtual environment

Navigate to the 'app.py' file and run the file.
Open the localhost url (http:.//127.1.0.0:5000). This will navigate you to a 'waiting room / lobby' with a link to the chat room. Click the link to join the chat room.
This sends you to the chat room. Enter text into the form and submit to display your text to other chat participants. 
To simulate other participants, open another tab from the localhost url and join the chat room. From the second tab, the messages previously sent from the first tab will not appear.
Send messages (from either the first or second tab) and all particpants in the chat room will be able to view the messages.

Thanks for viewing this project!

- Grant
