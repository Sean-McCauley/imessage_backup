import sqlite3
import time

# 1. Read in chat.db
connection = sqlite3.connect("chat.db")

# Query data needed 
cursor = connection.execute("""
  SELECT           
    c.chat_identifier, 
    c.display_name, 

    h.id,

    a.guid,
    a.filename, 
    a.transfer_name,   
    a.created_date,    
    a.mime_type,      
    a.total_bytes,      
    a.is_outgoing,     
        
    m.text,           
    m.handle_id,       
    m.service,        
    m.date,           
    m.is_from_me,             
    m.associated_message_guid, 
    m.associated_message_type,

    m.guid,    
    m.reply_to_guid,   
    m.thread_originator_guid   

  FROM message AS m
  LEFT JOIN message_attachment_join AS maj ON maj.message_id = m.rowid
  LEFT JOIN attachment AS a ON attachment_id = a.rowid
  LEFT JOIN chat_message_join AS cmj ON cmj.message_id = m.rowid 
  LEFT JOIN chat AS c ON cmj.chat_id = c.rowid
  LEFT JOIN handle AS h ON m.handle_id = h.id
""")
  

# Extract Data: only worry about formatting data that is collected.
data = cursor.fetchone() 

# for record in cursor:
#   pass






connection.close()













# 2. Go through returned data
# 3. Proccess data
# 4. Create new database
# 5. Add data to new database
