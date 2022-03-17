from linkedin import LinkedIn
email = "test@mail.com" 
password = "test" 
target_profile = "https://www.linkedin.com/in/alexandrarynne/" 
client = LinkedIn()
if client.login(email, password):
    
    
    print(client.singleScan(target_profile))
    
else:
    print("Login Failed, please recheck login credentials")
