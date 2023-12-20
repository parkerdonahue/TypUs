import json
from datetime import date



def read_specs(json_file):
    # Import spec data into a variable   
    with open(json_file) as spec_file:
        specs = json.load(spec_file)
        # print(specs)
        return specs['users']


def seperate(users, date):
    user_count = len(users)
    # print(user_count)
    # print()
    # print('---')
    all = []
    for user_id, user in users.items():
        # print(type(user))
        # print(user)
        name = user.get('name')
        # print(name)
        # print(user_id)
        entries = user.get('entries')
        # print(entries)
        
        today = entries.get(date)
        # print(type(today))
        # print(today)
        if today != None:
            accuracy = today.get('accuracy') or 0
            # print("Accuracy: {}".format(accuracy))
            score = today.get('score') or 0
            # print("Score: {}".format(score))
            wpm = today.get('wpm') or 0
            # print("WPM: {}".format(wpm))
            all.append({'name':name,'wpm': wpm,'score': score})
        else:
            all.append({'name':name,'wpm': 0,'score': 0})
        
    sorted_scores = sorted(all, key=lambda x: x['score'], reverse=True)

    scores={}
    for i in range(user_count):
        scores[i] = sorted_scores[i]

    return scores
    


if __name__ == "__main__":
    import sys

    file = sys.argv[-1]
    users = read_specs(file)
    # print(users)
    # print("\n\n\n")
    today = date.today()
    formatted_date = today.strftime("%m-%d-%Y")

    # print("Today's date:", formatted_date)

    scores = seperate(users, formatted_date)
    # for val in scores:
    #     print(val)
    #     print('---')
    
    # sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)

    # print("\nSorting...\n")
    # for val in scores:
    #     print(val)
    #     print('---')

    # into_dict = dict(('scores',sorted_scores))

    into_object = json.dumps(scores)#, indent=2)

    # print()
    
    print(into_object)