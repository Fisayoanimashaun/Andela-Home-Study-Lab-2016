def manipulate_data(lists):
   if isinstance(lists, (list, set, tuple)):
      positive_list = filter(lambda x: x >= 0, lists)
      negative_list = filter(lambda x: x < 0, lists)
      return [len(positive_list), sum(negative_list)]

print manipulate_data((0,1,2,5,-2,-4,0,-1))


    
    
    
