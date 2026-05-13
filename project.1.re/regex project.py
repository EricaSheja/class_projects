import re                     
import xml.etree.ElementTree as ET

tree = ET.parse('/Users/apple/Downloads/modified_sms_v2.xml')   
root = tree.getroot()                   

received_pattern  = re.compile(r'You have received ([\d,]+) RWF')

transferred_pattern = re.compile(r'\*165\*S\*([\d,]+) RWF')

total_received    = 0    
total_transferred = 0    

received_list    = []    
transferred_list = []    

for sms in root.findall('sms'):      
    body = sms.get('body', '')        
                                      
    match = received_pattern.search(body)   
    if match:                               
        amount_str = match.group(1)         
        amount_str = amount_str.replace(',', '') 
        amount = int(amount_str)          
        total_received += amount           
        received_list.append(amount)     

    match = transferred_pattern.search(body)
    if match:
        amount_str = match.group(1)
        amount_str = amount_str.replace(',', '')
        amount = int(amount_str)
        total_transferred += amount
        transferred_list.append(amount)

print("RECEIVED MONEY")
print(f"Number of times money was received: {len(received_list)}")
# len() 
print(f"Total received: {total_received:,} RWF")

print()  

print("TRANSFERRED MONEY")
print(f"Number of transfers out: {len(transferred_list)}")
print(f"Total transferred: {total_transferred:,} RWF")