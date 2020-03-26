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

    return output
