class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
       int size=nums.size();
       unordered_map<int,int> pair;
       for(int i=0;i<size;i++){
        int required=target-nums[i];
        if(pair.find(required)!=pair.end()){
            return {pair[required],i};
        }
        pair.insert({nums[i],i});
       }
       return {}; 
    }
};
