from twilio.rest import Client

account_sid = "AC36bf4257da386c1870e16218be3dedee"
auth_token = "2a505c2787dec13cafa4e82952051c43"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+8613591150781",
    from_="+17479980610",
    body="hello")

'''
call = client.calls.create(
    to="+8613591150781",
    from_="+17479980610",
    url="hello")
'''
print(message.sid)
