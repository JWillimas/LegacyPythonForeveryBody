print("-"*50)#------------------------------------------------
#Question0:How to turn str to list
#use iteration to loop the str and store it to the list

#Question1:when we got some special char in the str or list
#how to skip it?---->use continue when we loop it

print("-"*50)#------------------------------------------------
def verify_card_number(num_str):
    arr=[]
    for d in num_str:
        if d in (" ","-"):
            continue
        arr.append(int(d))

    for i in range(len(arr)-1):
        #even nums of elements in arr
        if len(arr)%2==0:
            if i%2==0:
                arr[i]*=2
                if arr[i]>9:
                    arr[i]-=9
        else:
            if i%2!=0:
                arr[i]*=2
                if arr[i]>9:
                    arr[i]-=9

    result=0
    for i in arr:
        result+=i

    if result%10==0:
        return "VALID!"
    else:
        return "INVALID!"


test="4111-1111-1111-1111"
print(verify_card_number(test))