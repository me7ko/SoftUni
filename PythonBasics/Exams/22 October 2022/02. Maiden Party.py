price_girls_party = float(input())
love_msg_count = int(input())
vosuk_count_roses = int(input())
keychain_count = int(input())
karikaturi_count = int(input())
luck_count = int(input())


total_count = love_msg_count + vosuk_count_roses + keychain_count + karikaturi_count + luck_count
total_love_msg = love_msg_count * 0.6
total_vosuk_rose = vosuk_count_roses * 7.2
total_keychain = keychain_count * 3.6
total_karikaturi = karikaturi_count * 18.2
total_luck = luck_count * 22

total_money = total_love_msg + total_vosuk_rose + total_keychain + total_karikaturi + total_luck
total_money *= 0.9
if total_count >= 25:
    total_money *= 0.65


diff = abs(total_money - price_girls_party)
if total_money >= price_girls_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

