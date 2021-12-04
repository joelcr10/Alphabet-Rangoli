def print_rangoli(size):
    # your code goes here
    rows = (2*size)-1
    column = ((2*size)-1)+((2*size)-2)
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    dash = '-'
    center = 1
    li = []
    for i in range(int(rows/2)+1):
        numberOfDash = (column-center)/2
        string = ""
        index = 0
        starting = numberOfDash
        alpha = 0
        for j in range(column):
            if j<numberOfDash or j>=numberOfDash+center:
                string = string + dash
            else:
                if j == starting:
                    if j <= int(column/2):
                        string = string + alphabet[size-1-index]
                        index = index + 1
                    else:
                        if(j == int(column/2)+2):
                            alpha = size - 1 - index + 2
                        string = string + alphabet[alpha]
                        alpha = alpha+1
                    starting = starting+2
                else:
                    string = string + dash
        print(string)
        li.append(string)
        center = center + 4

    for i in range(1,int(rows/2)+1):
        print(li[int(rows/2)-i])

if __name__ == '__main__':
    n = int(input("Enter the Size of the Rangoli: "))
    print_rangoli(n)