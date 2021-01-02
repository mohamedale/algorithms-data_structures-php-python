<?php

function linear_search(array $array, $item){
    for ($i=0; $i < count($array); $i++){
        if ($array[$i] == $item){
            return $i;
        }
    }
    return -1; // mean this element not found
}

echo linear_search([1, 2, 3, 4, 5, 6], 2);
