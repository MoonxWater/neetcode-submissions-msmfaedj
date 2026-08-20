class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;
        s = s.toLowerCase();

        while (l <= r) {
            char charl = s.charAt(l);
            char charr = s.charAt(r);
            int asl = (int) charl;
            int asr = (int) charr;

            if ((asl < 97 || asl > 122) && (asl < 48 || asl > 57)) {
                System.out.println("Hello");
                l++;
            } else if ((asr < 97 || asr > 122) && (asr < 48 || asr > 57)) {
                System.out.println("hi");
                r--;
            } else if (charl != charr) {
                return false;
            } else {
                l++;
                r--;
            }
        }

        return true;
    }
}
