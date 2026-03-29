class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map<int,int> map;
       vector<vector<int>> ans(nums.size()+1);
       vector<int> res;
        for(auto& n : nums){
            map[n]=1+map[n];
        }
        for(auto& e : map){
            ans[e.second].push_back(e.first);//num of occurence is used as index in this wat we 
            //get a sorted vector in ascending order
        }
        for(int i=ans.size()-1;i>0;i--){
            for(int n : ans[i]){
                res.push_back(n);
                if(res.size()==k){
                    return res;
                }
            }
        }
        return res;
    }
};
