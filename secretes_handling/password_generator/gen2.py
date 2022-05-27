import string
import random
import sys

# Creating dataset of all characters required
if __name__ == "__main__":
    dataset1 = string.ascii_lowercase
    dataset2 = string.ascii_uppercase
    dataset3 = string.digits
    dataset4 = string.punctuation

# Hanlding exceptions
try:
    plen = int(input('Enter password lenght\n'))
except ValueError:
    print('Please input an integer value')
    sys.exit(1)

# Extending dataset
dataset = []
dataset.extend(list(dataset1))
dataset.extend(list(dataset2))
dataset.extend(list(dataset3))
dataset.extend(list(dataset4))

# Shuffling the dataset using sample
sample_list = random.sample(dataset, plen)
print('Your password is:')
print("".join(sample_list))

""" 
# Shuffling the dataset using shuffle
random.shuffle(dataset)
print('Your password is:')
print("".join(dataset[0:plen]))
"""