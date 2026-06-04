
"""
168. Excel Sheet Column Title [Easy]

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1    Z -> 26
B -> 2    AA -> 27
C -> 3    AB -> 28 
"""

#-------------------------------------------------------------------------------------------------------------------------

def excelColumnTitle(col):
    if col == 1:
        return 'A'
    
    title = []
    while col > 0:
        col -= 1

        rem = col % 26
        title.append(chr(rem + 65))
        col //= 26

    title.reverse()
    title = "".join(title)

    return title

if __name__ == "__main__":
    col_number = int(input("COL NO: "))
    answer = excelColumnTitle(col_number)
    print(f"Excel Column title corresponding to column number {col_number} is {answer}")