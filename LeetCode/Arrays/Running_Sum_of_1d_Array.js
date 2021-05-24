var runningSum = function (nums) { 
    let val = 0;
    let sum = nums.map(res=>{
        val = res + val;
        return val;
    });
    console.log(sum);
};

runningSum([1,2,3,]);