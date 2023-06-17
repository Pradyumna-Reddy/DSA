class Solution1 {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i = 0,j = 0;
        int curr = 0;
        //int ans = 0;
        
        for(int j = 0; j < nums.size(); j++) {
            if(nums[j] == 0) {
                curr++;
            }
            
            // Decreasing the window size here while popping from front
            // (not needed to decrease though, as we only want largest length of subarray which confirms to the condition
            while(curr > k) {
                if(nums[i] == 0) {
                    curr--;
                }
                i++;
            }
            
            ans = j - i + 1 > ans? j - i + 1 : ans;
        }
        return ans;
    }
};

class Solution2 {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i = 0,j = 0;
        int curr = 0;
        int ans = 0;
        
        for(int j = 0; j < nums.size(); j++) {
            
            if(nums[j] == 0) {
                curr++;
            }

            // better approach when trying to find largest length subarray
            // when your window size is proportional to constraint measure
            // meaning: Once an invalid window is found, increasing right pointer
            // to increase window size would only result in invalid solutions 
            if(curr > k) {
                if(nums[i] == 0) {
                    curr--;
                }
                i++;
            } 
            // I was storing the ans previousy, but not needed as I would not be decreasing window size once it's valid, but only increase as long as validity stays.
            // ans = j - i + 1 > ans? j - i + 1 : ans;
        }
        return j - i + 1;
    }
};

class Solution3 {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i = 0,j = 0;
        int ans = 0;
        for(int j = 0; j < nums.size(); j++) {
            
            if(nums[j] == 0) {
                k--;
            }

            // Same as second approach, just that we don't use variable to store frequency, we use k directly 
            // Since we can only decrement k to certain extent, we will say window is invalid when we use up k
            if(k < 0) {
                if(nums[i] == 0) {
                    k++;
                }
                i++;
            }      

            ans = j - i + 1;     
        }
        return ans;
    }
};
