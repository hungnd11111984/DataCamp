# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())


   total_bill   tip     sex smoker  day    time  size total_dollar  \
0       16.99  1.01  Female     No  Sun  Dinner     2       $16.99   
1       10.34  1.66    Male     No  Sun  Dinner     3       $10.34   
2       21.01  3.50    Male     No  Sun  Dinner     3       $21.01   
3       23.68  3.31    Male     No  Sun  Dinner     2       $23.68   
4       24.59  3.61  Female     No  Sun  Dinner     4       $24.59   

  total_dollar_replace total_dollar_re  
0                16.99           16.99  
1                10.34           10.34  
2                21.01           21.01  
3                23.68           23.68  
4                24.59           24.59