// check if a string is a palindrome

function isPalindrome(str) {
    // split the string into an array of characters, reverse the array, join the array back into a string
    const reversed = str.split('').reverse().join('');
    return str === reversed;
}

// example usage
const word1 = 'madam';
const word2 = 'racecar';
const word3 = 'hello';

console.log(isPalindrome(word1));//true
console.log(isPalindrome(word2));//true
console.log(isPalindrome(word3));//false