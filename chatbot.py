print("Hlw Buddy !!")
a = input("Are we known To each Other  Yes/No :").strip().lower()     # Write Yes or No in same way
if a == "yes":
    print("Haha !! I knew it.\U0001F600")
    print("But I know you dont know me,")
    print("Let me introduce myself , I'm Python\U0001F4BB")
    d = input("Want to know more about me ? Yup/Nope :").strip().lower()
    if d == "yup":
        print("HAHA !! I'm not in mood right now, open Google or any other AI. they will tell you who I am.\U0001F525")
    elif d == "nope":
        print("Okay then read Poems")
    else:
        print("Hey Buddy ! I didn't understand please answer with yup or nope.")

elif a == "no":
    print("Lets know other buddy !!")
    b = input("Tell me your name :")
    print(f"Nice To meet You {b}")
    print("My name is Python")

    c = input("Want To Know  About Me Yup/Nope:").strip().lower()         # Write Yup or Nope in same way
    if c == "yup":
     print("HAHA !! I'm not in mood right now, open Google or any other AI. they will tell you who I am.")
    elif c == "nope":
        print("Okay then, read poems")
else:
    print("Hey Buddy ! I didn't understand please answer with yes or no.")


