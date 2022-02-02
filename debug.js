//Debug the functions kata level 7
//Kata's link: https://www.codewars.com/kata/5844a422cbd2279a0c000281/train/javascript



function multi(arr) {
    let result = 1;
    for(const i of arr){
      result*=i;
    }
    return result;
  }
  function add(arr) {
    let result = 0;
    for(const i of arr){
      result+=i;
    }
    return result;
  }
  function reverse(str) {
    return str.split("").reverse().join("");
  }