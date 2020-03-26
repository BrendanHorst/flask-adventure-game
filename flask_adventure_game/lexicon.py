words = {
    'directions' : ['north', 'south', 'east', 'west'],
    'movement' : ['go', 'move', 'head'],
    'action' : ['jump', 'fly', 'leave', 'open', 'unlock', 'drink', 'sip', 'chug', 'throw', 'toss', 'drop', 'offer']
}

def scan(input):

    output = { 'type': 'error', 'detail': "I don't know what that means"}

    #Checks for an empty command submission
    if input == '':
        output['detail'] = 'Enter a command'
        return output

    for test_word in input.split(' '):

        for category in words:
            for word in words[category]:

                if test_word.lower() == word:

                    if category == 'movement':
                        output['type'] = 'movement'
                        break

                    elif category == 'directions':

                        #A direction without a movement command doesn't work,
                        #it needs to follow a movement command to count
                        if output['type'] == 'movement':
                            output['detail'] = word
                            break

                    #Movement commands take priority over action commands
                    elif category == 'action' and output['type'] != 'movement':

                        output['type'] = 'action'
                        output['detail'] = word
                        break

            if output['detail'] != "I don't know what that means":
                break


    if output['type'] == 'movement' and output['detail'] == "I don't know what that means":
        output['type'] = 'error'
        output['detail'] = 'Please give a cardinal direction'

    return output
