import pandas as pd
 
 
def process_message(text):
    text = text.lower()
    return list(set(text.split()))
 
 
def p_message_spam(message):
    message = message.lower()
    words = set(message.split())
    spam = num_spam
    ham = num_ham
    for word in words:
        if word in model:
            spam *= model[word]['spam'] / num_spam
            ham *= model[word]['ham'] / num_ham
    return spam / (spam + ham)
 
 
messages = pd.read_csv('messages.csv')
messages['text'] = messages['text'].apply(process_message)
num_messages = len(messages)
num_spam = sum(messages['spam'])
num_ham = num_messages - num_spam
 
 
model = {}
 
for index, message in messages.iterrows():
    for word in message['text']:
        if word not in model:
            model[word] = {'spam': 0, 'ham': 0}
 
        if message['spam']:
            model[word]['spam'] += 1
        else:
            model[word]['ham'] += 1
 
print('Predication using Naive Bayes for word lottery sale', p_message_spam('lottery is niceaodinbaosdnasdolandoaidsnasd'))
print('Predication using Naive Bayes for word lottery sale', p_message_spam('asdfghlottery'))
print('Predication using Naive Bayes for word lottery sale', p_message_spam('Hi Mom, How are you?'))
