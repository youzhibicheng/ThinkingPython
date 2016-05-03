>>> import bisect
>>> farm=sorted(['haystack','needle','cow','pig'])
>>> farm
['cow', 'haystack', 'needle', 'pig']
>>> bisect.bisect(farm,'needle')
3
>>> bisect.bisect_left(farm, 'needle')
2
>>> bisect.bisect(farm, 'chicken')
0
>>> bisect.bisect(farm, 'eggs')
1
>>> bisect.bisect_left(farm, 'eggs')
1
# very strange, is there a 'eggs'???
# just identify where to insert

