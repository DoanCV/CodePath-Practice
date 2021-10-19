"""
U
We are given a list of transactions
    each transaction is a string in the form "name, time, amount, city"

if the transaction amount exceeds 1000. it can be invalid so we need to return that transaction

also if the transaction occurs within 60 minutes of another transaction with the same name in a different city


M
we can map the name to the transactions associated with that name

PIR

E
O(N) time complexity, where N is the number of transactions. We traverse through our transactions to map the name to its respective transactions. Then we check all transactions per key for validity. These two loops are worst case O(N).
"""

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        # add to hashmap
        hashmap = {}
        for transaction in transactions:
            curr_transaction = transaction.split(",")
            
            # [name, time, amount, city]
            
            if curr_transaction[0] not in hashmap:
                hashmap[curr_transaction[0]] = []
            
            hashmap[curr_transaction[0]].append(curr_transaction)
        
        
        # check for invalid transactions
        invalid_transactions = []
        for transaction in transactions:
            curr_transaction = transaction.split(",")
            
            if int(curr_transaction[2]) > 1000:
                invalid_transactions.append(",".join(curr_transaction))
                
            else:
                
                # check all of the transactions with the same name and see if they are within 60 min in a different city
                
                for curr in hashmap[curr_transaction[0]]:
                    
                    if curr_transaction[3] != curr[3] and abs(int(curr_transaction[1]) - int(curr[1])) <= 60:
                        invalid_transactions.append(",".join(curr_transaction))
                        break
        
        
        return invalid_transactions
