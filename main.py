from pyscript import display

business_name = 'Shoemakers StorageCup'
owner_name = 'Ledesma, Aisha Ashley' #string
year_established = 2026 #integer
popular_item_price = 5000 #integer
has_delivery = True #boolean
product_names = ['Room Corner Kit', 'Full Room', 'Full House'] #3 product names #list
business_hours = ['Monday-Thursday: 9AM-4PM', 'Saturday 8:30AM-4PM', 'Off on Fridays & Sundays'] #list
product_prices = [750, 1000, 10000] #list
commmon_requests = ['childhood bedroom', 'miniature livingroom/kitchen model', 'dream 3flr height lobby or office building'] #list
tax_rate = .08 #float
contact_information = ['+63 912 345 6789', 'For all purposes: shoemakerscup@gmail.com', '123 Creative Lane, Quezon City, Metro Manila, PH 1100', 'Shipping with: J&T Express'] #list
product_images = ['']

display(f"{business_name}", target="brand_introduction1")
display(f"YOU HAVE ARRIVEEDDDD!! HeeeEEREee at {business_name}!, {owner_name} ({year_established}).", target="brand_introduction2")

display(f"At a tax rate of... {tax_rate}", target="tax_rate")
display(f"Our prices range from {product_prices[0]}&emsp;{product_prices[1]}&emsp;{product_prices[2]}", target="product_prices")
display(f"", target="product_images")
display(f"Some common things we get requested:{commmon_requests}", target="commmon_requests")

display(f"We are open on {business_hours}! <br> Operations INCLUDE: Audience interaction, main discussion hours, inquiry services for applying clients & business inquiries.", target="business_hours")
display(f"Right now, our delivery status is: {has_delivery}", target="delivery_status")

display(f"<br>".join(contact_information), target="contact_information")
