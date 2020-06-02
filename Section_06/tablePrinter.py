tableData = [['apples', 'oranges', 'cherriestattoo', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose123456789']]


def printTable(lists):

    col_widths = [0] * len(tableData)

    for index, list in enumerate(lists):
        longest = 0
        col_widths[index]
        for item in list:
            length = len(item)
            # print(item)
            if length > col_widths[index]:
                col_widths[index] = length

    j = 0
    for i in range(len(tableData[0])):
        # print(tableData[j][i])
        for k in range(len(tableData)):
            print(tableData[k][i].rjust(col_widths[k]), end=' ')
        print()


printTable(tableData)

#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose
