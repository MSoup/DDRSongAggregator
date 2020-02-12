import scrapy

table = response.xpath('//*[@class="wikitable sortable"]//tbody')
rows = table.xpath('//tr')

#Using scrapy I found out there were 14 empty fields after
#so I want to iterate through 1-len(rows)-13
for col in range(len(rows)-13):
  row = rows[col]
  print(row.xpath('td//text()')[col].extract())