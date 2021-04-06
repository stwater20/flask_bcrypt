# flask_bcrypt

Because there seems to be some errors in the official documents, a demo that can run normally is implemented here.

### how to use
---
<code>
  conda install --file requirements.txt
</code>
or 
<code>
  pip install -r requirements.txt
</code>
<br>

  
    python crypt.py
    


#### encrypt - Methods => POST
---



    http://{your_ip:port}:encrypt
  

    data:{put_your_key}


response String -> $2b$12$D593RvtunfXMQG1aPxxvqecu5VJDqvxr.tWDLCHftaPPyMeYv.7wy

![alt text](encrypt.png "Title")
  
#### decrypt - Methods => POST
---


    http://{your_ip:port}:encrypt
  

    data:{put_your_key}


response
  String -> True or False 
  
![alt text](decrypt.png "Title")  
License
---
MIT
