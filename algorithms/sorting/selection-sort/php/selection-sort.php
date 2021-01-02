<?php

function do_sorting(array $array){
    for($i=0; $i<count($array); $i++){
        $lowNumIndex = $i;
        for($j=$i+1; $j<count($array); $j++){
            if($array[$j] < $array[$lowNumIndex]){
                $lowNumIndex = $j;
            }
        }
        if($array[$i] > $array[$lowNumIndex]){
            $tmp = $array[$i];
            $array[$i] = $array[$lowNumIndex];
            $array[$lowNumIndex] = $tmp;
        }
    }
    return $array;
}

$array = [5, 7, 9, 4, 3, 8, 2];
var_dump(do_sorting($array));