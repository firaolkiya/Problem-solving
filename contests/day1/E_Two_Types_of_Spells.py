light=0

lightning=0
free =0
free_spell =0
for _ in range(int(input())):
    tp,powo = map(int,input().split())
    if tp==1:
        light+=(powo//abs(powo))
        lightning+=powo
    else:
        free+=(powo//abs(powo))
        free_spell+=powo
        
    