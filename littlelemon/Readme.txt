http://127.0.0.1:8000/restaurant/menu/      the static html page

http://127.0.0.1:8000/restaurant/menu/items/  list and create menu items

http://127.0.0.1:8000/restaurant/menu/items/<int:pk>  update and retrieve and delete an existing item

http://127.0.0.1:8000/restaurant/booking/tables/ list and create booking (must be authorized using http://127.0.0.1:8000/restaurant/menu/api-token-auth/ to obtain auth token)

http://127.0.0.1:8000/restaurant/booking/tables/ update and retrieve and delete an existing booking (must be authorized using http://127.0.0.1:8000/restaurant/menu/api-token-auth/ to obtain auth token)

http://127.0.0.1:8000/auth/token/login login to obtain djoser token

http://127.0.0.1:8000/auth/token/logout/ logout a djoser token