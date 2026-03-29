class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> pair;

        for(auto& s : strs){
            vector<int> count(26,0);
            for(auto c : s){
                count[c-'a']++;
            }
            string key;
            for(auto i : count){
                key+="$"+to_string(i);
            }
            pair[key].push_back(s);
        }
        vector<vector<string>> res;
        for(auto v : pair){
            res.push_back(v.second);
        }
        return res;
    }
};
