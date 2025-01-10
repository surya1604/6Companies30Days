class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        self.dp = {}
        return self.dfs(price, special, needs)
    def dfs(self, price, special, needs):
        if tuple(needs) in self.dp: # Memorization
            return self.dp[tuple(needs)]
        
        cost = sum(x*y for x, y in zip(needs, price)) # Don't take offers
        
        for offer in special: # Take one offer
            for i, need in enumerate(needs):
                if need < offer[i]: # Make sure it can take at least one offer
                    break
            else: # no break in thie for loop
                new_needs = [need - offer[i] for i, need in enumerate(needs)]
                cost = min(cost, offer[-1] + self.dfs(price, special, new_needs))
        self.dp[tuple(needs)] = cost
        return cost
