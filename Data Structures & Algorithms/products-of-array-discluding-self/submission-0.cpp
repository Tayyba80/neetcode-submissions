class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(),1);
        int p=1;
        for(int i=0;i<nums.size();i++){
            res[i]=p;
            p=p*nums[i];
        }

       int q=1;
        for(int j=nums.size()-1;j>=0;j--){
            res[j]=res[j]*q;
            q=q*nums[j];
        }
        return res;
    }
};
