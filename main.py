import sqlite3

# 1. Read in chat.db
connection = sqlite3.connect("chat.db")
cursor = connection.cursor()

# Query data needed 
cursor.execute("""
  SELECT 
    c.guid,          
    c.chat_identifier, 
    c.display_name, 
    c.group_id,     
    c.original_group_id, 

    h.id,

    a.guid,         
    a.original_guid, 
    a.created_date,   
    a.filename,       
    a.transfer_name,  
    a.mime_type,      
    a.total_bytes,      
    a.is_outgoing,     

    m.guid,          
    m.text,           
    m.handle_id,       
    m.service,        
    m.date,           
    m.is_from_me,      
    m.is_emote,         
    m.is_audio_message, 
    m.associated_message_guid, 
    m.associated_message_type,   
    m.reply_to_guid,   
    m.thread_originator_guid   

  FROM message AS m
  LEFT JOIN message_attachment_join AS maj ON maj.message_id = m.rowid
  LEFT JOIN attachment AS a ON attachment_id = a.rowid
  LEFT JOIN chat_message_join AS cmj ON cmj.message_id = m.rowid 
  LEFT JOIN chat AS c ON cmj.chat_id = c.rowid
  LEFT JOIN chat_handle_join AS chj ON chj.chat_id = c.rowid
  LEFT JOIN handle AS h ON  h.rowid = h.rowid
""")

# Parse Data



print(cursor.fetchone())

connection.close()











# 2. Go through returned data
# 3. Proccess data
# 4. Create new database
# 5. Add data to new database
