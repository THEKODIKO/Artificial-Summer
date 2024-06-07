
from artificial_summer import *


instruction_prompt= "Instruction: You are Connor from 'Detroit: Become Human', and User is me and Connor is you. Just respond with your response and nothing else."

context= []
context.append(instruction_prompt)


while True:
  speech= recognize_speech()
  
  text= "User:"+speech
  
  context.append(text)
  
  _resp= ai_respond(context)
  
  if not _resp.startswith("Assistant:"):
    _resp= "Assistant:"+_resp
  
  context.append(_resp)
  print(context)

  _resp= _resp.split(":")[1]
  
  print(_resp)
  speak(_resp)