class Phone:
    
    def __init__(self, phone_num):
        self.phone_num = phone_num
        self.call_history = []
        self.messages = []
        
    def call(self, other_num):
        called = print(f"{self.phone_num} called {other_num.phone_num} at 12:12")
        self.call_history.append(called)
        
    def show_call_history(self):
        print(self.call_history)
        
    def send_message(self, other_num, content):
        message = {"to" : self.phone_num, "from" : other_num.phone_num, "content" : content}
        self.messages.append(message)
      
    def outgoing_msg(self):
        print("outgoing messages: ")
        for message in self.messages:
            if message["from"] == self.phone_num:
                print(f"To: {message['to']}: {message['content']}")
        
    def incoming_msg(self):
        print("incoming messages: ")
        for message in self.messages:
            if message["to"] == self.phone_num:
                print(f"From: {message['from']}: {message['content']}")
        
my_phone = Phone("0587815608")
friend = Phone("0537221091")
my_phone.send_message(friend, "tes ou la??")
friend.send_message(my_phone, "jarriveee")
my_phone.send_message(friend, "ca fais 1h je tattend")
friend.send_message(my_phone, "oui ba jetait avec un client")
friend.incoming_msg()
my_phone.outgoing_msg()



        
