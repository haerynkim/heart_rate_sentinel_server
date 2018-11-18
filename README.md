# heart_rate_sentinel_server
Access and write to a database.

This repository has one server code named api.py and various client functions that act on the server. The host address is vcm-7474.vm.duke.edu, and this is already coded into the URLs of all client functions. Each client function corresponds to each get or post request, but they may return different values or print statements. For example, posting a new patient may return the database to which the new patient's information was posted.

I did not use mongoDB. I have a database that each get and post request writes to using the add_to_database function in the main server code. It is a list of dictionaries that should have one dictionary corresponding to one patient ID.

Sendgrid does not work in the current state of files on the master branch. The send_email.py function, an isolated sketch that is not integrated into the code, works as I mentioned in issue #7. The send_email function in the main server sketch, api.py, also works as I mentioned in issue #7. However, I could figure out a way to make the sketch send an email without having to enter the following two command lines:
<br/>1: /Applications/Python\ 3.7/Install\ Certificates.command
<br/>2: export SENDGRID_API_KEY='<my Send Grid key>'
<br/> One thing to note is this send_email function is inside the post request function that puts up a patient's heart rate. Thus the HTTP Error (401 unauthorized), makes the server crash. The sendgrid code has some internal exception so I could not program in another exception so the code does not terminate gracefully, but the rest of the function continues to work.
<br/> So this sketch, integrated into api.py assuming that it is in working state, is in another branch called email. I would git pull master while you're on this branch to your local machine, because the master branch on remote origin would be ahead by a few commits as things are.
  
  Have a good time!
