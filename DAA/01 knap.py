def Knapsack_using_DP(profit,weight,capacity):
    n=len(profit)
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for w in range(capacity+1):
            if w==0 or i==0:
                dp[i][w]=0
            elif weight[i-1]<=w:
                dp[i][w]=max(profit[i-1]+dp[i-1][w-weight[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    selected_items=[]
    i,w=n,capacity
    while i>0 and w>0:
        if dp[i][w]!=dp[i-1][w]:
            selected_items.append(i-1)
            w=w-weight[i-1]
        i=i-1
    return dp[n][capacity],selected_items
    
if __name__ == "__main__":
    n=int(input("Enter the total no of objects: "))
    profit=[]
    weight=[]
    for i in range(n):
        ele=int(input(f"Enter the profit of {i+1}th object: "))
        profit.append(ele)
    for i in range(n):
        ele=int(input(f"Enter the weight of {i+1}th object: "))
        weight.append(ele)
    capacity=int(input("Enter the capacity of the element: "))
    ans,selected_items=Knapsack_using_DP(profit,weight,capacity)
    print("The maximum profit is: ",ans)
    for i in selected_items:
        print(f'item: {i+1} and its weight: {weight[i]} and profit: {profit[i]}')