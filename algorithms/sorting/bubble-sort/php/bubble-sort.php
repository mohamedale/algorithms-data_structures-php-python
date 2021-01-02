<?php

function bubble_sort(array $array){
    for ($i=0; $i < count($array); $i++){
        $swapped = false; // for Optimized Implementation:
        for ($m=0; $m < count($array) -$i - 1; $m++){
            if ($array[$m] > $array[$m + 1]) {
                $number = $array[$m];
                $array[$m] = $array[$m + 1];
                $array[$m + 1] = $number;
                $swapped = true;
            }
        }
        if (!$swapped)
            break;
    }
    return $array;
}

$array = [7, 5, 2, 3, 8];
var_dump(bubble_sort($array));