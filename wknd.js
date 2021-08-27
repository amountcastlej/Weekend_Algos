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

//Alan is good at breaking secret codes. 
//One method is to eliminate values that lie within a specific known range. 
//Given arr and values min and max, retain only the array values between min and max. 
//Work in-place: return the array you are given, with values in original order. No built-in array functions.

function filterRange(arr, min, max){
    for (var i = 0; i < arr.length; i++){
        if(arr[i] <= min || arr[i] >= max){
        var temp = arr[i];
        for (var j=i; j<arr.length-1; j++){
            arr[j] = arr[j+1];
        }
        arr[arr.length-1] = temp;
        arr.pop();
        i--;
    }
    else {

    }
    }
    return arr;
}
console.log(filterRange([1, 3, 5, 7, 10], 4, 8))

//Create threesFives(n) that adds values from 1 and n (inclusive) if that value is not divisible by 3 or 5. Return the final sum.
function threesFives(num){
var sum = 0;
for (var i = 1; i <= num; i++){
    if(i % 3 ==0 || i % 5 == 0){
        console.log(i, 'is divisible by 3 and five');
    }
    else {
        sum += i;
} 
}
return sum;
