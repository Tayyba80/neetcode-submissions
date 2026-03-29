class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> calc;
        
        for (int i = 0; i < tokens.size(); i++) {
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/") {
                int v = stoi(tokens[i]);
                calc.push(v);
            } else {
                int sec = calc.top();
                calc.pop();
                int first = calc.top();
                calc.pop();
                
                if (tokens[i] == "+") {
                    calc.push(first + sec);
                } else if (tokens[i] == "-") {
                    calc.push(first - sec);
                } else if (tokens[i] == "*") {
                    calc.push(first * sec);
                } else if (tokens[i] == "/") {
                    calc.push(first / sec);
                }
            }
        }
        
        return calc.top();
    }
};
