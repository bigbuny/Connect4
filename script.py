class Connect4:
    # getStruct {{{ 
    def getStruct(self, x, y):

        # Gaol 
            # create a datastructure for the board and return it.
            # If a block is empty, '' is used.
            # x and 0 would be used for the two players.
            # TYPE: nested looped list.
        # 

        struct = [ [ ' ' for i in range(x) ] for i in range(y) ] 
        self.x = x
        self.y = y
        return struct
    # }}} 
    
# Addfoo {{{ 
    def Addfoo(self, info, struct):
        #info = {'Player': 'x', 'x':}
        #validate x and y using the structure
        player = info[0]
        x = info[1] - 1 

        # Logic: the user will only specify the x, you have to find the right y.
        for i in range(self.y):
            if struct[self.y-i-1][x] == ' ':
                struct[self.y-i-1][x]  = player
                break
        return struct
        
# }}}

# Draw {{{ 
    def Draw(self, x, y, struct):
        for i in range(x):                                  #
            print(i+1, end='    ')                          # Numbers
        print()                                             #

        for j in range(y):                                  #
            print('+',end='')                               #
            for i in range(x):                              # First 
                print('----', end='+')                      #       Line
            print()                                         # 

            for i in range(x):                              # From now on 
                if struct[j][i] != ' ':                     #   j => local y
                    print('|', end=' '+struct[j][i]+'  ')   #   i => local x
                elif struct[j][i] == ' ':                   #
                    print('|', end='    ')                  #
            print('|', end='')                              #
            print()                                         #

        print('+',end='')                                   # Last 
        for i in range(x):                                  #     Line
            print('----', end='+')                          #        
        print()                                             #
#}}}

# check_winner {{{
    def check_winner(self, struct, playeri):
    #for horizontal, any adjacent four.
        for i in range(len(struct)):
            bool_ = False
            L = struct[i]
            # take all elements into consecutive group of 4.
            for j in range(len(L)):
                L_i = L[j:4+j]
                if set(L_i) == {playeri}:
                    bool_ = True
                    return True
                    break
                if 4+j == len(L): break
            if bool_:
                break
        count = 0
    #for vertical checking
        while count != self.x-1:
            bool_ = False
            L = []
            for i in range(len(struct)):
                L.append(struct[i][count])
            for j in range(len(L)):
                L_i = L[j:4+j]
                if set(L_i) == {playeri}:
                    bool_ = True
                    return True
                    break
                if 4+j == len(L): break
            if bool_:
                break
            count += 1
    # diagnol
        
        #    
# }}}

# Main {{{ 
    def Main(self):
        dimensions = input("Dimensions (i.e 6x7 for 6col & 7rows): ")
        x=int(dimensions.split('x')[0])
        y=int(dimensions.split('x')[1])
        
        player1 = input("Symbol 4 player1 (i.e x, 0, $, ^, etc): ")
        player2 = input("Symbol 4 player2 (u know): ")
            
        initial_struct=self.getStruct(x, y)
        struct = initial_struct # initially
        self.Draw(x,y, initial_struct)

        i=1 
        while True:
            print(f"=======================================Move for player{i}==================================")
            k = int(input("Choose the column: "))
            if i==1:
                playeri = player1
                play_1 = True
            elif i==2:
                playeri = player2
                play_1 = False
            if play_1:
                i = 2
            else:
                i = 1
            info = [playeri, k]
            struct=self.Addfoo(info, struct) 
            winner=self.check_winner(struct, playeri)
            print(winner)
            self.Draw(x, y, struct)
            if winner:
                print(f" player {playeri} is the winner")
                break



          

        
# }}} 

connect = Connect4()
connect.Main()
