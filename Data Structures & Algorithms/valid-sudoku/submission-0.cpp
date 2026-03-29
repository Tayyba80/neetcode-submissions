class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int,unordered_set<char>> rows;
        unordered_map<int,unordered_set<char>> cols;
        unordered_map<int,unordered_set<char>> sub_box;

        for(int r=0;r<9;r++){
            for(int c=0;c<9;c++){
                char cell=board[r][c];
                if(cell=='.'){
                    continue;
                }
                if(rows[r].count(cell)|| cols[c].count(cell)|| sub_box[(r/3)*3+c/3].count(cell)){
                    return false;
                }
                rows[r].insert(cell);
                cols[c].insert(cell);
                sub_box[(r/3)*3+c/3].insert(cell);
            }
        }
        return true;
    }
};
