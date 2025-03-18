# SudoR2spr WOODcraft
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "27536109")
API_HASH  = os.environ.get("API_HASH", "b84d7d4dfa33904d36b85e1ead16bd63")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
auth_users = "6428531614, 7841326954"
sudo_users = [int(num.strip()) for num in auth_users.split(",")]

osowner_users = "7841326954, 6428531614"
owner_users = [int(num.strip()) for num in osowner_users.split(",")]

#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

