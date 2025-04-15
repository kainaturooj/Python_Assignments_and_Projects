# # This program demonstrates chaotic counting behavior
# # It counts from 1-10 but may stop early based on random chance
# # The DONE_LIKELIHOOD constant controls probability of early stopping
import random

 # Probability that done() returns True
DONE_LIKELIHOOD = 0.2 

def done():
   
    #Returns True with a probability of DONE_LIKELIHOOD    
    return random.random() < DONE_LIKELIHOOD


def chaotic_counting():
    
    # Counts from 1 to 10, but stops early if done() returns True
    for i in range(1, 11):
        if done():

            # Stop execution and return to main()
            return  
        print(i, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

if __name__ == '__main__':
    main()



# ////////////////////////// testing code with printing random number , just understand the working flow of code ..

# import random

# DONE_LIKELIHOOD = 0.2  # Probability that done() returns True

# def done():
#     """Returns True with a probability of DONE_LIKELIHOOD"""
#     rand_value = random.random()
#     print(f"\n[Debug] Random value: {rand_value:.4f}")  # Print the generated random number
#     return rand_value < DONE_LIKELIHOOD

# def chaotic_counting():
#     """Counts from 1 to 10, but stops early if done() returns True"""
#     for i in range(1, 11):
#         if done():
#             print("-> Stopping early due to random condition being met.")
#             return  # Stop execution and return to main()
#         print(i, end=" ")

# def main():
#     print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
#     chaotic_counting()
#     print("\nI'm done.")

# if __name__ == '__main__':
#     main()
