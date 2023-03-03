import sqlparse

raw_input = "select sum(sales),region_name, product_name from sales_tbl sales \
inner join region_tbl region \
on sales.region_id = region.region_id \
inner join product_tbl product \
on sales.product_id = product.product_id \
where upper(region_name)='APAC' and upper(product_name) ='KEYBOARD' \
group by region_name, product_name;"


statements = sqlparse.split(raw_input)
print(statements)


print(sqlparse.format(raw_input, reindent=True, keyword_case='upper'))

parsed = sqlparse.parse(raw_input)[0]
l=[]
print(parsed.tokens)
tkns = parsed.tokens
#print(parsed)
for i in tkns:
    print(i.ttype)
    #print(i.flatten())
    for j in i.flatten():
        print(j)
