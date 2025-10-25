#recursive  approach complexity : o(n^2)

def insertBottom(st,x):
    if not st:
        st.append(x)
        return 
    top=st.pop()
    insertBottom(st,x)
    st.append(top)
def reverseStack(st):
    if not st:
        return
    top=st.pop()
    reverseStack(st)
    insertBottom(st,top)
if __name__=="__main__":
    st=[1,2,3,4,5,6,7,8]
    reverseStack(st)
    print("Reversed stack:", st)







#iterative approach complexity : o(n)


def reverseStack(st):
    aux = []
    while st:
        aux.append(st.pop())
    st[:] = aux

if __name__ == "__main__":
    st = []
    st.append(1)
    st.append(2)
    st.append(3)
    st.append(4)
    
    reverseStack(st)
    
    while st:
        print(st.pop(), end=" ")