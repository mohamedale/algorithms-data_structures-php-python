<?php

$array = [9, 5, 7, 2, 3, 1, 4];

for($i=1; $i<count($array); $i++){
    $key = $array[$i];
    $j = $i - 1;

    while ($j>=0 && $array[$j] > $key){
        $array[$j + 1] = $array[$j];
        $j--;
    }
    $array[$j + 1] = $key;
}

var_dump($array);