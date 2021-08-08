// Given two strings s & t, determine if they are isomorphic.
// Two strings s & t are isomorphic if the characters in s can be replaced to get t
// All occurences of a character must be replaced with another character while preserving the order of characters
// No two characters may be the same

var isIsomorphic = function(s, t) {
    if (s.length != t.length) return false
    var data = {};
    for (i = 0; i < s.length; i++) {
        if (!data[s[i]]) {
            if (Object.values(data).indexOf(t[i]) > -1) return false
            data[s[i]] = t[i];
        } else {
            if (data[s[i]] != t[i]) return false
        }
    }
    return true;
};

console.log(isIsomorphic("egg11e", "add33a"))

//Longest Substring without repeating characters
//Given a string s, find the length of the longest substring without repeating characters

var lengthOfLongestSubstring = function(s) {
    let l = "";
    for (let i = 0; i < s.length; i++) {
        let t = "";
        for (let j = i; j < s.length; j++) {
            if (t.indexOf(s[j]) < 0) {
                t = t + s[j];
            } else {
                break;
            }
        }
        if (t.length > l.length) {l = t}
    }
    return l.length;
};

console.log(lengthOfLongestSubstring("abcabcasdf"))