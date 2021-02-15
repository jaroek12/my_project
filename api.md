**Show User**
----
  Returns json data about a single user.

* **URL**

  /api/users/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"id":4,"username":"Test_3","email":"test3@com.pl"}`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`


* **Sample Call:**

  ```javascript
    $curl --request GET http://127.0.0.1:8000/api/users/4/;
  ```
  
  ***Show Products***
  ----
  Returns json data about a available products.

* **URL**

  /api/products/

* **Method:**

  `GET`
  
*  **URL Params**

  None

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[{"id":3,"name":"Laptop_1","desc":"The best gaming laptop","cost":"2500.99","on_stock":9},{"id":4,"name":"Laptop_2","desc":"New better version of the gaming laptop","cost":"3300.99","on_stock":20},{"id":5,"name":"Dishwasher","desc":"A good and inexpensive dishwasher","cost":"800.00","on_stock":11},{"id":6,"name":"Washing machine","desc":"The best washing machine ever made","cost":"1000.99","on_stock":15}]}`
 
* **Error Response:**

  None

* **Sample Call:**

  ```javascript
    $curl --request GET http://127.0.0.1:8000/api/products/;
  ```
  
   ***Show user orders***
  ----
  Returns json data about an user orders.

* **URL**

  /api/orders/?username=:username

* **Method:**

  `GET`
  
*  **URL Params**

  
     **Required:**
 
   `username=[string]`

* **Data Params**

  None
  
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[{"id":4,"quantity":4,"product_id":5,"username":"Test_2","total_price":"3200.00"},{"id":5,"quantity":1,"product_id":3,"username":"Test_2","total_price":"2500.99"}]`
 
* **Error Response:**

  None

* **Sample Call:**

  ```javascript
    $curl --request GET http://127.0.0.1:8000/api/orders/?username=Test_2;
  ```
     ***Add new order***
  ----
  Adding new order.

* **URL**

  /api/orders/

* **Method:**

  `POST`
  
*  **URL Params**

  None

* **Data Params**

     **Required:**
 
   `product_id=[integer]`
   `quantity=[integer]`
   `username=[string]`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"id":7,"quantity":1,"product_id":4,"username":"Test_3","total_price":"3300.99"}`
 
* **Error Response:**

  None

* **Sample Call:**

  ```javascript
    $curl --header "Content-Type: application/json" --request POST --data '{"product_id": 4, "quantity":1, "username":"Test_3"}'  http://127.0.0.1:8000/api/orders/;
  ```
       ***Delete order***
  ----
  Deleting an order.

* **URL**

  /api/orders/:id

* **Method:**

  `DELETE`
  
*  **URL Params**

     **Required:**
 
   `id=[integer]`


* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
 
* **Error Response:**

  None

* **Sample Call:**

  ```javascript
    $curl --request DELETE http://127.0.0.1:8000/api/orders/7/;
  ```
         ***Update order***
  ----
  Uptading an order.

* **URL**

  /api/orders/:id

* **Method:**

  `PUT`
  
*  **URL Params**

     **Required:**
 
   `id=[integer]`


* **Data Params**

   `product_id=[integer]`
   `quantity=[integer]`
   `username=[string]`

* **Success Response:**

  * **Code:** 200 <br />
  **Content:** `{"id":6,"quantity":1,"product_id":4,"username":"Test_3","total_price":"3300.99"}`
 
* **Error Response:**

  None

* **Sample Call:**

  ```javascript
    $curl --header "Content-Type: application/json" --request PUT --data '{"product_id": 4, "quantity":1, "username":"Test_3"}'  http://127.0.0.1:8000/api/orders/6;
