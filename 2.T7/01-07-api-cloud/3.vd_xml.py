import xml.etree.ElementTree as ET

xml = """
   <students>
       <student>
           <name>Nguyễn Văn An</name>
           <address>Hà Nội</address>
       </student>
       <student>
           <name>Nguyễn Thị Bình</name>
           <address>TP.HCM</address>
       </student>
   </students>
"""

root = ET.fromstring(xml)
for student in root:    
   name = student.find('name').text
   address = student.find('address').text
   print(name, address)