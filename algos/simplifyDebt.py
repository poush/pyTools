# Sample data
transactions = [
    {   'paidBy': 'A',  'paidFor': { 'B': 100, 'C': 50 } },
    {   'paidBy': 'A',  'paidFor': { 'C': 500 } },
    {   'paidBy': 'B',  'paidFor': { 'A': 150, 'C': 200 } },
    {   'paidBy': 'C',  'paidFor': { 'A': 250, 'B': 200 }   }
]

# transactions = [
#   { 'paidBy': 'B' , 'paidFor': { 'A': 200 }},
#   { 'paidBy': 'C' , 'paidFor': { 'B': 100 }},
#   { 'paidBy': 'A' , 'paidFor': { 'C': 100 }},
# ]

# transactions = [
#     {   'paidBy': 'A',  'paidFor': { 'C': 300, 'E': 40, 'F': 30 } },
#     {   'paidBy': 'B',  'paidFor': { 'D': 50 } }
# ]

def findSame(txs, value):
    # print(txs)
    n = 0
    while n<len(txs):
        if txs[n][1] == -value:
            return n
        n+=1
    return -1


def simplifyDebts(transactions):
    owes = []
    people_dept = {}
    for transaction in transactions:
        paidBy = transaction.get('paidBy')
        if paidBy not in people_dept:
            people_dept[paidBy] = 0

        transfers = transaction.get('paidFor');

        for person in transfers:
            if person in people_dept:
                people_dept[person] += transfers[person]
            else:
                people_dept[person] = transfers[person]

            # removing from the debt of person who paid
            people_dept[paidBy] -= transfers[person]

    people_dept = sorted(people_dept.items(), key=lambda k: k[1])
    while True:
        
        # print(people_dept)
        # Now calculating who will pay to whom
        total = len(people_dept)
        debit = people_dept[total-1]
        credit = people_dept[0]
        ccheck = findSame(people_dept, debit[1])
        credit = people_dept[ccheck] if ccheck is not -1 else credit
        c = ccheck if ccheck is not -1 else 0


        if credit[1] == 0 and debit[1]  == 0:
            # sorted, there is nothing to do now
            # Rupya Pohonch gaya
            break

        m = min([-credit[1], debit[1]])
        # settling the transaction
        people_dept[c] = (credit[0], credit[1] + m)
        people_dept[total-1] = (debit[0], debit[1] - m)
        # break
        
        print("Person " + debit[0] + " will pay " + str(m) + " to "+ credit[0])
        people_dept = sorted(people_dept, key=lambda k: k[1])
        # print(people_dept)


if __name__ == "__main__":
    simplifyDebts(transactions)
