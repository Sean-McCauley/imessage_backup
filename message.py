
class Message:

  # Handle all the info
  def __init__(self, data):
    self.chat_name = data[0]

    self.message_guid = data[1]
    self.message_text = data[2]
    self.message_service = data[3]  
    self.message_timestamp = data[4]
    self.message_from_me = data[5]
    self.message_sender = data[6]

    self.attachment_location = data[7]
    self.attachment_name = data[8]
    self.attachment_created_date = data[9]
    self.attachment_type = data[10]
    self.attachment_size = data[11]

    self.reaction_guid = data[12]
    self.reaction_type = data[13]

    self.reply_to_guid = data[14]
    self.reply_to_thread = data[15]


    # message_service
    # text
    # date
    # attachment_location
    # attachment_name
    # attachment_size
    # from_me?
    # from
    # reactions?


    # chat_name
    # message_service
    # date
    # sent?
    # sender

    # attachment_location
    # attachment_name
    # attachment_created_date
    # attachment_size
    # attachment_type

    # reaction_guid
    # reaction_type

    # message_guid
    # message_reply_to_guid,   
    # message_thread_originator_guid  
    
    # message_type




  # Clean up attachments

  # What if multiple attachments? sort by order?


# WHat 