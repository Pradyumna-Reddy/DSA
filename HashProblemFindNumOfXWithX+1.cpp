//Given an integer array arr, count how many elements x there are, 
//such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

// I wrote this code interpreting as number of pairs like in [2, 3, 3] we'd have (2, 3) and (2, 3).
// But question clearly states that how many elements x in array with x+1 also in array.
// My interpretation would allow me to get if x-1 is there that would mean a pair for 3 in above array 
// there is no 4 but I would check if 2 exists and added one count to answer which is incorrect
class Solution {
public:
    int countElements(vector<int>& arr) {
        unordered_set<int, int> arr_set();
        int count = 0;
        for(int num: arr) {
            count += arr_set[num + 1];
            count += arr_set[num - 1];
            arr_set[num]++;
        }
        return count;
    }
};
