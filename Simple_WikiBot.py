from sen_chatbot.ChatBot import ChatBot

cb = ChatBot()
cb.reply('hi')

input_list = ['new user','do not have account']
output_list = ['register','create one!']
cb.addData(input_list,output_list)

cb.enableWikipedia(True)

data = {'1':{'input':['hi','hello'],'output':['hello']},'2':{'input':['bye'],'output':['goodbye','tata']}}
cb.setData(data)
