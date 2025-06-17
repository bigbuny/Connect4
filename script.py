class Connect:
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
        #numbers
        for i in range(x):
            print(i+1, end='    ')
        print()
        for j in range(y):

        #first line
            print('+',end='')
            for i in range(x):
                print('----', end='+')
            print()

        #content after lines
            for i in range(x):

        #from now on j is y and i is x
                if struct[j][i] != ' ':
                    print('|', end=' '+struct[j][i]+'  ')
                elif struct[j][i] == ' ':
                    print('|', end='    ')
            print('|', end='')
            print()
        #last_line
        print('+',end='')
        for i in range(x):
            print('----', end='+')
        print()
#}}}

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
            self.Draw(x, y, struct)



          

        
# }}} 

connect = Connect()
connect.Main()

