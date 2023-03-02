
# --------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------
import sqlite3
import time
import sql
from extract import *
from datetime import datetime
from message import Message

# --------------------------------------------------------------------------
# FUNCITONS
# --------------------------------------------------------------------------
def convert_timestamp(apple_timestamp):
  epoch_timestamp = apple_timestamp + 978307200
  return epoch_timestamp


# --------------------------------------------------------------------------
# MAIN LINE
# --------------------------------------------------------------------------

# 1. Read in chat.db
connection = sqlite3.connect("chat.db")

# Query data needed 
chatdb = connection.execute(sql.chatdb_data_query)

# Map indices for data that needs modified:
query_fields = list(map(lambda x: x[0], chatdb.description))
index_message_timestamp = query_fields.index('message_timestamp')
index_attachment_timestamp = query_fields.index('attachment_created_date')

# Extract Data: only worry about formatting data that is collected.
messages = []
for record in chatdb:
  data = list(record)
  data[index_message_timestamp] = convert_timestamp(data[index_message_timestamp]/1000000000)  # this is is nano seconds
  
  if data[index_attachment_timestamp] != None:
    data[index_attachment_timestamp] = convert_timestamp(data[index_attachment_timestamp])

  messages.append(Message(data))




connection.close()













# 2. Go through returned data
# 3. Proccess data
# 4. Create new database
# 5. Add data to new database
