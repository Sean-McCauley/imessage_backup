This intention of this document is to help focus my goal, keep track of my thoughts, and be used as a general game plan. As I progress throught this project, this document will be subject to change. Hopefully this change is always for the better. 

# Goal
I want to create a web app that backups my Imessages and allows me to view them. I want this web app to semi mimic apples Immesage app. To keep things simple, the main page will have a list of conversations. I will be able to click the conversation to view more details.

# Layout

## Conversation Page  
The main page should be list of the conversations. A basic conversation item probably should include:  
- Conversation name
- Contact(s)
- Edit Button
  - Allows me to change the Conversation name
  - Maybe a delete button to remove unwanted conversations

## Message Page
This page will show the message history. There are different types of messages I am going to try to handle.

1. Text: This is a basic message with just characters to display
2. Attachment: This is a message that contains a picture or video
3. Reaction: This is a persons reaction to a message
4. Reply Thread: This is a chain of messages that are linked. I am not sure how to handle this yet. 


# Step one: Backup Database

## My Database Tables
In my database, I want a couple differnt tables to make my life easier. 
1. Chat table
    - Chat Chat Name (editable)
    - Contact(s) Involved
2. Contact Table
    - Phone number
    - First Name
    - Last Name
3. Message Table
    - guid
    - text
    - message service (immesage/sms)
    - date 
    - is_emote? 
    - is from me
    - is empty?
    - is audio message
    - is attachment
    - reactions
    - reply to guid
    - reply thread guid

How do these tables relate to eachother?  
1. __Chat to Contacts:__ I believe this is a  `many to many` relationship. Contacts can be a part of many chats, and a chat can have many contacts.
2. __Chat to Messages:__ I believe this is a `one to many` relationship. One chat contains many messages


Helpul link for relating these tables:
```
https://www.youtube.com/watch?v=4q-keGvUnag&ab_channel=LinkedInLearning
```


## Understanding `chat.db`
`chat.db` is my main resource to being able to get accesss to my Imessages. This SQLite database stores the messages information and will be the key to creating this app. In `chat.db`, there are 4 main tables:

Table Name  | Description
----------- | ------------- 
attachment: | Data about attachments
chat:       | Every chat
handle:     | Chats viewed by `this` device 
message:    | Messages sent and recieved

For all of these tables to work together, relationship tables are also available in the database. These include `chat_handle_join`, `chat_message_join`, and  `message_attachemnt_join`. I will be using these tables to gather and connect data into my own backup database.  



### Useful Information in `chat.db`:

Table      | Field         | Type 
 --------- | -----         | -----
attachment | created_date  | INTEGER DEFAULT 0
attachment | filename      | TEXT
attachment | transfer_name | TEXT
attachment | mime_type     | TEXT
attachment | total_bytes   | INTEGER DEFAULT 0
attachment | is_outgoing   | INTEGER DEFAULT 0
chat       | guid          | TEXT UNIQUE NOT NULL
chat       | display_name  | TEXT
chat       | group_id      | TEXT
message    | text          | TEXT
message    | service       | TEST
message    | date          | INTEGER
message    | is_from_me    | INTEGER DEFAULT 0
message    | is_emote      | INTEGER DEFAULT 0   
message    | is_audio_message | INTEGER DEFAULT 0
message    | guid          | TEXT UNIQUE NOT NULL
message    | associated_message_guid | TEXT
message    | associated_message_type | INTEGER DEFAULT 0
message    | reply_to_guid | TEXT DEFAULT NULL
message    | thread_orginator_guid | TEXT DEFAULT NULL



## Translating Chat.DB to My database
To create my table from `chat.db`, I will make a query to get all the data at once. I think that I will clean up certain attributes as I process each record. 

### Chat Table
Desired Field | Need      | Notes 
------------- | --------- | ----
chat_id       | Not sure  | I might want to clean this up
chat_name     | guid?     | Contact(s) as defualt

### Contacts Table
Desired Field | Need      | Notes 
------------- | --------- | ----
contact_id    |           | just a number 
contact_number | handle   | Collect the pone
contact_first |           | User input?
contact_first |           | User input

### Message Table
Desired Field | Need      | Notes 
------------- | --------- | ----
message_id    |           | I can create this
timestamp     | date      | date/created_date
text          |           | If any
attachment    | filename  | If any
attachment_type |           |
reactions     |           |
reply_to_guid |           |
reply_thread_guid |

### Later updates to the table
To create functionality for future updates to my table, I will create a seperate table that stores data to help me pick up where i last left off.







