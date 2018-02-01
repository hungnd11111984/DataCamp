# Merge site and visited: m2m
print(site.head())
print(visited.head())
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')
print(survey.head())
# Print the first 20 lines of m2m
print(m2m.head(20))

### Results 
    name    lat    long
0   DR-1 -49.85 -128.57
1   DR-3 -47.15 -126.72
2  MSK-4 -48.87 -123.40
   ident  site       dated
0    619  DR-1  1927-02-08
1    622  DR-1  1927-02-10
2    734  DR-3  1939-01-07
3    735  DR-3  1930-01-12
4    751  DR-3  1930-02-26
   taken person quant  reading
0    619   dyer   rad     9.82
1    619   dyer   sal     0.13
2    622   dyer   rad     7.80
3    622   dyer   sal     0.09
4    734     pb   rad     8.41
     name    lat    long  ident   site       dated  taken person quant  \
0    DR-1 -49.85 -128.57    619   DR-1  1927-02-08    619   dyer   rad   
1    DR-1 -49.85 -128.57    619   DR-1  1927-02-08    619   dyer   sal   
2    DR-1 -49.85 -128.57    622   DR-1  1927-02-10    622   dyer   rad   
3    DR-1 -49.85 -128.57    622   DR-1  1927-02-10    622   dyer   sal   
4    DR-1 -49.85 -128.57    844   DR-1  1932-03-22    844    roe   rad   
5    DR-3 -47.15 -126.72    734   DR-3  1939-01-07    734     pb   rad   
6    DR-3 -47.15 -126.72    734   DR-3  1939-01-07    734   lake   sal   
7    DR-3 -47.15 -126.72    734   DR-3  1939-01-07    734     pb  temp   
8    DR-3 -47.15 -126.72    735   DR-3  1930-01-12    735     pb   rad   
9    DR-3 -47.15 -126.72    735   DR-3  1930-01-12    735    NaN   sal   
10   DR-3 -47.15 -126.72    735   DR-3  1930-01-12    735    NaN  temp   
11   DR-3 -47.15 -126.72    751   DR-3  1930-02-26    751     pb   rad   
12   DR-3 -47.15 -126.72    751   DR-3  1930-02-26    751     pb  temp   
13   DR-3 -47.15 -126.72    751   DR-3  1930-02-26    751   lake   sal   
14   DR-3 -47.15 -126.72    752   DR-3         NaN    752   lake   rad   
15   DR-3 -47.15 -126.72    752   DR-3         NaN    752   lake   sal   
16   DR-3 -47.15 -126.72    752   DR-3         NaN    752   lake  temp   
17   DR-3 -47.15 -126.72    752   DR-3         NaN    752    roe   sal   
18  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14    837   lake   rad   
19  MSK-4 -48.87 -123.40    837  MSK-4  1932-01-14    837   lake   sal   

    reading  
0      9.82  
1      0.13  
2      7.80  
3      0.09  
4     11.25  
5      8.41  
6      0.05  
7    -21.50  
8      7.22  
9      0.06  
10   -26.00  
11     4.35  
12   -18.50  
13     0.10  
14     2.19  
15     0.09  
16   -16.00  
17    41.60  
18     1.46  
19     0.21