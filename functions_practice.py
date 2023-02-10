#Function which returns a greeting

def hello():
    print("Best wishes to you.")

hello()

# Pack function, tells contents of backpack in a return

def pack(thing_1,thing_2,thing_3):
    backpack = [thing_1,thing_2,thing_3]
    return backpack

print(pack("granola_bars","cell_phone","inflatable_dinghy"))

# Lunch function
'''The len() function can find the length of a list or a string, but it counts the
characters in the string, not the words.
The empty lunchbox is the if statement because it has the least amount to check for.
Once the function has determined there is, indeed, a list, it can move on to the else.
The for loop uses range(len()) instead of just len(). Range creates a list of the index
numbers from the total it receives from len(), which the for loop then iterates over.
'''

lunch_items = ["a sandwich","milk","an apple","a whole cake"]
no_lunch = []
small_lunch = ["a salad"]

def eat_lunch(list_name):
    if len(list_name) == 0:
        print("My lunchbox is empty!")
    else:
        for x in range(len(list_name)):
            if x == 0:
                print(f"First I eat {list_name[0]}.")
            else:
                print(f"Next I eat {list_name[x]}")

eat_lunch(lunch_items)
eat_lunch(no_lunch)
eat_lunch(small_lunch)