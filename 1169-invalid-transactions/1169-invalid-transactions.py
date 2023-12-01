class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        persons_transactions = defaultdict(list)
        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            persons_transactions[name].append([time, amount, city])

        visited = set()
        invalid_transactions = []
        for person, curr_transactions in persons_transactions.items():
            n = len(curr_transactions)
            for i in range(n):
                time, amount, city = curr_transactions[i]

                if int(amount) > 1000 and (i not in visited):
                    invalid_transactions.append(f"{person},{time},{amount},{city}")
                    visited.add(i)

                for j in range(n):
                    if i == j:
                        continue

                    new_time, new_amount, new_city = curr_transactions[j]

                    if abs(int(new_time) - int(time)) <= 60 and (city != new_city):
                        if i not in visited:
                            invalid_transactions.append(f"{person},{time},{amount},{city}")
                            visited.add(i)

                        if j not in visited:
                            invalid_transactions.append(f"{person},{new_time},{new_amount},{new_city}")
                            visited.add(j)

            visited.clear()

        return invalid_transactions