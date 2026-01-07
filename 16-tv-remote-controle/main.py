import random
import time


class RemoteControl:
    def __init__(self, tv_status="Off", volume=0, channel_list=None, current_channel="TRT"):
        if channel_list is None:
            channel_list = ["TRT"]

        self.tv_status = tv_status
        self.volume = volume
        self.channel_list = channel_list
        self.current_channel = current_channel

    def turn_on_tv(self):
        if self.tv_status == "On":
            print("TV is already ON.")
        else:
            print("Turning TV ON...")
            self.tv_status = "On"

    def turn_off_tv(self):
        if self.tv_status == "Off":
            print("TV is already OFF.")
        else:
            print("Turning TV OFF...")
            self.tv_status = "Off"

    def volume_settings(self):
        while True:
            choice = input(
                "Decrease Volume: '<'\n"
                "Increase Volume: '>'\n"
                "Exit: 'exit'\n"
            )

            if choice == "<":
                if self.volume > 0:
                    self.volume -= 1
                print("Volume:", self.volume)

            elif choice == ">":
                if self.volume < 31:
                    self.volume += 1
                print("Volume:", self.volume)

            else:
                print("Volume updated:", self.volume)
                break

    def add_channel(self, channel_name):
        print("Adding channel...")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("Channel added successfully.")

    def random_channel(self):
        self.current_channel = random.choice(self.channel_list)
        print("Current channel:", self.current_channel)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return (
            f"TV Status      : {self.tv_status}\n"
            f"TV Volume      : {self.volume}\n"
            f"Channel List   : {self.channel_list}\n"
            f"Current Channel: {self.current_channel}\n"
        )


remote = RemoteControl()

print("""
📺 TV Remote Control Application

1. Turn TV On
2. Turn TV Off
3. Volume Settings
4. Add Channel
5. Channel Count
6. Random Channel
7. TV Information

Press 'q' to quit
""")

while True:
    action = input("Select an option: ")

    if action == "q":
        print("Exiting program...")
        break

    elif action == "1":
        remote.turn_on_tv()

    elif action == "2":
        remote.turn_off_tv()

    elif action == "3":
        remote.volume_settings()

    elif action == "4":
        channels = input("Enter channel names separated by commas: ")
        for channel in channels.split(","):
            remote.add_channel(channel.strip())

    elif action == "5":
        print("Total channels:", len(remote))

    elif action == "6":
        remote.random_channel()

    elif action == "7":
        print(remote)

    else:
        print("Invalid option!")
