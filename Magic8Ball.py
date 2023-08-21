while True:

    import random

    a1 = "It is certain."
    a2 = "Without a doubt."
    a3 = "Yes, definitely."
    a4 = "Signs point to yes."
    b1 = "Cannot predict now."
    b2 = "Better not tell you now."
    c1 = "Don't count on it."
    c2 = "My reply is no."
    c3 = "My sources say no."
    c4 = "Outlook not so good."

    def getnumber():
        Q = input("Ask a question :")
        A = [a1, a2, a3, a4, b1, b2, c1, c2, c3, c4]
        R = random.choice(A)
        return R

    result = getnumber()
    print("Magic 8 Ball says: " + result)

