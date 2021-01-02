<?php

function binary_search(array $array, $item){
    $start = 0;
    $end = count($array) - 1;
    while ($end >= $start){
        $middle = $start + ($end - $start) / 2;
        // check if x is present at middle
        if ($array[$middle] == $item){
            return floor($middle);
        }
        // If x greater, ignore left half
        if ($array[$middle] < $item){
            $start = $middle + 1;
        } else { // If x is smaller, ignore right half
            $end = $middle - 1;
        }
    }
    return -1;
}

$myArray = [1, 2, 3, 4, 5, 6];
echo binary_search([1, 2, 3, 4, 5, 6], 4);