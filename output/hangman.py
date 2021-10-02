import os,random,time,randomword
# Welcome to game
print("***************************************************************************\n\n\t********************************************************\n")
print("\n\n\n\t\t       WELCOME TO THE GAME HANGMAN!!!!!!!!\n\n")
print("\n\n\t********************************************************\n\n***************************************************************************\n")
time.sleep(3)
os.system('CLS')
#USER DETAILS
name = input("Enter your name : ")
name=name.capitalize()
os.system('CLS')
#user welcome
print("\n\n\n\n\t\t Welcome {}\n\n".format(name.upper()))
#game started
print('{:*^60}'.format('Lets start the game HANGMAN!!!!!!!!!'))
print("\n\n\n")
time.sleep(2)
os.system('CLS')
#words in a list
cowrd = randomword.get_random_word()
j=len(cowrd)
#selecting trials
trails = random.randrange(j,j*2)
a="*"*j
guess_list=list()
# map can listify the list of strings/strings individually
test = list(map(str, cowrd))
#checking game start and end
while('*' in a and trails>=0):#add case when star is over and trail still not 0 and vice versa
    print("\n\n\t",a)
    print("\n\nWrong guesses allowed :", trails)
    guess=input("\nGuess a letter : ")
        #checking if is guess present or not in our answer
    if len(guess)<1:
        print('\n\n\t Oohhhhh noooo!!!! Please enter alphabets only')
        time.sleep(2)
        os.system('CLS')
        continue
    elif guess in cowrd and guess not in a:
        print("\n\n\t Hurray!!!!Right guess",name)
        k=int(test.index(guess))
        for i in range(k,j):
            if guess==test[i]:
                a = "".join(a[:i]+guess+a[i+1:])

    #trials -> if word is already matched or wrong guess
    else:
        if guess not in guess_list and guess not in cowrd:
            guess_list.append(guess)
            print("\n\n\tOooppssss!!!! Wrong guess", name)
            trails -= 1
        else:
            print("\n\n\tOooppssss!!!! Already guessed this letter", name)
    time.sleep(3)
    os.system('CLS')
guess_list.clear()
count = dict()
if a==cowrd:
    print("""\n\n               Marvellous !!! Fantastic !!! {}!!!!\n\n\t\t   The word is {}\n\n"
          
          
                         You won the game.......
                
                
                 You are awarded with {} points!!!!!""".format(name, cowrd, 2*j))
    point=2*j 
else:
    print("\n\n\t Bad luck {} !!!!!\n\n\t\t   The correct word is {}\n\n".format(name,cowrd))
    print("""              ******** GAME OVER ******** 
          
                        {} , better luck next time!!!!!!!!!!
          
                You score is reduced by {} points!!!!!""".format(name.upper(), 2*j))
    point=-(2*j)
time.sleep(6)
os.system('CLS')
print("\n\n\n\t\t****** STATS ******\n\n")
fhand = open("hang1.txt")
#checking if name exists in file
check = False
#reading from file
for line in fhand:
    #reading names and points of file 
    if line.startswith(name):
        check = True
        c = line.split()
        nm = c[0]
        count[nm] = int(c[1])+point
    else:
        c = line.split()
        nm = c[0]
        count[nm] = int(c[1])
fhand.close()
if check is False:
    #fhand.write("{} {}".format(name, point))
    nm = name
    count[nm] = point
#fhand.close()
#sorting and printing count on basis of score
newtup = list()
newtup = sorted([(val, key) for key, val in count.items()], reverse=True)
a = 1
fhand = open("hang1.txt", 'w')
print("RANK \t\t{:^20} \t\t\tSCORE".format("NAME"))
for k, v in newtup:
    print("{}\t\t{:^20}\t\t\t{}".format(a, v, k))
    a += 1
    fhand.write("{} {}\n".format(v,k))  # updated value in file
fhand.close()


