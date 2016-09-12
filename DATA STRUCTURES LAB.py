def manipulate_data(data):
   if isinstance(data, (list)):
      positive_list = filter(lambda x: (x >= 0 and isinstance(x, int)), data)
      negative_list = filter(lambda x: (x < 0 and isinstance(x, int)), data)
      return [len(positive_list), sum(negative_list)]
   else:
      return "Only lists allowed"
      
print manipulate_data({})
print manipulate_data([1, 2, 3, 4])
print manipulate_data([1, -9, 2, 3, 4, -5])



    
    
    
