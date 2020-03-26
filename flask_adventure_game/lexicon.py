words = {
    'directions' : ['north', 'south', 'east', 'west'],
    'movement' : ['go', 'move', 'head'],
    'action' : ['jump', 'fly', 'leave', 'open', 'drink', 'sip', 'chug', 'throw', 'toss', 'drop', 'offer']
}

def scan(input):

    output = { 'type': 'error', 'detail': 'Unknown error'}

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

                        #A direction without a movement command throws an error
                        if output['type'] == 'error':
                            output['detail'] = "I don't know what that means"
                            break

                        #A direction following a movement command is valid
                        elif output['type'] == 'movement':
                            output['detail'] = word
                            break

    if output['type'] == 'movement' and output['detail'] == 'Unknown error':
        output['type'] = 'error'
        output['detail'] = 'Please give a cardinal direction'

    return output
