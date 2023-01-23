This intention of this document is to help focus my goal, keep track of my thoughts, and be used as a general game plan. As I progress throught this project, this document will be subject to change. Hopefully this change is always for the better. 

# Goal
I want to create a web app that backups my Imessages and allows me to view them. As this is just my initial goal and understandings, this 

# Understanding `chat.db`
`chat.db` is my main resource to being able to get accesss to my Imessages. This SQLite database stores the messages information and will be the key to creating this app. In `chat.db`, there are 4 main tables:

Table Name  | Description
----------- | ------------- 
attachment: | Data about attachments
chat:       | Every chat
handle:     | Chats viewed by `this` device 
message:    | Messages sent and recieved

For all of these tables to work together, relationship tables are also available in the database. These include `chat_handle_join`, `chat_message_join`, and  `message_attachemnt_join`. I will be using these tables to gather and connect data into my own backup database.  

# Backup Database
My first step of this project will be to create the backup database. To do this, I first must determine what information in 'chat.db' may be relevant or useful. 

Useful Information in `chat.db`:

Table      | Field         | Type 
 --------- | -----         | -----
attachment | created_date  | INTEGER DEFAULT 0
attachment | filename      | TEXT
attachment | transfer_name | TEXT
attachment | mime_type     | TEXT
attachment | total_bytes   | INTEGER DEFAULT 0
attachment | is_outgoing   | INTEGER DEFAULT 0
chat       | guid          | TEXT UNIQUE NOT NULL
chat       | chat_identifier| TEXT
chat       | display_name  | TEXT
chat       | group_id      | TEXT
message    | text          | TEXT
message    | service       | TEST
message    | date          | INTEGER
message    | is_from_me    | INTEGER DEFAULT 0
message    | is_emote      | INTEGER DEFAULT 0   
message    | is_audio_message | INTEGER DEFAULT 0
message    | guid          | TEXT UNIQUE NOT NULL
message    | associated_guid | TEXT
message    | assoassociated_guid_type | INTEGER DEFAULT 0
message    | reply_to_guid | TEXT DEFAULT NULL
message    | thread_orginator_guid | TEXT DEFAULT NULL



