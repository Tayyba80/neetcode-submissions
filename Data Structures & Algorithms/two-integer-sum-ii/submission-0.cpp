class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
         int size=numbers.size();
       unordered_map<int,int> pair;
       for(int i=0;i<size;i++){
        int required=target-numbers[i];
        if(pair.find(required)!=pair.end()){
            return {pair[required]+1,i+1};
        }
        pair.insert({numbers[i],i});
       }
       return {};
    }
};
