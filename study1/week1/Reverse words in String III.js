/**
 * @param {string} s
 * @return {string}
 */

//  떠오른데로 풀기
//  O(n^2)
/**
 *  for문 안에 for문을 넣어서 돌려서 n*n형태의 연산이 이루어진다
 *  때문에 O(n^2)
 */
var reverseWords = function(s) {
    let returnVal ='';
    const tmp = s.split(" ");

    tmp.forEach((element) => {
        const wordInArr = element.split("");
        let tmpWord ='';
        for (let i = wordInArr.length-1; i >= 0; i--) {
            tmpWord += wordInArr[i];
        }
        returnVal += tmpWord;
        if(element != tmp.at(-1)){
            returnVal += ' ';
        }
    });

    return returnVal;
};

reverseWords('hello world man! zahooyy');


//  다른방법으로 풀기
//  O(n^2)
/**
 *  for문이 있고 그 안에 돌아가는 reverseString이 재귀형태로 작동해서
 *  이것도 마찬가지로 O(n^2) 이다
 */
var reverseWords = function(s) {
    let returnVal ='';
    const wordsArr = s.split(" ");

    wordsArr.forEach(element => {
        const wordInArr = element.split('');
        returnVal += reverseString(wordInArr,0,wordInArr.length-1).join('');
        if(element != wordsArr.at(-1)){
            returnVal += ' ';
        }
    });

    return returnVal;
};


var swap = function(arr, start, end) {
    let tmp = arr[start];
    arr[start] = arr[end];
    arr[end] = tmp;
    
    return arr;
};

var reverseString = function(arr,start, end){
       if (start < end){
        let tmp = swap(arr,start,end);
        return reverseString(tmp,start+1,end-1)
    } else {
        return arr;
    }
};

reverseWords('hello world man! zahooyy');