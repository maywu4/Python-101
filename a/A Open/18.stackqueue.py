#stack
# teller = []
# teller.append('Greet Customer')
# print(teller)
# teller.pop()
# print(teller)
# teller.append('Process Deposit')
# print(teller)
# teller.append('Phone Ringing')
# print(teller)
# teller.pop()
# teller.append('Greet caller, listen, answer question')
# print(teller)
# teller.pop()
# print(teller)
# teller.pop()
# print(teller)

#queue
processor = []
processor.append({'type':'page', 'path':'','header':[],'cookies':[]})
processor.append({'type':'api', 'function':'', 'parameters':[]})
processor.append({'email':'email','address':'bob@gmail.com', 'subject':''})
print('PROCESSOR LIST', processor)

for i in range(len(processor)):
    item = processor.pop(0)
    print('PROCESSING ITEM', item)
    print('REMAINING LIST', processor)

