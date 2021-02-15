<?php

// low  --> Starting index,  high  --> Ending index
function partition(&$arr, $low, $high){
    // to put it in the right position
    $pi = $arr[$high];
    // index of smaller element
    $i = $low - 1;

    for ($j=$low; $j<$high; $j++){
        // If current element is smaller than the pivot
        if ($arr[$j] < $pi){
            // increment index of smaller element
            $i++;
            // swapping
            $tmp1 = $arr[$i];
            $tmp2 = $arr[$j];
            $arr[$j] = $tmp1;
            $arr[$i] = $tmp2;
        }
    }
    // swapping
    $tmp3 = $arr[$i+1];
    $tmp4 = $arr[$high];
    $arr[$high] = $tmp3;
    $arr[$i+1] = $tmp4;

    return $i + 1;
}

function quick_sort(&$arr, $low, $high){
    if ($low < $high){
        // pi is partitioning index, $arr[pi] is now at right place
        $pi = partition($arr, $low, $high);
        // recursion
        quick_sort($arr, $low, $pi-1); // before pi
        quick_sort($arr, $pi+1, $high); // after pi
    }
    return $arr;
}

$unSortedArr = [9, 2, 7, 8, 3, 4];
print_r(quick_sort($unSortedArr, 0, count($unSortedArr)-1));