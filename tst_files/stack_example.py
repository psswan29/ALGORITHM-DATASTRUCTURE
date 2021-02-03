from dataStructure import Stack
import string

def infixtopostfix(infixexpr:str):
    """
    用python实现从中序表达式到后序表达式的转换
    :param infixexpr: 输入的表达式需要严格按照空格分开的形式
    :return:
    """
    # 建立一个字典用来存储运算优先级
    priority = {}
    priority['*'] = 3
    priority['/'] = 3
    priority['+'] = 2
    priority['-'] = 2
    priority['('] = 1
    # 在这里为什么括号的优先级最低?只有中序表达式才需要括号，在后序表达式中
    # 建立栈用以存储运算符
    operatorStack = Stack()
    # 用来储存输出结果
    postfixList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token[0] in string.ascii_letters or token[0] in string.digits:
            postfixList.append(token)
        elif token == '(':
            operatorStack.push(token)
        elif token == ')':
            toptoken = operatorStack.pop()
            while toptoken != '(':
                postfixList.append(toptoken)
                toptoken = operatorStack.pop()
            pass
        # 若是运算符时
        else:
            while (not operatorStack.isEmpty) and (priority[operatorStack.peek()] >= priority[token]):
                postfixList.append(operatorStack.pop())
            operatorStack.push(token)

    while not operatorStack.isEmpty:
        postfixList.append(operatorStack.pop())
    return " ".join(postfixList)

def cal_postfix(postfixExpr):
    oper_dict = {
        '+': lambda x,y: x + y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x/y,
    }
    s = Stack()
    tokens = postfixExpr.split()
    for token in tokens:
        if token[0] in string.digits:
            if '.' in token:
                s.push(float(token))
            else:
                s.push(int(token))
        else:
            value2 = s.pop()
            value1 = s.pop()
            s.push(oper_dict[token](value1, value2))

    return s.pop()


if __name__ == '__main__':
    exp = infixtopostfix(' 11 + 12.4 / 2 - 1 + 1')
    print(cal_postfix(exp))