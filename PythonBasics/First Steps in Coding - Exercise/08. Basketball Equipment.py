tax_for_year = int(input())

basket_kec = tax_for_year - (tax_for_year * 0.4)
ekip = basket_kec - (basket_kec * 0.2)
basket_ball = ekip / 4
basket_accessoaries = basket_ball / 5

total =tax_for_year + basket_kec + ekip + basket_ball + basket_accessoaries
print(total)
