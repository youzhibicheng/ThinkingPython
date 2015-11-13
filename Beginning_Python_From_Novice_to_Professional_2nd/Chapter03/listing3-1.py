# Print a formatted price list with a given width

width = input('Please enter width: ')

price_width = 10
item_width = width - price_width

# % 转换说明符开始
# - 左对齐
# + 在转换之前要加上正负号
# 0 表示转换值如果位数不够用0填充
# * 最小宽度值
header_format = '%-*s%*s'
format       = '%-*s%*.2f'

print '=' * width

print header_format % (item_width, 'Item', price_width, 'Price')

print '-' * width

print format % (item_width, 'Apples', price_width, 0.4)
print format % (item_width, 'Pears', price_width, 0.5)
print format % (item_width, 'Cantaloupes', price_width, 1.92)
print format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8)
print format % (item_width, 'Prunes (4 lbs.)', price_width, 12)

print '=' * width