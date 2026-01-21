# JavaScript Logic & Algorithms Practice

This file contains "must-know" algorithms and logic patterns for coding interviews and practice. You can implement these in a `.js` file to test them out.

## 1. FizzBuzz (Basic Logic)
A classic test of basic loops and conditionals.
Print numbers 1 to 100. If divisible by 3, print "Fizz". If by 5, "Buzz". If both, "FizzBuzz".

```javascript
function fizzBuzz(n) {
    for (let i = 1; i <= n; i++) {
        let output = "";
        if (i % 3 === 0) output += "Fizz";
        if (i % 5 === 0) output += "Buzz";
        console.log(output || i);
    }
}
fizzBuzz(15);
```

## 2. Palindrome Check (Strings & Pointers)
Check if a string reads the same forward and backward.
*Technique: Two pointers (start and end).*

```javascript
function isPalindrome(str) {
    // Remove non-alphanumeric chars and lowercase
    const cleanStr = str.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    let authors = 0;
    let end = cleanStr.length - 1;

    while (start < end) {
        if (cleanStr[start] !== cleanStr[end]) return false;
        start++;
        end--;
    }
    return true;
}
console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
```

## 3. Two Sum (Hash Maps)
Find two numbers in an array that add up to a target.
*Technique: Use an object/Map for O(n) lookups.*

```javascript
function twoSum(nums, target) {
    const map = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);
    }
    return [];
}
console.log(twoSum([2, 7, 11, 15], 9)); // [0, 1]
```

## 4. Binary Search (O(log n))
Efficiently find an item in a **sorted** array.
*Technique: Divide and conquer.*

```javascript
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (arr[mid] === target) return mid;
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
console.log(binarySearch([1, 2, 3, 4, 5, 6, 7], 5)); // 4
```

## 5. Fibonacci (Recursion vs Memoization)
Calculate the Nth Fibonacci number.
*Technique: Optimization via caching (Memoization).*

```javascript
// O(2^n) - Very Slow
function fibRecursive(n) {
    if (n <= 1) return n;
    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// O(n) - Fast
function fibMemo(n, memo = {}) {
    if (n in memo) return memo[n];
    if (n <= 1) return n;
    
    memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
    return memo[n];
}
console.log(fibMemo(50)); // 12586269025
```

## 6. Depth-First Search (DFS) - Tree Traversal
Basic traversal of a tree structure.
*Technique: Recursive exploration.*

```javascript
const tree = {
    value: 1,
    children: [
        { value: 2, children: [] },
        { value: 3, children: [
            { value: 4, children: [] }
        ]}
    ]
};

function dfs(node) {
    if (!node) return;
    console.log(node.value);
    node.children.forEach(dfs);
}
dfs(tree); // 1, 2, 3, 4
```
