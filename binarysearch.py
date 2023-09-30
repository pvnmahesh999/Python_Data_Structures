def binary(elements,query):
    low=0
    high=len(elements)-1
    while low<=high:
         mid=(low+high)//2
         if elements[mid]==query:
             if len(elements)>1:
                if elements[mid-1]==elements[mid]:
                    high=mid-1
                elif elements[mid-1]!=elements[mid]:
                    return mid
             elif len(elements)==1:
                return mid
         elif elements[mid]>query:
             high=mid-1
         elif elements[mid]<query:
             low=mid+1
    return -1
    
testcases=[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
 {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
 {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
 {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
 {'input': {'cards': [6], 'query': 6}, 'output': 0},
 {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
 {'input': {'cards': [], 'query': 7}, 'output': -1},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
  'output': 7},
 {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
  'query': 6},
  'output': 2}]
            
for j in range(0,len(testcases)):
    position=binary(testcases[j]['input']['cards'],testcases[j]['input']['query'])
    if position==testcases[j]['output']:
        print("{} test case passed".format(j+1))
