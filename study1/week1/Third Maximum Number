class Third Maximum Number {

    int count = 3;            
    int tmp = Integer.MIN_VALUE;

    public int thirdMax(int[] nums) {              // Space Complexity= O(n), n is the length of the Array
      Arrays.sort(nums);                          // time complexity = O(n * log(n))
      if(nums.length <3){    
          return nums[nums.length-1];
      }else{
         for(int i=nums.length-1; i>=0 ; i--){   // time complexity = O(m), m is the position, where the third maximum number is set
             if(tmp != nums[i]){
                 count -= 1;
             }
              tmp = nums[i];
            if(count ==0){
                break;
            }
         }
        if(count ==0){
           return tmp;
         }else{
           return nums[nums.length-1];
         }
      }
    }
}

// Time Complexity :  O(n * log(n))
// Space Complexity :  O(n)
