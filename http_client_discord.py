import requests

class HTTP_CLIENT_DISCORD:
    def __init__(self, token):
        self.rq = requests
        self.token = token
    
    def HTTP_CLIENT_MICRO(self, guild_id, user_id, bool):
        API_LINK = f'https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}'
        HTTP_CLIENT_HEADER = {
            'content-type': 'application/json',
            'authorization': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        HTTP_CLIENT_PAYLOAD = {
            'mute': bool
        }

        response = self.rq.patch(API_LINK, headers=HTTP_CLIENT_HEADER, json=HTTP_CLIENT_PAYLOAD)
        return response.text
    
    def HTTP_CLIENT_HEADSET(self, guild_id, user_id, bool):
        API_LINK = f'https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}'
        HTTP_CLIENT_HEADER = {
            'content-type': 'application/json',
            'authorization': self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        HTTP_CLIENT_PAYLOAD = {
            'deaf': bool
        }

        response = self.rq.patch(API_LINK, headers=HTTP_CLIENT_HEADER, json=HTTP_CLIENT_PAYLOAD)
        return response.text
    
    def FULL_MUTE(self, guild_id, user_id, bool):
        self.HTTP_CLIENT_HEADSET(guild_id, user_id, bool)
        self.HTTP_CLIENT_MICRO(guild_id, user_id, bool)
    
    def CHANGE_VOICE_STATE(self, voice_id, region):
        HTTP_API_LINK = f'https://discord.com/api/v9/channels/{voice_id}'
        HTTP_CLIENT_HEADER = {
            "content-type": "application/json",
            "authorization": self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        HTTP_CLIENT_PAYLOAD =  {
            "bitrate": 96000,
            "flags": 0,
            "name": "🔊│𝐓𝐞𝐚𝐦-𝐓𝐚𝐥𝐤 𝟐",
            "nsfw": False,
            "rate_limit_per_user": 0,
            "rtc_region": region,
            "topic": "",
            "type": 2,
            "user_limit": 0
        }

        response = self.rq.patch(HTTP_API_LINK, headers=HTTP_CLIENT_HEADER, json=HTTP_CLIENT_PAYLOAD)
        return response.text
    
    def DISCONECT_USER(self, guild_id, user_id):
        HTTP_API_LINK = f'https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}'
        HTTP_CLIENT_HEADER = {
            "content-type": "application/json",
            "authorization": self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        HTTP_CLIENT_PAYLOAD =  {
            "channel_id": None
        }

        response = self.rq.patch(HTTP_API_LINK, headers=HTTP_CLIENT_HEADER, json=HTTP_CLIENT_PAYLOAD)
        return response.text
        
    def RING_USER(self, channel_id, user_id):
        HTTP_API_LINK = f'https://discord.com/api/v9/channels/{channel_id}/call/ring'
        HTTP_CLIENT_HEADER = {
            "content-type": "application/json",
            "authorization": self.token,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        HTTP_CLIENT_PAYLOAD =  {
            "recipients": [f'{user_id}']
        }

        response = self.rq.post(HTTP_API_LINK, headers=HTTP_CLIENT_HEADER, json=HTTP_CLIENT_PAYLOAD)
        return response.text
        