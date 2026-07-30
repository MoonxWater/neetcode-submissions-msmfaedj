class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> brackets = new HashMap<>();
        brackets.put(')', '(');
        brackets.put(']', '[');
        brackets.put('}', '{');

        for (char c : s.toCharArray()) {
            if (brackets.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == brackets.get(c)) {
                    stack.pop();
                } else return false;
            } else stack.push(c);
            
        }

        return stack.isEmpty();
    }

}
