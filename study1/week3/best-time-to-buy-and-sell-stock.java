// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Time Complexity: O(n), n: prices.length
// Space Complexity: O(1), because 3 int-variables are declared -> O(1)+O(1)+O(1)
class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = prices[0];
        int sellPrice = 0;
        int profit = sellPrice - buyPrice;  // store maxProfit

        for (int i = 1; i < prices.length; ++i) {
            if (buyPrice > prices[i]) {
                buyPrice = prices[i];
            }
            if (profit < prices[i] - buyPrice) {
                profit = prices[i] - buyPrice;
            }
        }

        if (profit < 0) {   // if the profit is negative
            return 0;
        }

        return profit;
    }
}