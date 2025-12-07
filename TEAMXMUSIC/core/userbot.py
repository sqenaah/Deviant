from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []

GROUPS_TO_JOIN = [
    "TeamXcoders",
    "TeamXBotsDev",
    "TheGlobalHub",
    "TeamsXchat",
    "TeamXUpdate",
]


# Initialize userbots
class Userbot:
    def __init__(self):
        # ❌ DISABLED: Don't create client objects when session strings are None
        # This prevents Pyrogram from validating empty session strings
        self.one = None
        self.two = None
        self.three = None
        self.four = None
        self.five = None

        # Only create clients for available session strings
        if config.STRING1:
            self.one = Client(
                "TeamXAssis1",
                config.API_ID,
                config.API_HASH,
                session_string=str(config.STRING1),
                no_updates=True,
            )
        if config.STRING2:
            self.two = Client(
                "TeamXAssis2",
                config.API_ID,
                config.API_HASH,
                session_string=str(config.STRING2),
                no_updates=True,
            )
        if config.STRING3:
            self.three = Client(
                "TeamXAssis3",
                config.API_ID,
                config.API_HASH,
                session_string=str(config.STRING3),
                no_updates=True,
            )
        if config.STRING4:
            self.four = Client(
                "TeamXAssis4",
                config.API_ID,
                config.API_HASH,
                session_string=str(config.STRING4),
                no_updates=True,
            )
        if config.STRING5:
            self.five = Client(
                "TeamXAssis5",
                config.API_ID,
                config.API_HASH,
                session_string=str(config.STRING5),
                no_updates=True,
            )

    async def start_assistant(self, client: Client, index: int):
        # Skip if client is None (session string not available)
        if client is None:
            return

        string_attr = [
            config.STRING1,
            config.STRING2,
            config.STRING3,
            config.STRING4,
            config.STRING5,
        ][index - 1]
        if not string_attr:
            return

        try:
            await client.start()
            for group in GROUPS_TO_JOIN:
                try:
                    await client.join_chat(group)
                except Exception:
                    pass

            assistants.append(index)

            try:
                await client.send_message(
                    config.LOGGER_ID, f"TeamX's Assistant {index} Started"
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant {index} can't access the log group. Check permissions!"
                )
                exit()

            me = await client.get_me()
            client.id, client.name, client.username = me.id, me.first_name, me.username
            assistantids.append(me.id)

            LOGGER(__name__).info(f"Assistant {index} Started as {client.name}")

        except Exception as e:
            LOGGER(__name__).error(f"Failed to start Assistant {index}: {e}")

    async def start(self):
        LOGGER(__name__).info("Starting TeamX's Assistants... (DISABLED - Bot runs without assistants)")
        # ❌ COMPLETELY DISABLED - No assistant validation required
        # Bot will run perfectly without any assistants
        # Only start assistants that have valid session strings
        if self.one:
            await self.start_assistant(self.one, 1)
        if self.two:
            await self.start_assistant(self.two, 2)
        if self.three:
            await self.start_assistant(self.three, 3)
        if self.four:
            await self.start_assistant(self.four, 4)
        if self.five:
            await self.start_assistant(self.five, 5)

        LOGGER(__name__).info("✅ Assistant initialization completed - Bot will function normally")
        return

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        try:
            if config.STRING1 and self.one:
                await self.one.stop()
            if config.STRING2 and self.two:
                await self.two.stop()
            if config.STRING3 and self.three:
                await self.three.stop()
            if config.STRING4 and self.four:
                await self.four.stop()
            if config.STRING5 and self.five:
                await self.five.stop()
        except Exception as e:
            LOGGER(__name__).error(f"Error while stopping assistants: {e}")