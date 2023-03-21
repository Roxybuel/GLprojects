print("Hello Nerd, Welcome to Dungeons, Dungeons and more Dungeons!")

que_1 = input("Are you ready to play (yes/no)?: ")

if que_1 == 'yes':
    while True:

        que_2 = input("""Good Luck dungeon master!!!
        You awaken in a mystical land with two doors in front of you.
        Which door do you pick? (left/right): """)  # don't pick right, it takes you to the wrong door
        if que_2 == "left":
            que_3 = input("""You encounter a pretty princess.
            She is holding both a knife and a bag full of money.
            Do you a.Approach her
                   b.Grab the money and run (a/b): """)
            if que_3 == "a":
                que_4 = input("""She stabs you in the neck and leaves you for dead.
                Do you a. Pull out the knife and stab her as well
                       b. Lay there and hope for a miracle (a/b): """)
                if que_4 == "a":
                    que_4 = input("""You are still on the verge of death
                     Do you a. Take the money
                            b.Lie there(a/b): """)
                    if que_4 == "a":
                        que_5 = ("""You open up the bag and it talks!
                        The talking bag gives you two options.
                        Do you want to a. Be healed
                                       b. Go back to the real world(a/b): """)
                        if que_5 == "a":
                            print("You're saved. Broke, but saved!")
                        else:
                            print("""The bag was nice to you and decided to give you unlimited cash.
                            You're a rich nerd!""")
                    else:
                        print("You die a broke nerd!, Sorry loser.")
                else:
                    print("You die! Try again.")


            else:
                que_3 = input("""As you are running, you trip on a rock and all your money falls to the ground.
                The princess is now coming straight at you with the knife
                Do you a. Stay and pick up your money
                       b. Stand up and run for your dear life.(a/b): """)
                if que_3 == "a":
                    print("""You die a broke nerd!, Sorry loser.""")
                else:
                    que_4 = input("""You run and travel through a hidden passage way back to the real world.
                    Do you a. Go back
                           b. Continue with your life """)
                    if que_4 == "a":
                        print("""The princess was waiting for you with her precious knife.
                        She kills you. You die a broke nerd!""")
                    else:
                        print("""You have your bag of money and you can live your life as a rich nerd. :).""")


        else:
            print("""You encounter a lion that tears you to shreds.
            You die a broke nerd! Try again""")
        break
else:
    print("You're a boring nerd! Try again.")

# .lower()
