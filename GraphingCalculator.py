from graphics import *

class Stack:

    def __init__(self):
        self.mStack = []

        return
    
    def Top(self):
        return self.mStack[-1]

    def Push(self, p):
        self.mStack.append(p)
        return

    def Pop(self):
        return self.mStack.pop()
    
    def isEmpty(self):
        if len(self.mStack) >= 1:
            return False
        else:
            return True

        
    


def PrintInstructions():
    print("This program takes a math equation and graphs it for you." + '\n' + "Acceptable characters include all numbers, +, -, *, /, x or X, and '(' or ')'. " + '\n' +
    "Do not type y= only type the expression in" + '\n' + "terms of x. Example: '(x-3)*(x+2)*(x)'")


def InfixToPostfix(infix):
    S = Stack()
    postfix = ""
    for c in infix:
        if c in "0123456789":
            postfix += c
        elif c in "+-":
            while not S.isEmpty() and S.Top() in "+-*/":
                postfix += S.Pop()
            S.Push(c)
        elif c in "*/":
            while not S.isEmpty() and S.Top() in "*/":
                postfix += S.Pop()
            S.Push(c)
        elif c == "(":
            S.Push(c)
        elif c == ")":
            while S.Top() != "(":
                postfix += S.Pop()
            S.Pop()
        elif c == "x" or c == "X":
            postfix += c
    while not S.isEmpty():
        postfix += S.Pop()

    return postfix

def EvaluatePostfix(postfix, X):
    S = Stack()
    for c in postfix:
        if c in "0123456789":
            S.Push(float(c))
        elif c == "X" or c == "x":
            #print("pushing",X)
            S.Push(X)
        elif c == "+":
            x = float(S.Pop())
            y = float(S.Pop())
            S.Push(float(y + x))
        elif c == "-":
            x = float(S.Pop())
            y = float(S.Pop())
            S.Push(float(y - x))
        elif c == "*":
            x = float(S.Pop())
            y = float(S.Pop())
            S.Push(float(y * x))
        elif c == "/":
            x = float(S.Pop())
            y = float(S.Pop())
            S.Push(float(y / x))
            
        
    answer = S.Pop()
    return answer


#call this func feeding it a x list and y list and it will create window and graph
def CalculateGraph(xList, yList, xLow, xHigh, yLow, yHigh, color, title):
    #PrintInstructions()
    #infix = infixInput
    #postfix = InfixToPostfix(infix)

                  
    # Generate the point data:
    X = xList
    Y = yList
    
    XLOW = xLow
    YLOW = yLow
    XHIGH = xHigh
    YHIGH = yHigh
    #XINC = resolution
        
    # while x <= XHIGH:
    
    #     y = EvaluatePostfix(postfix, x)

	# 	#X is time
	# 	#Y is value

    #     X.append(x)
    #     Y.append(y)
    #     x += XINC


    # Draw the point data:
    win = GraphWin("Graphing Calculator", 600, 600)
    win.setCoords(XLOW,YLOW, XHIGH,YHIGH)
    anchorPoint = Point(300, 300)
    titleText = Text(anchorPoint, str(title))
    titleText.draw(win)
    for i in range(len(X)-1):
        p1 = Point(X[i], Y[i])
        p2 = Point(X[i+1], Y[i+1])
        l = Line(p1, p2)
        l.setFill(color)
        l.draw(win)
        
    #c = Circle(Point(50,50), 10)
    #c.draw(win)

    # Wait for the user to click, then quit.
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

