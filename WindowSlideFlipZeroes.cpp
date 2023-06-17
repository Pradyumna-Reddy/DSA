class Solution1 {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i = 0,j = 0;
        int curr = 0;
        int ans = 0;
        
        for(int j = 0; j < nums.size(); j++) {
            
            if(nums[j] == 0) {
                curr++;
            }

            if(curr > k) {
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
            ans = j - i + 1 > ans? j - i + 1 : ans;
        }
        return ans;
    }
};

class Solution3 {
public:
    int longestOnes(vector<int>& nums, int k) {
        int i = 0,j = 0;
        int curr = 0;
        int ans = 0;
        for(int j = 0; j < nums.size(); j++) {
            
            if(nums[j] == 0) {
                k--;
            }

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
