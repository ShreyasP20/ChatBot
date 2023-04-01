import re
from urllib import response
import ChatBot.long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty=0
    has_required_words=True
    
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage=float(message_certainty)/float(len(recognised_words))
    
    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break
    
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    
def check_all_messages(message):
    highest_prob_list={}
    
    def response(bot_responses, list_of_words, single_response=False, required_words=[] ):
        nonlocal highest_prob_list
        highest_prob_list[bot_responses]=message_probability(message, list_of_words, single_response, required_words)
        
    response("Namaste!",['hello','hi','sup','hey','heyo'], single_response=True)
    response('I m doing fine ,Wbt U?', ['how','are','you','doing'], required_words=['how'])
    response('Thank YOU!', ['i','love','bot',], required_words=['love','bot'])
    
    response(long.R_EATING, ['What','do','u','eat'], required_words=['eat'])

    best_match=max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)
    
    return long.unknown() if highest_prob_list[best_match]<1 else best_match

                


def get_response(user_input):
    split_msg=re.split(r'\s+|[, ; ?! .-]\s*',user_input.lower())
    response=check_all_messages(split_msg)
    return response


while True:
    print("Bot:" + get_response(input("You:")))