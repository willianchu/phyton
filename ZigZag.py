def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1 # first"
    print("mid:", mid)
    a[mid], a[n-1] = a[n-1], a[mid]
    print("inicial a:", a)

    st = mid + 1
    print ("st:", st)
    ed = n - 2 # second
    print ("ed:", ed)
    
    while(st <= ed):
        print("st:", st, "ed:", ed)
        a[st], a[ed] = a[ed], a[st]
        print("after a:", a)
        st = st + 1
        ed = ed - 1 # third

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

# test_cases = int(input())
# for cs in range (test_cases):
#     n = int(input())
#     a = list(map(int, input().split()))
#     findZigZagSequence(a, n)

print(findZigZagSequence([1,2,3,4,5], 5))

print(findZigZagSequence([1,2,3,4,5,6,7], 7))