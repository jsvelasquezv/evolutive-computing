#!/bin/bash
for reinas in 8 10 12 14; 
do
	for iteraciones in 1000 5000 10000; 
	do
		python ./Main.py $reinas 100 $iteraciones 15 5 experimento-reinas-$reinas.txt
	done
done
