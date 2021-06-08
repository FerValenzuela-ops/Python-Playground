from twilio.rest import Client 
 
account_sid = 'ACe18fe74bb7e3f282bb98607bbc5c45f1' 
auth_token = '6b1d28974d2fa997e5cbeaa2065c78a9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG530aade62c8959e044411a056d39c265', 
                              body='WOW!, this is working',      
                              to='+56945171370' 
                          ) 
 
print(message.sid)