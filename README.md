# flask_bcrypt

### how to use
---
#### encrypt

<code>
  http://{your_ip:port}:encrypt
  
  form-data
    data:{put_your_key}
</code>

response String -> $2b$12$D593RvtunfXMQG1aPxxvqecu5VJDqvxr.tWDLCHftaPPyMeYv.7wy
  
#### decrypt

<code>
  http://{your_ip:port}:encrypt
  
  form-data
    data:{put_your_key}
</code>

response
  String -> True or False 
  
  
