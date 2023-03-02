chatdb_data_query = """
  SELECT           
    c.chat_identifier,

    m.guid as message_guid,   
    m.text as message_text,                  
    m.service as message_service,        
    m.date as message_timestamp,           
    m.is_from_me as message_from_me, 
    m.handle_id as message_handle_id,  

    a.filename as attachment_filename, 
    a.transfer_name as attachment_transfer_name,   
    a.created_date as attachment_created_date,    
    a.mime_type as attachment_type,      
    a.total_bytes as attachment_size,      

    m.associated_message_guid, 
    m.associated_message_type,
   
    m.reply_to_guid,   
    m.thread_originator_guid   

    a.is_outgoing as attachment_is_outgoing,     
       

  FROM message AS m
  LEFT JOIN message_attachment_join AS maj ON maj.message_id = m.rowid
  LEFT JOIN attachment AS a ON attachment_id = a.rowid
  LEFT JOIN chat_message_join AS cmj ON cmj.message_id = m.rowid 
  LEFT JOIN chat AS c ON cmj.chat_id = c.rowid
  LEFT JOIN handle AS h ON m.handle_id = h.id
"""