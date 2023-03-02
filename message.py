
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

