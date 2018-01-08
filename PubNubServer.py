# This file handles PubNub messages sent to the application.

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

import POSTRequests
 
class PubNubServer(object):
    credentials_file_name = "PubNubCredentials.txt"
    channel_name = 'blinky_channel'

    def __init__(self, blinky_interface):
        self.blinky_interface = blinky_interface

        self.credentials = {}

        self.read_credentials()

    def read_credentials(self):
        try:
            with open(self.credentials_file_name) as credentials_file:
                for line in credentials_file:
                    key, value = line.split("=")
                    self.credentials[key.strip()] = value.strip()
        except IOError:
            print('Could not read credentials from file: ' + self.credentials_file_name)

    def subscribe_key(self):
        return self.credentials.get('subscribe_key')

    def publish_key(self):
        return self.credentials.get('publish_key')

    def listen(self):
        pnconfig = PNConfiguration()
        pnconfig.subscribe_key = self.subscribe_key()
        pnconfig.publish_key = self.publish_key()
        self.pubnub = PubNub(pnconfig)
        self.blinky_listener = BlinkySubscribeCallback()
        self.blinky_listener.inject_blinky_interface(self.blinky_interface)
        self.pubnub.add_listener(self.blinky_listener)
        self.pubnub.subscribe().channels(self.channel_name).execute()

    def stop_listening(self):
        self.pubnub.remove_listener(self.blinky_listener)


class BlinkySubscribeCallback(SubscribeCallback):
    def inject_blinky_interface(self, blinky_interface):
        self.blinky_interface = blinky_interface

    def presence(self, pubnub, presence):
        pass  # handle incoming presence data

    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            # This event happens when radio / connectivity is lost
            print 'PubNub unexpected disconnect'
 
        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            print 'PubNub connected'
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
            print 'PubNub reconnected'
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
            print 'PubNub decryption error'

    def message(self, pubnub, message):
        # Handle new message stored in message.message
        print 'Received PubNub message: ' + str(message.message)
        route = message.message.get('route')
        if route:
            POSTRequests.process_route_with_data(route, message.message, self.blinky_interface)

