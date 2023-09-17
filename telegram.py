from telethon.sync import TelegramClient
import datetime
import pandas as pd
import config

# Create your own ID and HASH on Telegram
api_id = config.api_id
api_hash = config.api_hash

# Select a group you want to scrape
chats = ['berlinhelpsukrainians']
# Select a date from which you want to scrape
specific_date = datetime.datetime(2021, 1, 1)

# Create a single client instance
with TelegramClient('test', api_id, api_hash) as client:
    df = pd.DataFrame()

    for chat in chats:
        for message in client.iter_messages(chat, offset_date=specific_date, reverse=True):
            print(message)
            data = {"group": chat, "sender": message.sender_id, "text": message.text, "date": message.date}
            temp_df = pd.DataFrame(data, index=[1])
            df = df.append(temp_df)

    df['date'] = df['date'].dt.tz_localize(None)

    # Save the DataFrame to a CSV file
    csv_filename = "data_ext2_{}.csv".format(datetime.date.today())
    df.to_csv(csv_filename, index=False)

    print("CSV file saved as:", csv_filename)
