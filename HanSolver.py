import time
import multiprocessing
import os

positionCount = {"A":0,"B":0,"C":0}
posArr = []

def MoveCoin(frm,too):
    # Move for one coin.
    print("=============================")
    print("Move Coin from {} to {}.".format(frm,too))

    # Revise the position matrix.
    if too == "A": 
        t = 0
    elif too == "B":
        t = 1
    elif too == "C":
        t = 2
    if frm == "A": 
        c = 0
    elif frm == "B":
        c = 1
    elif frm == "C":
        c = 2

    # Position (to)
    posArr[len(posArr) - positionCount[too]-1][t] = posArr[len(posArr) - positionCount[frm]][c]
    # Position (from)
    posArr[len(posArr) - positionCount[frm]][c] = 0

    positionCount[frm] -= 1
    positionCount[too] += 1
    
    print("-----------------------------")
    for i in range(len(posArr)):
        print(posArr[i])
    print("-----------------------------")
    # Verbose Mode
    #print("Coin count list    :", end="")
    #print(positionCount)
    print("=============================")
    #time.sleep(0.1)

def MoveCoinWith(frm,too,wit):
    # Moves for 2 coins.
    MoveCoin(frm,wit)
    MoveCoin(frm,too)
    MoveCoin(wit,too)

def GuiSolver(frm,too,wit,count):
    # Arrange the window
    #os.system("mode con cols=50 lines={}".format(count+6))

    # Load position dictionary.
    positionCount[frm] = count
    # Load Poisiton Array.
    for i in range(count):
        posArr.append([0,0,0])
    if positionCount["A"] == count:
        for i in range(count):
            posArr[i][0] = posArr[i-1][0] + 1
    elif positionCount["B"] == count:
        for i in range(count):
            posArr[i][1] = posArr[i-1][1] + 1
    elif positionCount["C"] == count:
        for i in range(count):
            posArr[i][2] = posArr[i-1][2] + 1
    # Show...
    print("***********START*************")
    print("-----------------------------")
    for i in range(len(posArr)):
        print(posArr[i])
    print("-----------------------------")
    print("*****************************")
    ######## Main Solver Path ###########
    HanoiSolver(frm,too,wit,count)
    ######## Main Solver Path ###########
    print("***********END***************")
    
def HanoiSolver(frm,too,wit,count):
    if count != 3:
        HanoiSolver(frm,wit,too,count-1)
        MoveCoin(frm,too)
        HanoiSolver(wit,too,frm,count-1)
    else :
        # Tree coin solution.
        MoveCoinWith(frm,wit,too)
        MoveCoin(frm,too)
        MoveCoinWith(wit,too,frm)

starttime1 = time.time()
GuiSolver("A","C","B",5) 
time1 = time.time() - starttime1
print("1 Core solution took {} seconds".format(time1)) 

#########MULTİPROCESSİNG BU DEĞİL#############
### RUNNERS ###
#if __name__ == '__main__':
#    # Two Core Process
#    starttime2 = time.time()
#    processes = []
#   for i in range(1):
#        p = multiprocessing.Process(target=GuiSolver("A","C","B",9), args=(i,))
#        processes.append(p)
#        p.start()
#    for process in processes:
#        process.join()
#    time2 = time.time() - starttime2
#    # One Core Process
#    starttime1 = time.time()
#    GuiSolver("A","C","B",9) 
#    time1 = time.time() - starttime1
#    print("1 Core solution took {} seconds".format(time1)) 
#   print("2 Core solution took {} seconds".format(time2))