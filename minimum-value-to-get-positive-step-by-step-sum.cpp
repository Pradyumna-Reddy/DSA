// Given an array of integers nums, you start with an initial positive value startValue.

// In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

// Return the minimum positive value of startValue such that the step by step sum is never less than 1.

// Both below approaches are O(n) time

class Solution1 {
public:
    int minStartValue(vector<int>& nums) {
        int smallest = 1;
        if(nums[0] <= 0) {
                smallest = -(nums[0] - 1) > smallest ? -(nums[0] - 1) : smallest;
            }
        for(int i = 1; i < nums.size(); i++) {
            nums[i] += nums[i-1];
            if(nums[i] <= 0) {
                smallest = -(nums[i] - 1) > smallest ? -(nums[i] - 1) : smallest;
            }
        }
        return smallest;
    }
};


// Doesn't use array to store
// Better incase array values are not used for later use and values generated are used iteratively.
// We can simulate same behavior using a sum variable
class Solution2 {
public:
    int minStartValue(vector<int>& nums) {
        int total = 0;
        int minVal = 0;
        for(int i = 0; i < nums.size(); i++) {
            total += nums[i];

            minVal = min(minVal, total);
        }
        return 1 - minVal;
    }
};
