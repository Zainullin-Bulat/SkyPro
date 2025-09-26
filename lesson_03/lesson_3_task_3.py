from address import Address
from mailing import Mailing

to_address = Address("111111", "Казань", "1ая", "1", "2")
from_address = Address("222222", "Москва", "2ая", "3", "4")

mailing = Mailing(to_address, from_address, "99.99", "TRACK123")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, \
{mailing.from_address.city}, {mailing.from_address.street}, \
{mailing.from_address.house} - {mailing.from_address.apartment} в \
{mailing.to_address.index}, {mailing.to_address.city}, \
{mailing.to_address.street}, {mailing.to_address.house} - \
{mailing.to_address.apartment}.\
Стоимость {mailing.cost} рублей.")
